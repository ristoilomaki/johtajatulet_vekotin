""" Tästä tulee tämän härvelin pääfile."""
from osallistuja import Osallistuja
from paja import Paja
import import_pajat
import import_osallistujat
import pandas as pd

file_osallistujat = "C:/Users/risto/OneDrive/Asiakirjat/Johtajatulet_vekotin/osallistujat_input.xlsx"
file_pajat = "C:/Users/risto/OneDrive/Asiakirjat/Johtajatulet_vekotin/työpajat_input_testi.xlsx"
sheet_osallistujat = "input"
sheet_pajat = "input"

# 1. tuodaan excel pd dataframeksi
osallistujat = import_osallistujat.osallistujat_to_list(file_osallistujat, sheet_osallistujat)

# 2. luodaan jokaisesta osallistujasta olio
# oliolla kentät nimi, toivelista, tieto kuhunkin työpajaan osallistumisesta, ajankohta hyvälle työlle
# se tapahtuu y.o. fktiossa


# 3. luodaan kustakin työpajasta olio
# kentät ajankohta, osallistujalista, osallistujamäärä
pajat = import_pajat.pajat_to_list(file_pajat, sheet_pajat)

# 4. ajetaan kaikki osallistujat työpaja-arvonnan läpi
# jos 10 toivetta valittu, valitaan niiden perusteella työpajat
# jos toiveita ei valittu, valitaan teeman perusteella työpajat
# pitää jutella erikoistilanteet (vajaa määrä valintoja, ei teemaa valittuna)

# osallistujat pitää jakaa niihin, keillä työpajatoivelista kunnossa ja niihin, jotka arvotaan teeman perusteella
byList = []
byTheme = []
for guy in osallistujat:
    if len(Osallistuja.get_wishlist(guy)) == 10: # tämä pitää muuttaa, kaikenmittaiset listat ok
        byList.append(guy)
    else:
        byTheme.append(guy)

""" print(byList[0].get_wishlist())
for paja in pajat:
    print(paja.get_participants_list()) """

def find_and_add(guy, aika, pajat):
    """ Etsii osallistujalle sopivan pajan haluttuna ajankohtana.
    Etsii pajan jossa vähiten osallistujia.
    Lisää osallistujan pajan osallistujalistalle, ja poistaa osallistujan toivelistalta ko. pajan. """
    least = None # paja with least participants
    least_index = None
    for i in range(len(pajat)):
        if Paja.get_time(pajat[i]) == aika and Paja.get_name(pajat[i]) in Osallistuja.get_wishlist(guy):
            # katsotaan vain halutun ajankohdan aikoja
            # ja sellaisia pajoja, joihin osallistuja haluaa
            if (least == None and Paja.is_room(pajat[i])) or (Paja.is_room(pajat[i]) and Paja.get_participants_n(pajat[i]) < Paja.get_participants_n(least)):
                least = pajat[i]
                least_index = i
    # nyt muuttujassa least on paja, johon osallistuja haluaa ja hänet voidaan lisätä
    if least_index is not None:
        Paja.add_participant(pajat[least_index], guy)
        Osallistuja.remove_added(guy, Paja.get_name(pajat[least_index]))
        Osallistuja.assign_name(guy, Paja.get_name(pajat[least_index]), aika)
    else:
        find_and_add_by_theme(guy, aika, pajat) # kaikki toivepajat täynnä, arvotaan teeman mukaan

def find_and_add_by_theme(guy, aika, pajat):
    """ Etsii osallistujalle sopivan pajan haluttuna ajankohtana.
    Etsii pajan jossa vähiten osallistujia.
    Lisää osallistujan pajan osallistujalistalle, ja poistaa osallistujan toivelistalta ko. pajan. """
    least = None # paja with least participants
    least_index = None
    for i in range(len(pajat)):
        if Paja.get_time(pajat[i]) == aika and Paja.get_theme(pajat[i]) == Osallistuja.get_wishtheme(guy) and Paja.get_name(pajat[i]) not in Osallistuja.get_all_pajat(guy):
            # katsotaan vain halutun ajankohdan aikoja
            # ja sellaisia pajoja, joihin osallistuja haluaa
            if (least == None and Paja.is_room(pajat[i])) or (Paja.is_room(pajat[i]) and Paja.get_participants_n(pajat[i]) < Paja.get_participants_n(least)):
                least = pajat[i]
                least_index = i
    # nyt muuttujassa least on paja, johon osallistuja haluaa ja hänet voidaan lisätä
    if least_index is not None:
        Paja.add_participant(pajat[least_index], guy)
        Osallistuja.assign_name(guy, Paja.get_name(pajat[least_index]), aika)
    # tähän else-case että guy arvotaan mihin tahansa pajaan minne mahtuu?
    

""" find_and_add(byList[0], "AP", pajat)
print(byList[0].get_wishlist())
for paja in pajat:
    print(paja.get_participants_list()) """

# käydään läpi byList eli ne, joilla on toivelista mintissä
for guy in byList:
    if Osallistuja.ap_isgoing(guy):
        find_and_add(guy, "AP", pajat)
    if Osallistuja.ip_isgoing(guy):
        find_and_add(guy, "IP", pajat)
    if Osallistuja.sunnuntai_isgoing(guy):
        find_and_add(guy, "sunnuntai", pajat)

# käydään läpi teeman perusteella sijoitettavat osallistujat

for guy in byTheme:
    if Osallistuja.ap_isgoing(guy):
        find_and_add_by_theme(guy, "AP", pajat)
    if Osallistuja.ip_isgoing(guy):
        find_and_add_by_theme(guy, "IP", pajat)
    if Osallistuja.sunnuntai_isgoing(guy):
        find_and_add_by_theme(guy, "sunnuntai", pajat)

# 5. osallistujat ja tulokset dataframeen ja ulos excelii

paja_results = pd.DataFrame()
for paja in pajat:
    column_name = Paja.get_name(paja) + ", " + Paja.get_time(paja)
    help_df = pd.DataFrame(Paja.get_participants_list(paja), columns = [column_name])
    paja_results = pd.concat([paja_results, help_df], axis=1)

paja_results.to_excel("pajat_results.xlsx", sheet_name="Pajat")

# yhdistetään osallistujat ja ulostetaan ne exceliin
all_participants = byList + byTheme

osallistuja_results = pd.DataFrame(columns= ['Nimi', 'AP', 'IP', 'sunnuntai'])
for guy in all_participants:
    new_row = {'Nimi': guy.get_name(), 'AP': guy.get_pajaname('AP'), 'IP': guy.get_pajaname('IP'), 'sunnuntai': guy.get_pajaname('sunnuntai')}
    osallistuja_results = osallistuja_results.append(new_row, ignore_index=True)

osallistuja_results.to_excel("osallistujat_results.xlsx", sheet_name="Osallistujat")