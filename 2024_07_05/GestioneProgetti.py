from Personale import Personale


class GestioneProgetti():
    def __init__(self):
        self.__elenco = []

    def aggiungiPersona(self, persona: Personale):
        self.__elenco.append(persona)

    def eliminaPersona(self, nome):
        for p in self.__elenco:
            if p.getNome() == nome:
                self.__elenco.remove(p)
                return True
        return False

    def cercaPersona(self, nome):
        for p in self.__elenco:
            if p.getNome() == nome:
                return True, p
        return False, None

    def elencoPersone(self):
        strelenco = ""
        for p in self.__elenco:
            strelenco+= str(p)+"\n"+"\n"
        return strelenco

    def getTotPersone(self):
        return len(self.__elenco)

    def costiProgetto(self, anno: int):
        sum = 0
        for p in self.__elenco:
            sum += p.getCosto(anno)
        return float(sum)
