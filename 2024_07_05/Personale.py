from abc import ABC, abstractmethod


class Personale(ABC):
    def __init__(self, codice, cognome, nome, annoAssunzione):
        self.__codice = codice
        self.__cognome = cognome
        self.__nome = nome
        self.__annoAssunzione = annoAssunzione

    def __str__(self):
        return f"Codice: {self.__codice}\nCognome: {self.__cognome}\nNome: {self.__nome}\nAnno Assunzione: {self.__annoAssunzione}\n"

    def getCodice(self):
        return self.__codice

    def getCognome(self):
        return self.__cognome

    def getNome(self):
        return self.__nome

    def getAnnoAssunzione(self):
        return self.__annoAssunzione

    def setCodice(self, codice):
        self.__codice = codice

    def setCognome(self, cognome):
        self.__cognome = cognome

    def setNome(self, nome):
        self.__nome = nome

    def setAnnoAssunzione(self, annoAssunzione):
        self.__annoAssunzione = annoAssunzione

    @abstractmethod
    def getCosto(self, ore):
        pass
