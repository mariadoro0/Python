class Persona:
    def __init__(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome

    def __str__(self):
        return self.__nome + " " + self.__cognome

    def getNome(self):
        return self.__nome

    def getCognome(self):
        return self.__cognome

    def setNome(self, nome):
        self.__nome = nome

    def setCognome(self, cognome):
        self.__cognome = cognome
