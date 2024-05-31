class Treno:
    def __init__(self):
        self.__nvagoni = 0
        self.__passeggerimax = 0
        self.__passeggerinow = 0

    def __str__(self):
        return ("----TRENO----"+"\nNumero vagoni: "
                +str(self.__nvagoni)+"\nMax passeggeri: "+str(self.__passeggerimax) +
                "\nPasseggeri a bordo: "+str(self.__passeggerinow))+"\n----------------"

    def getVagoni(self):
        return self.__nvagoni

    def getPasseggeri(self):
        return self.__passeggerimax

    def getPasseggeriNow(self):
        return self.__passeggerinow

    def setVagoni(self, nvagoni):
        self.__nvagoni = nvagoni

    def setPasseggeri(self, passeggeri):
        self.__passeggerimax = passeggeri

    def setPasseggeriNow(self, passeggerinow):
        self.__passeggerinow = passeggerinow



    def passeggeriTotali(self, passvagone):
        self.setPasseggeri(passvagone*self.__nvagoni)

    def salgonoPersone(self, npersone):
        self.setPasseggeriNow(self.__passeggerinow + npersone)

    def scendonoPersone(self, npersone):
        self.setPasseggeriNow(self.__passeggerinow - npersone)

    def checkCapienzaMax(self, npersone):
        if self.__passeggerinow + npersone > self.__passeggerimax:
            personesalite = self.__passeggerimax-self.__passeggerinow
            personegiu = npersone - personesalite
            if personesalite > 0:
                msg = f"Sono riuscite a salire {personesalite} persone, ma altre {personegiu} persone sono rimaste giù per superata capienza."
                return msg, personesalite
            else:
                msg = "Nessuno è riuscito a salire. Siamo al completo!"
                personesalite=0
                return msg, personesalite
        else:
            msg = "Tutti sono riusciti a salire sul treno."
            return msg, npersone

    def checkCapienzaMin(self, npersone):
        if self.__passeggerinow - npersone < 0:
            personescese = self.__passeggerimax - self.__passeggerinow
            msg = f"Non ci sono così tante persone sul treno! Ma tutti e {self.__passeggerinow} i presenti sono scesi."
            return msg, self.__passeggerinow
        else:
            msg = f"I {npersone} passeggeri sono scesi."
            return msg, npersone








