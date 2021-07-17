import pandas as pd
from osallistuja import Osallistuja

def osallistujat_to_list(filename, sheetname):
    """takes the excel input file name and returns a list of Osallistuja objects"""
    osallistujat_df = pd.read_excel(filename, sheet_name=sheetname)
    osallistujat_list = []
    # print(osallistujat_df)
    # iterate through df and create a new Osallistuja object from each row

    for _, row in osallistujat_df.iterrows():
        osallistujat_list.append(Osallistuja(row['Osallistuja'], row['AP'], row['IP'], row['Sunnuntai'], row['Toivelista'], row['Toiveteema'], row['Vertaisverstas']))

    return osallistujat_list

# print(osallistujat_to_list("C:/Users/risto/OneDrive/Asiakirjat/Johtajatulet_vekotin/osallistujat_input.xlsx")[0].get_name())

    