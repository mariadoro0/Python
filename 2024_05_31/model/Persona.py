from model.ContoCorrente import ContoCorrente


class Persona:
    def __init__(self,nome,cognome):
        self.__nome = nome
        self.__cognome = cognome
        self.__conto = None

    def __str__(self):
        return "------Persona--------"+"\nNome: "+self.__nome+"\nCognome: "+self.__cognome

    def getNome(self):
        return self.__nome

    def getCognome(self):
        return self.__cognome

    def getConto(self):
        return self.__conto

    def setNome(self, nome):
        self.__nome = nome

    def setCognome(self, cognome):
        self.__cognome = cognome

    def setConto(self, conto:ContoCorrente):
        self.__conto = conto




