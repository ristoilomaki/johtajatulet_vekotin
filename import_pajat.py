import pandas as pd
from paja import Paja
from pprint import pprint

def pajat_to_list(filename, sheetname):
    """Takes a filename as input and returns a list of Paja objects"""
    paja_df = pd.read_excel(filename, sheet_name=sheetname)
    # print(paja_df)
    global themes # globaali muuttuja teemat, käytetään muissakin fileissä
    themes = paja_df['Teema'].tolist()
    paja_list = []

    for _, row in paja_df.iterrows():
        paja_list.append(Paja(row['Työpaja'], row['Teema'], row['Ajankohta'], row['Osallistujat']))

    return paja_list

file_pajat = "C:/Users/risto/OneDrive/Asiakirjat/Johtajatulet_vekotin/työpajat_legit.xlsx"
sheet_pajat = "data"

l = pajat_to_list(file_pajat, sheet_pajat)
i = 8
pprint(vars(l[i]))
