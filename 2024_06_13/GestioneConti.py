class GestioneConti:
    def __init__(self):
        self.__elenco = []

    def aggiungiConto(self, persone, conto):
        for p in persone:
            conto.setProprietario(p)
        self.__elenco.append(conto)
        return True

    def prelievo(self, numconto, valore):
        flag = False
        for c in self.__elenco:
            if c.getNumConto() == numconto:
                flag = True
                res = c.prelievo(valore)
                if res == 0:
                    return 0
                else:
                    return -1
        return -2

    def cercaConto(self, numconto):
        for c in self.__elenco:
            if c.getNumConto() == numconto:
                return c
        return None

    def versamento(self, numconto, valore):
        for c in self.__elenco:
            if c.getNumConto() == numconto:
                res = c.versamento(valore)
                if res == 0:
                    return 0
                else:
                    return -1
        return -2

    def bonifico(self, contoprel, contover, valore):
        flag1 = False
        flag2 = False
        for c1 in self.__elenco:
            if c1.getNumConto() == contoprel:
                cp = c1
                flag1 = True
                if flag1:
                    for c2 in self.__elenco:
                        if c2.getNumConto() == contover:
                            cv = c2
                            flag2 = True
        if flag1 and flag2:
            checkp = cp.prelievo(valore)
            checkv = cv.versamento(valore)
            if (checkp == 0 and checkv == 0) or (checkp == 1 and checkv == 0):
                return 0
            elif checkp == -1:
                return -3
            elif checkv == -1:
                return -4
        elif not flag1:
            return -1
        elif not flag2:
            return -2

        def stampaElencoProprietari(self, nome, cognome):
            conti_per_prop = []
            for c in self.__elenco:
                for p in c.getProprietari():
                    if p.getNome() == nome and p.getCognome() == cognome:
                        conti_per_prop.append(c)
            print(conti_per_prop)

        def stampaElencoConti(self):
            for c in self.__elenco:
                print(c)

        def ordinamentoConti(self, mode):
            if mode =="saldo":
                self.__elenco.sort(key=lambda x:x.getSaldo())
            if mode == ""
