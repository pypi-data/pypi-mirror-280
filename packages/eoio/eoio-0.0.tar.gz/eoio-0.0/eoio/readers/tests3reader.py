path = r"C:\Users\jf16\OneDrive - National Physical Laboratory\Desktop\eoio_olci_data\S3B_OL_1_EFR____20220602T093742_20220602T094042_20220602T211101_0180_066_307_2160_PS2_O_NT_002.SEN3"
unc_path = r"C:\Users\jf16\Downloads\S3B_OL_1_EFR____20230512T110005_20230512T110305_20230512T125754_0180_079_208_2160_PS2_O_NR_003\S3B_OL_1_EFR____20230512T110005_20230512T110305_20230512T125754_0180_079_208_2160_PS2_O_NR_003.SEN3"
from eoio.readers.s3_olci_l1 import OLCIL1Reader
#from eoio.readers.landsat89 import Landsat89Reader
from eoio.readers.s3_slstr_l1 import SLSTRL1Reader

slstr_path = r"C:\Users\jf16\Downloads\S3B_SL_1_RBT____20230516T105322_20230516T105622_20230516T130011_0179_079_265_1980_PS2_O_NR_004\S3B_SL_1_RBT____20230516T105322_20230516T105622_20230516T130011_0179_079_265_1980_PS2_O_NR_004.SEN3"
landsat_path = r"C:\Users\jf16\Downloads\LC08_L1GT_155111_20230201_20230208_02_T2"
# Region of interest coordinates: [
#     [xmin,ymax],
#     [xmax,ymax],
#     [xmax,ymin],
#     [xmin,ymin],
# ]

# # test_roi = [[4.5,48.5],[9,48.5],[9,46],[4.5,46]]
# unc_roi = [[-7,48],[-16,47],[-14,42],[-4,45]]
slstr_roi = [[-1,57],[0,57],[0,56],[-1,56]]
test_subset_dict = {
    "bands": [
        "S1_radiance_an",
        "S4_radiance_bn"
    ],
    "read_img": True,
    "roi": slstr_roi,
    "roi_crs": 4326,  # default value degrees (if values don't make sense try image crs)
    "metadataLevel": None,
    "masks": None, #['cloud','exception',],
    "aux_data": ["geometry"]# 'observation_geometry' , ['geometry'],
}

# tester = OLCIL1Reader(path=unc_path,subset_info=test_subset_dict)
tester = SLSTRL1Reader(path=slstr_path,subset_info=test_subset_dict)
# #tester = Landsat89Reader(path=landsat_path,subset_info=test_subset_dict)
test = tester.open_dataset()
print("HERE")

