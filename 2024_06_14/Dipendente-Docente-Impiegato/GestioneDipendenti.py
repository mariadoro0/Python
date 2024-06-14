from Dipendente import Dipendente

class GestioneDipendenti:
    def __init__(self):
        self.__elenco = []


    def getElenco(self):
        return self.__elenco


    def aggiungiDipendente(self, d : Dipendente):
        check = self.cercaDipendente(d)
        if not check:
            self.__elenco.append(d)
        return check

    def eliminaDipendente(self, nome):
        check = self.cercaDipendente(nome)
        if check:
            for d in self.__elenco:
                if d.get_nome() == nome:
                    self.__elenco.remove(d)
        return check

    def cercaDipendente(self, nome):
        check = False
        for record in self.__elenco:
            if record.get_nome() == nome:
                check = True
        return check

    def cancellaTuttiDip(self):
        self.__elenco.clear()
        if len(self.__elenco) == 0:
            return True
        else:
            return False

    def stampaDipendenti(self):
        return self.__str__()

    def __str__(self):
        str = ""
        for d in self.__elenco:
            str += d.__str__() +"\n"
        return str
