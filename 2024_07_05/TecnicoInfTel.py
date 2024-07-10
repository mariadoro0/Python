from Personale import Personale


class TecnicoInfTel(Personale):
    costo = 40
    def __init__(self, codice, cognome, nome, annoAssunzione, oreLavorate, interno):
        super().__init__(codice, cognome, nome, annoAssunzione)
        self.__oreLavorate = oreLavorate
        self.__interno = interno



    def getOreLavorate(self):
        return self.__oreLavorate
    def getInterno(self):
        return self.__interno

    def setOreLavorate(self, oreLavorate):
        self.__oreLavorate = oreLavorate
    def setInterno(self, interno):
        self.__interno = interno


    def getCosto(self, anno):
        if self.__interno:
           return  self.costo*self.__oreLavorate+(2024-anno)
        else:
            return self.costo*self.__oreLavorate

    def __str__(self):
        return super().__str__()+f"Ore lavorate: {self.__oreLavorate}\nInterno: {self.__interno}"