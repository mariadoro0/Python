class Atleta:
    def __init__(self, nome: str, cognome: str, altezza: int):
        self.__nome = nome
        self.__cognome = cognome
        self.__altezza = altezza
        self.__squadra = ""
        self.__visitamedica = False

    def get_nome(self):
        return self.__nome

    def get_cognome(self):
        return self.__cognome

    def get_altezza(self):
        return self.__altezza

    def get_squadra(self):
        return self.__squadra

    def get_visitamedica(self):
        return self.__visitamedica

    def set_nome(self, nome):
        self.__nome = nome

    def set_cognome(self, cognome):
        self.__cognome = cognome

    def set_altezza(self, altezza):
        self.__altezza = altezza

    def set_squadra(self, squadra):
        self.__squadra = squadra

    def __set_visitamedica(self, visitamedica):
        self.__visitamedica = visitamedica

    def assegna_squadra(self, squadra):
        self.__squadra = squadra

    def effettua_visita(self, visitamedica):
        self.__set_visitamedica(visitamedica)


    def __str__(self):
        return "-----ATLETA-----\nNome: "+self.__nome+"\nCognome: "+self.__cognome+"\nAltezza: "+str(self.__altezza)+"cm\nSquadra: "+self.__squadra+"\nVisita medica: "+str(self.__visitamedica)
