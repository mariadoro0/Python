

class ContoCorrente:
    numcont: int = 0

    def __init__(self, saldo=0):
        ContoCorrente.numcont += 1
        self.__saldo: float = saldo
        self.__numconto: int = ContoCorrente.numcont
        self.__movimenti = []
        self.__proprietario = None

    def __str__(self):
        st = "\nConto corrente N."+str(self.__numconto)+"\nSaldo: "+str(self.__saldo)+"\n"
        st+=" Movimenti:\n"
        for m in self.__movimenti:
            st+=m+"\n"
        return st

    def getSaldo(self):
        return self.__saldo

    def getNumConto(self):
        return self.__numconto

    def getMovimenti(self):
        return self.__movimenti

    def getProprietario(self):
        return self.__proprietario

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def setNumConto(self, numconto):
        self.__numconto = numconto

    def setMovimenti(self, movimenti):
        self.__movimenti = movimenti

    def setProprietario(self, proprietario):
        self.__proprietario = proprietario

    def versamento(self, valore):
        if valore < 0:
            return "Non puoi inserire un valore negativo."
        else:
            self.__saldo += valore
            self.__movimenti.append("VERSAMENTO: +" + str(valore))
            return "Versamento effettuato con successo."

    def prelievo(self, valore):
        if valore < 0:
            return "Impossibile eseguire il prelievo di un numero negativo. Operazione eliminata"
        else:
            if valore>self.__saldo:
                self.__saldo -= valore
                self.__movimenti.append("PRELIEVO: -" + str(valore))
                return ("Il prelievo è superiore al saldo. Verranno applicati degli interessi del 2% annuo sulla "
                           "soglia sconfinante.")
            else:
                self.__saldo -= valore
                self.__movimenti.append("PRELIEVO: -" + str(valore))
                return "Prelievo effettuato correttamente."




