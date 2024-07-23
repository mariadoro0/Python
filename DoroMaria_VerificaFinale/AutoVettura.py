from Veicolo import Veicolo


class AutoVettura(Veicolo):
    def __init__(self, marca, targa, costo, posti):
        super().__init__(marca, targa, costo)
        self.__posti = posti

    def getPosti(self):
        return self.__posti

    def setPosti(self, posti):
        self.__posti = posti

    def __str__(self):
        return "AUTOVETTURA\n"+super().__str__()+f"Posti: {self.__posti}\n"