class Paja:
    def __init__(self, name, theme, time, max_participants) -> None:
        self.__name = name
        self.__theme = theme
        self.__aika = time
        self.__max_participants = max_participants
        self.__participants_list = []

    def get_name(self):
        return self.__name
    def get_theme(self):
        return self.__theme
    def get_time(self):
        return self.__aika
    def get_max_participants(self):
        return self.__max_participants
    def get_participants_n(self):
        return len(self.__participants_list)
    def get_participants_list(self):
        return self.__participants_list
    
    # metodi osallistujan lisäämiseksi
    # jos mahtuu, lisätään osallistuja ja palautetaan true
    # jos ei mahdu, ei tehdä mitään ja palautetaan false

    def add_participant(self, participant):
        if self.get_participants_n() < self.get_max_participants(): # mahtuu
            self.__participants_list.append(participant.get_name())
            return True
        else: # muussa tilanteessa ei mahdu
            return False

    def is_room(self):
        return self.get_participants_n() < self.get_max_participants()

    

    
