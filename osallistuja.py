# import random
# from import_pajat import themes
import pandas as pd
class Osallistuja:
    def __init__(self, name, ap, ip, sunnuntai, wishlist, wishtheme, verstas) -> None:
        self.__name = name
        
        if ap == "kyllä": # guess the input will be alike
            self.__ap = True
        else:
            self.__ap = False

        
        if ip == "kyllä":
            self.__ip = True
        else:
            self.__ip = False

        if sunnuntai == "kyllä":
            self.__sunnuntai = True
        else:
            self.__sunnuntai = False

        if pd.isnull(wishlist):
            self.__wishlist = []
        else:
            self.__wishlist = wishlist.split(", ")
        
        # wishlistiin siis kymmenenen pajaa, joihin mieluusti osallistuisi
        # entä jos ei ole kymmentä pajaa valittuna? nyt listaan päätyy niin monta kuin on tarjolla
        # self.__wishlist = wishlist
        if pd.isnull(wishtheme): # voi olla monta teemaa -> lista
            self.__wishtheme = []
        else:
            self.__wishtheme = wishtheme.split(", ")
        self.__verstas = verstas # no idea actually what this is (16.7.)
        self.__ap_paja = None
        self.__ip_paja = None
        self.__sunnuntai_paja = None
        self.__all_pajat = []

    def get_name(self):
        return self.__name
    def get_wishlist(self):
        return self.__wishlist
    def ap_isgoing(self):
        return self.__ap
    def ip_isgoing(self):
        return self.__ip
    def sunnuntai_isgoing(self):
        return self.__sunnuntai
    def get_wishtheme(self):
        return self.__wishtheme
    def get_verstas(self):
        return self.__verstas
    def remove_added(self, pajaname):
        """ poistaa pajan nimen toivelistasta """
        self.__wishlist.remove(pajaname)

    def assign_name(self, pajaname, aika):
        """ asettaa pajalle nimen halutuksi ajaksi """
        if aika == "AP":
            self.__ap_paja = pajaname
        if aika == "IP":
            self.__ip_paja = pajaname
        if aika == "sunnuntai":
            self.__sunnuntai_paja = pajaname
        self.__all_pajat.append(pajaname)
    
    def get_pajaname(self, aika):
        if aika == "AP":
            return self.__ap_paja
        if aika == "IP":
            return self.__ip_paja
        if aika == "sunnuntai":
            return self.__sunnuntai_paja
    
    def get_all_pajat(self):
        return self.__all_pajat

        
    

        
