"""eoio.example_reader_structure - example reader class"""  # multi-spectral base reader?
import glob
import os
import numpy as np
import rioxarray as rxr
import xarray as xr
import json
import rasterio
import re
import warnings
import pyproj

from dateutil.parser import parse
from typing import Optional, Dict, Any, Union, Tuple
from copy import deepcopy
from rasterio.crs import CRS
from shapely.geometry import shape, Polygon

from eoio.readers.base import BaseReader
from eoio.utils.tif_tools import *
from eoio.utils.crs_utils import *
from eoio.utils.dict_tools import *

__author__ = "Mattea Goalen <mattea.goalen@npl.co.uk>"

__all__ = ["ExampleReader"]


class ExampleReader(BaseReader):
    """
    Example File Reader
    """

    _default_subset_dict = {
        "bands": True,
        "read_img": True,
        "roi": None,
        "roi_crs": 4326,
        "metadataLevel": True,
        "masks": None,
        "aux_data": None,
    }
    _default_read_dict = {}

    # used for the setting of the product bands (and you'll probably find it useful to have in general)
    band_res = {
        "B1": 30,
        "B2": 30,
        "B3": 30,
        "B4": 30,
        "B5": 30,
        "B6": 30,
        "B7": 30,
        "B8": 30,  # 15
        "B9": 30,
        "B10": 15,
        "B11": 30,
        "BQA": 30,
    }

    # plus any related class attributes that you might need for reading in masks etc

    def __init__(
            self,
            path,
            subset_info: Optional[Dict[str, Any]] = None,
            read_params: Optional[Dict[str, Any]] = None,
    ):
        """Initialise the reader"""
        super(ExampleReader, self).__init__(path, subset_info, read_params)

        # attributes inherent to the specified product
        self._available_bands = None
        self._bounds = None
        self._default_crs = None

        # subsetting attributes
        self._aux_data = None
        self._crs = None
        self._geometries = None
        self._masks = None
        self._meta_level = None
        self._roi = None
        self._selected_product_bands = None

        # initialise dataset
        self.ds = None

    # ----------------------------------------------------------------------------------------------------------------------

    @property
    def available_bands(self) -> list:
        """
        Return all available bands in product
        """
        if self._available_bands is None:
            self._parse_available_bands()
        return self._available_bands

    @property
    def aux_data(self) -> list:
        """
        Return list of auxiliary data selected
        """
        return self._aux_data

    @aux_data.setter
    def aux_data(self, aux_data: Optional[Union[list, str]]):
        """
        Set list of auxiliary data requested
        """
        self._aux_data = None  # if you do not have auxiliary data leave as None
        raise NotImplementedError

    @property
    def bounds(self) -> Dict[str, Any]:
        """
        Return coordinate bounds of the Satellite Product
        """
        if self._bounds is None:
            self._parse_product_geom_info()
        return self._bounds

    @property
    def crs(self):
        """
        Return requested subsetting coordinate reference system
        """
        if self._crs is None:
            roi = self.subset_info["roi"], self.subset_info["roi_crs"]
            self._set_requested_geom_info(roi)
        return self._crs

    @property
    def default_crs(self):
        """
        Return product default coordinate reference system
        """
        if self._default_crs is None:
            self._parse_product_geom_info()
        return self._default_crs

    @property
    def geometries(self):
        """
        Return region of interest in geometry form: [{"type": "Polygon", "coordinates": [list of coordinates]}]
        """
        if self._geometries is None:
            roi = self.subset_info["roi"], self.subset_info["roi_crs"]
            self._set_requested_geom_info(roi)
        return self._geometries

    @geometries.setter
    def geometries(self, roi_geometry: Optional[Dict[str, Polygon]]):
        """
        Set the geometry with which to clip the satellite data

        Note (regarding geometry setting and image reading)
            -----------------------------------------------------------------------------------------------------
            -----------------------------------------------------------------------------------------------------
            - Image reading
            If a crs is associated with an image it can be clipped with a geometry during opening using:
                rioxarray.open_rasterio.rio.clip(geometries, from_disk = True)
            - Geometry setting
            The geometries in this setter can then simply be set with:
                self._geometries = roi_geometry

            Example satellite products: Sentinel 2, Landsat 8 & 9
            -----------------------------------------------------------------------------------------------------
            -----------------------------------------------------------------------------------------------------

            In cases where a crs is not associated with an image when read in (you'll notice this warning message
            being thrown up by rioxarray when opening the image with rioxarray.open_rasterio():
                NotGeoreferencedWarning: Dataset has no geotransform, gcps, or rpcs. The identity matrix be returned.
                warnings.warn(str(rio_warning.message), type(rio_warning.message))  # type: ignore
            )
            the roi coordinates in the dimensions of the dataset must first be calculated and used to create a
            shapely.geometry.Polygon which can then be used to create geometries with which to clip image data.

            - Image reading
            To clip with this geometry once made, it is likely that a(n arbitrary) crs will first need to be assigned
            to the dataset. This can be done using:
                img_dataset.rio.set_crs(arbitrary_crs)
                where img_dataset is the image dataset that has just been read in, and arbitrary crs is any crs input
                accepted by rasterio.crs.CRS.from_user_input.
                https://corteva.github.io/rioxarray/stable/rioxarray.html#rioxarray.rioxarray.XRasterBase.set_crs
            The dataset can then be clipped using the img_dataset.rio.clip(geometries) function as for above
            - Geometry setting
            The geometry creation function described above is currently in development (and will also probably include


            Example satellite products: Sentinel 3, PRISMA

            ------------------------------------------------------------------------------------------------------

            :param roi_geometry: dictionary of form [{"type": "Polygon", "coordinates": [list of coordinates]}]
        """
        self._geometries = None
        raise NotImplementedError

    @property
    def masks(self):
        """
        Return requested product masks
        """
        return self._masks

    @masks.setter
    def masks(self, subset_masks: Union[list, str]):
        """
        Set requested product masks

        :param subset_masks: subset of requested product masks, either in list or string if only single mask requested
        """
        self._masks = None
        raise NotImplementedError

    @property
    def meta_level(self):
        """
        Return requested metadata level or whether or not it is desired
        """
        return self._meta_level

    @meta_level.setter
    def meta_level(self, meta_level: Optional[Union[bool, str]]):
        """
        Set metadata requested

        Examples from other satellites
        Landsat 8/9 options: [None, True, False]
        Sentinel 2 options: [None, True, False, "basic", "partial", "full"]
        """
        self._meta_level = None
        raise NotImplementedError

    @property
    def selected_product_bands(self) -> list:  # selected bands
        """
        Return the bands of the product requested by the user

        :return : list of the selected bands within the Sentinel-2 product
        """
        return self._selected_product_bands

    @selected_product_bands.setter
    def selected_product_bands(self, new_bands: Optional[Union[list, str, int, bool]]) -> None:
        """
        Set the selected product and spectral bands from the supplied new_bands

        If int supplied, self._selected_product_bands set to all bands of the desired resolution

        :param new_bands: list/str containing requested product bands or int of a desired band resolution

        """
        self._set_product_bands(new_bands)

    @property
    def roi(self) -> Polygon:
        """
        Return subsetting region of interest as a shapely.Polygon

        :return : shapely.Polygon of the selected region of interest
        """
        return self._roi

    @roi.setter
    def roi(self, roi: Tuple[Union[tuple, list, Polygon, None], int]) -> None:
        """
        Set the selected geometry/geographical information from provided region of interest

        Region of interest can be defined as a list of coordinates, a shapely Polygon,
        or a tuple containing a central point and a half box width from which to make
        a box in UTM projected coordinates around the central point.

        :param roi: region of interest tuple, containing both the desired region of
                    interest and the epsg code of the coordinate reference system it is defined in
        """
        self._set_requested_geom_info(roi)

    # ------------------------------------------------------------------------------------------------------------------

    def _parse_available_bands(self) -> None:
        """
        Parse through the product and set self._available_bands to all available bands in product
        """
        self._available_bands = ["split" + i + "however_you_need_to" for i in
                                 glob.glob(os.path.join(self.path, "your_band_pattern"))]

    def _parse_product_geom_info(self) -> None:
        """
        Parse through product geographically/geometric info and set relevant attributes

        Sets the default coordinate reference system and the bounds of the image.

        Example generation of default crs = rasterio.crs.CRS.from_epsg(4326)
        Example bounds:
            bounds = {
                "EPSG:4326": Polygon([lat_lon_0, lat_lon_1, lat_lon_2, lat_lon_3]),
                str(crs): Polygon([[x_0, y_0], [x_1, y_0], [x_1, y_1], [x_0, y_1]]),
            }
        """
        self._default_crs = None  # for PRISMA and Sentinel 3 this is likely to remain as None
        self._bounds = None  # for PRISMA and Sentinel 3 this will only contain one key "EPSG:4326" with a
        # corresponding value, please do include a second empty dictionary item {"":""} so as not to throw up an error
        # in self._set_requested_geom_info

        raise NotImplementedError

    def _set_product_bands(self, new_bands: Union[list, str, int]) -> None:
        """
        Check and set the selected product and spectral bands from the supplied new_bands

        If int supplied, self._selected_product_bands set to all bands of the desired resolution

        :param new_bands: list/str containing requested product bands or int of a desired band resolution
        """
        if not new_bands:
            self._selected_product_bands = []
        elif new_bands is True:
            self._selected_product_bands = self.available_bands
        elif isinstance(new_bands, str):
            if new_bands in self.available_bands:
                self._selected_product_bands = [new_bands]
            else:
                raise ValueError(
                    "'{}' not in '{}'. Please select from: {}.".format(
                        new_bands, self.path, self.available_bands
                    )
                )
        elif isinstance(new_bands, int):
            if new_bands not in self.band_res.values():
                raise ValueError(
                    "'{}' not a valid resolution. Please select from: {}".format(
                        new_bands, [*set(list(self.band_res.values()))]
                    )
                )
            else:
                bands = [
                    bnd
                    for bnd, res in self.band_res.items()
                    if res == new_bands and bnd in self.available_bands
                ]
                if len(bands) == 0:
                    raise ValueError(
                        "No bands available in '{}' for resolution '{}'".format(
                            self.path, new_bands
                        )
                    )
                else:
                    self._selected_product_bands = bands
        elif isinstance(new_bands, list):
            if all([i in self.available_bands for i in new_bands]):
                self._selected_product_bands = new_bands
            else:
                bad_bands = [i for i in new_bands if i not in self.available_bands]
                raise ValueError(
                    "{} not in '{}'. Please select from: {}.".format(
                        bad_bands, self.path, self.available_bands
                    )
                )
        else:
            raise ValueError(
                "'{}' not in '{}'. Please select from: {}.".format(
                    new_bands, self.path, self.available_bands
                )
            )

    def _set_requested_geom_info(self, roi: Tuple[Union[tuple, list, Polygon, None], int]) -> None:
        """
        Set the geometry related information from the requested region
        of interest and coordinate reference system

        Region of interest can be defined as a list of coordinates, a shapely Polygon,
        or a tuple containing a central point and a half box width from which to make
        a box in UTM projected coordinates around the central point.

        :param roi: region of interest tuple, containing both the desired region of
                    interest and the epsg code of the coordinate reference system it is defined in
        """
        roi_coords, roi_crs = roi

        if isinstance(roi_coords, tuple):
            if len(roi_coords) == 2:
                point, hw = roi_coords
                if isinstance(point, tuple) and isinstance(hw, (float, int)):
                    try:
                        roi_coords = self.generate_bounding_box(
                            CRS.from_epsg(roi_crs), self.default_crs, point, hw
                        )
                        roi_crs = self.default_crs.to_epsg()
                    except pyproj.exceptions.CRSError:
                        raise ValueError(
                            """Sensor data not able to be subset with Square About a Point 
                            ((lon, lat), half_box_width_in_meters) method, please try alternative.""")
                else:
                    raise ValueError(
                        """Incorrect formatting of ((lon, lat), half_box_width_in_meters).
                                Please input half_box_width_in_meters as a float or int, and (lon, lat) as a tuple."""
                    )

        if self.default_crs:
            product_coords = self.bounds[str(CRS.from_epsg(roi_crs))]
        else:
            product_coords = self.bounds["EPSG:4326"]  # see bounds property for applicable cases

        if isinstance(roi_coords, list):
            try:
                roi_coords = Polygon(roi_coords)
            except TypeError:
                raise ValueError(
                    """Please input an accepted roi format of form:
                             Region of interest coordinates: [
                                                              [xmin,ymax],
                                                              [xmax,ymax],
                                                              [xmax,ymin],
                                                              [xmin,ymin],
                                                              [xmin,ymax],
                                                             ]
                             or Square About a Point ((lon,lat), half_box_width_in_meters) 

                             Please select coordinates within bounds: 
                            {} : {}
                            {} : {}""".format(
                        list(self.bounds.keys())[0],
                        list(list(self.bounds.values())[0].exterior.coords),
                        list(self.bounds.keys())[1],
                        list(list(self.bounds.values())[1].exterior.coords),
                    )
                )
        if not roi_coords:
            self._roi = None
            self._crs = CRS.from_epsg(roi_crs)
            self.geometries = None
        elif isinstance(roi_coords, Polygon):
            if product_coords.contains(roi_coords):
                self._roi = roi_coords
                self._crs = CRS.from_epsg(roi_crs)
                self.geometries = self.roi_to_geom(self.roi)
            elif product_coords.intersects(roi_coords):
                self._roi = roi_coords
                self._crs = CRS.from_epsg(roi_crs)
                self.geometries = self.roi_to_geom(self.roi)  # TODO - update this in Sentinel 2 and Landsat 8/9 readers
                warnings.warn(
                    """Region of interest: {} : {}
                     not fully within bounds of the image.
            Consider changing coordinates to those within bounds:
            {} : {}
            {} : {}""".format(
                        CRS.from_epsg(roi_crs),
                        list(roi_coords.exterior.coords),
                        list(self.bounds.keys())[0],
                        list(list(self.bounds.values())[0].exterior.coords),
                        list(self.bounds.keys())[1],
                        list(list(self.bounds.values())[1].exterior.coords),
                    )
                )
            else:
                raise ValueError(
                    """Region of interest: {} : {}
                     not within bounds of the image.
                             Please select coordinates within bounds: 
                            {} : {}
                            {} : {}""".format(
                        CRS.from_epsg(roi_crs),
                        list(roi_coords.exterior.coords),
                        list(self.bounds.keys())[0],
                        list(list(self.bounds.values())[0].exterior.coords),
                        list(self.bounds.keys())[1],
                        list(list(self.bounds.values())[1].exterior.coords),
                    )
                )
        else:
            raise ValueError(
                """Please input an accepted roi format of form:
                         Region of interest coordinates: [
                                                          [xmin,ymax],
                                                          [xmax,ymax],
                                                          [xmax,ymin],
                                                          [xmin,ymin],
                                                          [xmin,ymax],
                                                         ]
                         or Square About a Point ((lon,lat), half_box_width_in_meters) 

                         Please select coordinates within bounds: 
                        {} : {}
                        {} : {}""".format(
                    list(self.bounds.keys())[0],
                    list(list(self.bounds.values())[0].exterior.coords),
                    list(self.bounds.keys())[1],
                    list(list(self.bounds.values())[1].exterior.coords),
                )
            )

    def image_filepaths(self) -> list:
        """Return filepaths to desired image bands"""
        return [
            glob.glob(os.path.join(self.path, "your_band_pattern"))[0]
            for i in self.selected_product_bands
        ]

    def read_image(self) -> None:
        """
        Read in image data

        Add image band data to bands present in the initialised xr.Dataset,
        subsetting in accordance with the subsetting parameters provided in subset_info.
        Resulting xr.Dataset has converted input coordinates from initial
        coordinate reference system to the World Geodetic System 1984 (WGS 84)
        """
        bands = self.selected_product_bands
        img_list = self.image_filepaths()
        raise NotImplementedError

    def read_meta(self) -> None:
        """
        Read metadata in and assign to dataset attributes
        """
        raise NotImplementedError

    def read_masks(self) -> None:
        """
        Read in mask data and add values as flags to the xr.Dataset
        """
        raise NotImplementedError

    def read_aux(self) -> None:
        """
        Read in auxiliary data and add to xr.Dataset
        """
        raise NotImplementedError

    def open_dataset(self) -> xr.Dataset:
        """
        Open selected data and metadata
        :return: xr.Dataset of desired subset
        """

        # check and set subsetting inputs
        self.masks = self.subset_info["masks"]
        self.meta_level = self.subset_info["metadataLevel"]
        self.roi = self.subset_info["roi"], self.subset_info["roi_crs"]
        self.selected_product_bands = self.subset_info["bands"]

        # create dataset to populate
        if (
                self.subset_info["read_img"] or self.subset_info["metadataLevel"]
        ):  # if band DataArrays are required
            self.ds = xr.Dataset(
                dict(
                    zip(
                        self.selected_product_bands,
                        [None] * len(self.selected_product_bands),
                    )
                )
            )
        else:
            self.ds = xr.Dataset()

        if self.subset_info["read_img"]:
            self.read_image()
        if self.subset_info["metadataLevel"]:
            self.read_meta()
        if self.subset_info["masks"]:
            self.read_masks()
        if self.subset_info["aux_data"]:
            self.read_aux()

        return self.ds

    # ----------------------------------------------------------------------------------------------------------------------
    # Potentially useful functions that I haven't put in a utils file/BaseReader

    def mask_to_flag(
            self, mask_ds: xr.Dataset, flag_name: str, flag_coords: Tuple[str, str], flag_dict: Optional[dict] = None
    ) -> None:
        """
        Convert mask xr.Dataset variables to flags in the self.ds xr.Dataset.

        Flag names can be specified using flag_dict which is a dictionary mapping from the dataset variable names
        to the desired flag names. If not specified, defaults to naming the flag variables the same names as their
        variable names in the mask_ds xr.Dataset.

        Note
            This function includes a check as to whether the required dimensions for setting variables as flags
            exist in the output dataset (self.ds) - using input flag_coords provided.

            The function to add the required dimensions is likely sensor specific, further abstraction may be possible
            later depending on reader structure. This function is only called if neither the image data nor latitude and
            longitude grids have been read in and assigned to self.ds (xr.Dataset), as there are therefore no
            dimensions present in self.ds (xr.Dataset) with which to assign the flag_variables.

        Example flag_dict:
               flag_dict = {
                    "ANC_DEG": "ancillary_degraded",
                    "ANC_LOST": "ancillary_lost",
                    "CIRRUS": "cirrus",
                    "DETECTOR_FOOTPRINT": "detector_footprint",
                    "MSI_DEG": "msi_degraded",
                    "MSI_LOST": "msi_lost",
                    "OPAQUE": "opaque",
                }

        :param mask_ds: mask xr.Dataset containing the masks as xr.DataArray variables
                        to be added as flags to self.ds xr.Dataset
        :param flag_name: str to use to name the flag variable e.g. quality_flags_B01, snow_cloud_flags_60m, etc.
        :param flag_coords: tuple containing the (y, x) coordinate names for the flag variables
        :param flag_dict: optional dictionary mapping from the dataset variable names to the desired flag names
        :return: None
        """

        if any([flag_coords[0] not in self.ds.dims.mapping.keys(), flag_coords[1] not in self.ds.dims.mapping.keys()]):
            self.add_dimensions_to_ds(flag_coords)  # todo - sensor specific function

        # create flag_variables and populate
        if flag_dict:
            self.ds.flag[flag_name] = (
                list(flag_coords),
                {"flag_meanings": [flag_dict[i] for i in mask_ds]},
            )
        else:
            self.ds.flag[flag_name] = (
                list(flag_coords),
                {"flag_meanings": [i for i in mask_ds]},
            )

        for i, k in zip(mask_ds, self.ds.flag[flag_name].keys()):
            try:
                self.ds.flag[flag_name][k][:, :] = mask_ds[i].data
            except IndexError:
                self.ds.flag[flag_name][k][:, :] = mask_ds[i].data[0]

    def add_dimensions_to_ds(self, flag_coords) -> None:
        """
        Add x,y dimensions from flag_coords and corresponding lon, lat to the self.ds xr.Dataset

        Note: may be done by reading in (and clipping if necessary) the longitude and latitude grids
        if these can be read in separately to the image data. Renaming of the dimensions might also be necessary
        if there are multiple spatial resolutions involved

        Example logic for Sentinel 2:
            The three different x, y dimensions: y_10, x_10; y_20, x_20; and y_60, x_60 need to be added.
            To be able to get all the desired coordinates, the dimensions must first be assigned to x and y,
            used to get lat and lon, before being renamed to the same as the flag_coords names given, enabling
            flag variables to be assigned using the desired dimensions.

        Dimensions can be renamed and longitude and latitude assigned using:
            self.ds = self.ds.rename(
                {"x": flag_coords[1], "y": flag_coords[0]}
            ).assign_coords(
                {
                    lon_name: (
                        list(flag_coords),
                        lon_new,
                    ),
                    lat_name: (
                        list(flag_coords),
                        lat_new,
                    ),
                }
            )
            where lon_name and lat_name are the desired names of the longitude and latitude coordinates

        :param flag_coords: tuple containing the (y, x) coordinate names for the flag variables
        """
        raise NotImplementedError
