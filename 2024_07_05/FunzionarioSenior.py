from Personale import Personale


class FunzionarioSenior(Personale):
    costo = 100

    def __init__(self, codice, cognome, nome, annoAssunzione, oreLavorate):
        super().__init__(codice, cognome, nome, annoAssunzione)
        self.__oreLavorate = oreLavorate

    def getOreLavorate(self):
        return self.__oreLavorate

    def setOreLavorate(self, oreLavorate):
        self.__oreLavorate = oreLavorate

    def getCosto(self, anno=None):
        return self.costo * self.__oreLavorate

    def __str__(self):
        return super().__str__() + f"Ore lavorate: {self.__oreLavorate}"
