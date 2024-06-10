class ContoCorrente:
    numcont: int = 0

    def __init__(self, saldo=0):
        ContoCorrente.numcont += 1
        self.__saldo: float = saldo
        self.__numconto: int = ContoCorrente.numcont
        self.__movimenti = []
        self.__proprietari = []

    def __str__(self):
        st = "\nConto corrente N." + str(self.__numconto) + "\nSaldo: " + str(self.__saldo) + "\n"
        st+= "Proprietari:\n"
        for p in self.__proprietari:
            st+= " - "+str(p)+"\n"
        st += " Movimenti:\n"
        for m in self.__movimenti:
            st += m + "\n"
        return st

    def getSaldo(self):
        return self.__saldo

    def getNumConto(self):
        return self.__numconto

    def getNumConti(self):
        return self.numcont


    def getMovimenti(self):
        return self.__movimenti

    def getProprietari(self):
        return self.__proprietari

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def setNumConto(self, numconto):
        self.__numconto = numconto

    def setMovimenti(self, movimenti):
        self.__movimenti = movimenti

    def setProprietari(self, proprietario):
        self.__proprietari.append(proprietario)

    def versamento(self, valore:float):
        if valore < 0:
            return -1
        else:
            self.__saldo += valore
            self.__movimenti.append("VERSAMENTO: +" + str(valore))
            return 0

    def prelievo(self, valore):
        if valore < 0:
            return -1
        else:
            if valore > self.__saldo:
                self.__saldo -= valore
                self.__movimenti.append("PRELIEVO: -" + str(valore))
                return 1
            else:
                self.__saldo -= valore
                self.__movimenti.append("PRELIEVO: -" + str(valore))
                return 0
