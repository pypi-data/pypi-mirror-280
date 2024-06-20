#from eoio.readers.s3_olci_l1 import OLCIL1Reader
#from eoio.readers.s3_slstr_l1 import SLSTRL1Reader
import rioxarray as rxr
import os
import xarray as xr
slstr_path = r"C:\Users\jf16\Downloads\S3B_SL_1_RBT____20230516T105322_20230516T105622_20230516T130011_0179_079_265_1980_PS2_O_NR_004\S3B_SL_1_RBT____20230516T105322_20230516T105622_20230516T130011_0179_079_265_1980_PS2_O_NR_004.SEN3"
unc_path = r"C:\Users\jf16\Downloads\S3B_OL_1_EFR____20230512T110005_20230512T110305_20230512T125754_0180_079_208_2160_PS2_O_NR_003\S3B_OL_1_EFR____20230512T110005_20230512T110305_20230512T125754_0180_079_208_2160_PS2_O_NR_003.SEN3"
# Region of interest coordinates: [
#     [xmin,ymax],
#     [xmax,ymax],
#     [xmax,ymin],
#     [xmin,ymin],
# ]

# test_roi = [[4.5,48.5],[9,48.5],[9,46],[4.5,46]]
unc_roi = [[-7,48],[-16,47],[-14,42],[-4,45]]
slstr_roi = [[-9,57],[0,56],[1.5,53],[-9,54]]
test_subset_dict = {
    "bands": [
        "Oa04",
    ],
    "read_img": True,
    "roi": unc_roi,
    "roi_crs": 4326,  # default value degrees (if values don't make sense try image crs)
    "metadataLevel": True,
    "masks": None, # ['bright','dubious'],
    "aux_data": 'observation_geometry' ,# ['geometry'],
}

#tester = OLCIL1Reader(path=unc_path,subset_info=test_subset_dict)
#tester = SLSTRL1Reader(path=slstr_path,subset_info=test_subset_dict)
test = rxr.open_rasterio(os.path.join(slstr_path,"flags_an.nc"))
#test = xr.open_dataset(os.path.join(slstr_path,"time_an.nc"))
#test = rxr.open_rasterio(os.path.join(unc_path,"qualityFlags.nc"))
print("HERE")