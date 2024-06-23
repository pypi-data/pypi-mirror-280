# import pandas as pd
# import os
#
# from ..vertical_config_store import vertical_store
#
#
# def fill_collection():
#
#     # data
#     data_file_path = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir),
#                                   "data",
#                                   "Care_Intent_Industries.xlsx")
#     df = pd.read_excel(data_file_path)
#
#     # data preprocess
#     vertical_config_list = []
#     for index, row in df.iterrows():
#         vertical_config = {"partner": int(row['PARTNER_ID']),
#                            "vertical": row['Vertical'],
#                            "display_vertical": row['Display_Vertical'],
#                            "additional": {
#                                "industry": row['Industry']
#                             }
#                            }
#         vertical_config_list.append(vertical_config)
#
#     # fill collection
#     vertical_store.bulk_save(vertical_config_list)
#
#
# if __name__ == "__main__":
#     fill_collection()
