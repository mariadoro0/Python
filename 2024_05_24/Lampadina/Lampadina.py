class Lampadina:
    def __init__(self, clickmax):
        self.__accesa = False
        self.__stato = True
        self.__contaclick = 0
        self.__clickmax = clickmax

    def getAccesa(self):
        return self.__accesa

    def getStato(self):
        return self.__stato

    def getContaClick(self):
        return self.__contaclick

    def getClickMax(self):
        return self.__clickmax



    def __str__(self):
        return "-----LAMPADINA-----\nAccesa: {0}\nFunzionante: {1}\nClick effettuati: {2}\nMax click: {3}\n------------".format(
            self.SioNo(self.__accesa), self.SioNo(self.__stato), str(self.__contaclick), str(self.__clickmax))

    def SioNo(self, parametro):
        if parametro:
            return "SI"
        else:
            return "NO"

    def click(self):
        self.__contaclick += 1
        if self.__accesa and self.__stato:              # se la lampadina è accesa e lo stato è buono, la spengo
            self.__accesa = False
        elif not self.__accesa and self.__stato:        # se la lampadina è spenta e lo stato è buono, la accendo
            self.__accesa = True
        elif not self.__stato:                          # se la lampadina è rotta, è sempre spenta
            self.__accesa = False

    def controllaClick(self):
        if self.__contaclick >= self.__clickmax:        #controllo i click effettuati per regolare lo stato
            self.__stato = False
        else:
            self.__stato = True
