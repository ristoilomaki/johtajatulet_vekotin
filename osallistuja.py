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

        if wishlist is not None:
            self.__wishlist = ""
        else:
            self.__wishlist = wishlist.split(", ")

        # entä jos ei ole kymmentä teemaa valittuna? nyt listaan päätyy niin monta kuin on tarjolla
        # self.__wishlist = wishlist
        self.__wishtheme = wishtheme
        self.__verstas = verstas # no idea actually what this is (16.7.)

    def get_name(self):
        return self.__name
        
