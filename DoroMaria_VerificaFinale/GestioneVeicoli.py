import operator
import string
from tokenize import String


class GestioneVeicoli:
    def __init__(self, veicoli: list):
        self.__veicoli = veicoli

    def __str__(self):
        return self.stampaVeicoli()

    def aggiungiVeicolo(self, veicolo):
        self.__veicoli.append(veicolo)

    def cercaVeicolo(self, targa):
        flag = False
        index = -1
        for v in self.__veicoli:
            if v.getTarga() == targa:
                flag = True
                index = self.__veicoli.index(v)
                break
        return flag, index

    def cancellaVeicolo(self, targa):
        eliminato = False
        flag, index = self.cercaVeicolo(targa)
        if flag:
            self.__veicoli.pop(index)
            eliminato = True
        return eliminato

    def totaleVeicoli(self):
        return len(self.__veicoli)

    def stampaVeicoli(self):
        str = ""
        for v in self.__veicoli:
            str += v.__str__() + "\n"
        return str

    def costoTotale(self):
        tot = 0
        for v in self.__veicoli:
            tot += v.getCosto()
        return tot

    def ordinaVeicoli(self, chiave):
        chiave = "get" + chiave.capitalize()
        self.__veicoli.sort(key=operator.methodcaller(chiave))
