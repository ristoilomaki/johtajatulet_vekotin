import pandas as pd
from osallistuja import Osallistuja
from pprint import pprint

def osallistujat_to_list(filename, sheetname):
    """takes the excel input file name and returns a list of Osallistuja objects"""
    osallistujat_df = pd.read_excel(filename, sheet_name=sheetname)
    osallistujat_list = []
    # print(osallistujat_df)
    # iterate through df and create a new Osallistuja object from each row

    for _, row in osallistujat_df.iterrows():
        osallistujat_list.append(Osallistuja(row['Nimi'], row['AP'], row['IP'], row['Sunnuntai'], row['Toivelista'], row['Teema'], row['Verstaslista'], row['Ikäkausi'], row['Sähköposti']))

    return osallistujat_list

""" file_osallistujat = "C:/Users/risto/OneDrive/Asiakirjat/Johtajatulet_vekotin/osallistujat_legit.xlsx"
sheet_osallistujat = "data"
l = osallistujat_to_list(file_osallistujat, sheet_osallistujat)
i = 1
pprint(vars(l[i])) """
    