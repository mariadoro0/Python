class Televisore:
    def __init__(self):
        self.__acceso = False
        self.__volume = 0
        self.__canale = 0
        self.__silenzioso = False

    def getAcceso(self):
        return self.__acceso

    def getVolume(self):
        return self.__volume

    def getCanale(self):
        return self.__canale

    def getSilzioso(self):
        return self.__silenzioso

    def setAcceso(self, acceso):
        self.__acceso = acceso

    def setVolume(self, volume):
        self.__volume = volume

    def setSilzioso(self, silzioso):
        self.__silenzioso = silzioso

    def __str__(self):
        return "----STATO TV-------" + "\nAcceso: " + str(self.__acceso) + "\nVolume: " + str(
            self.__volume) + "\nCanale: " + str(self.__canale) + "\nSilenzioso: " + str(
            self.__silenzioso) + "\n---------------"

    def Pulsante_Accensione(self):
        if self.__acceso:
            self.__acceso = False
            return "spenta"
        else:
            self.__acceso = True
            return "accesa"

    def Imposta_Canale(self, canale:int):
        self.__canale = canale

    def Canale_Successivo(self):
        if self.__canale == 99:
            self.__canale = 0
        else:
            self.__canale +=1

    def Canale_Precedente(self):
        if self.__canale == 0:
            self.__canale = 99
        else:
            self.__canale -=1

    def Aumenta_Volume(self):
        if self.__volume == 10:
            return -1
        else:
            return self.__volume + 1

    def Abbassa_Volume(self):
        if self.__volume == 0:
            return -1
        else:
            return self.__volume - 1

    def Pulsante_Silenzioso(self):
        if self.__silenzioso:
            self.__silenzioso = False
        else:
            self.__silenzioso = True

    def Print_Tv(self):
        if self.__acceso:
            return self
        else:
            return "La tv è spenta"
