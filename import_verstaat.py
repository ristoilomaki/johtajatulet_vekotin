import pandas as pd
from verstas import Verstas
from pprint import pprint

def verstaat_to_list(filename, sheetname):
    """Takes a filename as input and returns a list of Paja objects"""
    paja_df = pd.read_excel(filename, sheet_name=sheetname)
    # print(paja_df)
    paja_list = []

    for _, row in paja_df.iterrows():
        paja_list.append(Verstas(row['Nimi'], row['Volyymi']))

    return paja_list

file_verstaat="C:/Users/risto/OneDrive/Asiakirjat/Johtajatulet_vekotin/verstaat_legit.xlsx"
sheet_verstaat="data"

""" l = verstaat_to_list(file_verstaat, sheet_verstaat)
i = 1
pprint(vars(l[i])) """