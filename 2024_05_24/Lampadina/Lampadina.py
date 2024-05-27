class Lampadina:
    def __init__(self):
        self.__accesa = False
        self.__stato = True
        self.__contaclick = 0
        self.__clickmax = 0

    def getAccesa(self):
        return self.__accesa

    def getStato(self):
        return self.__stato

    def getContaClick(self):
        return self.__contaclick

    def getClickMax(self):
        return self.__clickmax

    def setAccesa(self, accesa):
        self.__accesa = accesa

    def setStato(self, stato):
        self.__stato = stato

    def setContaClick(self, click):
        self.__contaclick = click

    def setClickMax(self, clickmax):
        self.__clickmax = clickmax

    def __str__(self):
        return "-----LAMPADINA-----\nAccesa: {0}\nFunzionante: {1}\nClick effettuati: {2}\nMax click: {3}\n------------".format(
            str(self.__accesa), str(self.__stato), str(self.__contaclick), str(self.__clickmax))

    def click(self):
        self.__contaclick += 1
        if self.__accesa:
            return False
        else:
            return True

    def controllaClick(self):
        if self.__contaclick >= self.__clickmax:
            return False
        else:
            return True


