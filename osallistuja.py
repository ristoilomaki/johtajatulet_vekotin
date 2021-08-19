# import random
# from import_pajat import themes
import pandas as pd
class Osallistuja:
    def __init__(self, name, ap, ip, sunnuntai, wishlist, wishtheme, verstas, ikakausi, mail) -> None:
        self.__name = name
        
        if ap == "Tilattu": # guess the input will be alike
            self.__ap = True
        else:
            self.__ap = False

        
        if ip == "Tilattu":
            self.__ip = True
        else:
            self.__ip = False

        if sunnuntai == "Tilattu":
            self.__sunnuntai = True
        else:
            self.__sunnuntai = False

        self.__wishlist = []
        if pd.notna(wishlist):
            helplist = wishlist.split(";")
            for e in helplist:
                s = e.split(".")
                self.__wishlist.append(s[0].strip())
        
        # wishlistiin siis kymmenenen pajaa, joihin mieluusti osallistuisi
        # entä jos ei ole kymmentä pajaa valittuna? nyt listaan päätyy niin monta kuin on tarjolla
        # self.__wishlist = wishlist
        self.__wishtheme = []
        if pd.notna(wishtheme):
            helplist = wishtheme.split(";")
            for e in helplist:
                s = e.split(".")
                self.__wishtheme.append(s[0].strip())
        
        self.__verstas = []
        if pd.notna(verstas):
            helplist = verstas.split(";")
            for e in helplist:
                s = e.split(".")
                self.__verstas.append(s[0].strip())

        self.__ikakausi = ikakausi
        self.__mail = mail

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

    def get_ikakausi(self):
        return self.__ikakausi
    
    def get_mail(self):
        return self.__mail

    def assign_name(self, pajaname, aika):
        """ asettaa pajalle nimen halutuksi ajaksi """
        if aika == "Aamupäivä":
            self.__ap_paja = pajaname
        if aika == "Iltapäivä":
            self.__ip_paja = pajaname
        if aika == "sunnuntai":
            self.__sunnuntai_paja = pajaname
        self.__all_pajat.append(pajaname)
    
    def get_pajaname(self, aika):
        if aika == "Aamupäivä":
            return self.__ap_paja
        if aika == "Iltapäivä":
            return self.__ip_paja
        if aika == "sunnuntai":
            return self.__sunnuntai_paja
    
    def get_all_pajat(self):
        return self.__all_pajat

        
    

        
