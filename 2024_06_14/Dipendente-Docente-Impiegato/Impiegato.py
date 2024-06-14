from Dipendente import Dipendente

class Impiegato(Dipendente):
    def __init__(self, nome, indirizzo, sesso,  ufficio):
        Dipendente.__init__(self,nome, indirizzo, sesso)
        self._ufficio = ufficio

    def get_ufficio(self):
        return self._ufficio
    def set_ufficio(self, ufficio):
        return self._ufficio

    def __str__(self):
        return super().__str__() + f', Ufficio: {self.get_ufficio()}'

