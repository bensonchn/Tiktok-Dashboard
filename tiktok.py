# from TikTokApi import TikTokApi
# import json 
# import pandas as pd
# from helpers import process_results
# import sys

# def get_data(hashtag):
# #get cookie data
#     verifyFp = "verify_kwyfjb22_A4Aayd3T_5jHl_4Fdg_By4U_inZ17AWrq5pC"
#     # Setup instance
#     api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)
#     # Get data by hashtag
#     trending = api.by_hashtag(hashtag)
#     # print(trending)
#     flat_data  = process_results(trending)
#     # #export data to json
#     # with open('export.json', 'w') as f:
#     #     json.dump(trending, f)

#     df = pd.DataFrame.from_dict(flat_data, orient = 'index')
#     df.to_csv('tiktokdata.csv', index=False)


# if __name__ == '__main__':
#     # sys.argv will pass the tiktok.py
#     # sys.argv will pass the second thing in (which is what we are searching for)
#     # this sys enables you to run an argument in the commandline
#     get_data(sys.argv[1])

# -----------------------------------------------------------
# Importing the tiktok Python SDK
from TikTokApi import TikTokApi as tiktok
# Import JSON for export of data
import json
# Import data processing helper
from helpers import process_results 
# Import pandas to create dataframes
import pandas as pd
# Import sys dependency to extract command line arguments
import sys

def get_data(hashtag):
    # Get cookie data
    verifyFp = "verify_kx2ee558_BH6fvQVi_cXHF_4lfK_Bimg_hH0lYMCV6Vm6"
    # Setup instance
    api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)
    # Get data by hashtag
    trending = api.by_hashtag(hashtag)
    # Process data
    flattened_data = process_results(trending)
    # Convert the preprocessed data to a dataframe
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('tiktokdata.csv', index=False)

if __name__ == '__main__':
    get_data(sys.argv[1])