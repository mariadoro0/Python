class Squadra:
    def __init__(self, nome):
        self.__nome = nome
        self.__pvinte = 0
        self.__pperse = 0
        self.__ppar = 0
        self.__golf = 0
        self.__gols = 0

    def getNome(self):
        return self.__nome

    def getPartiteVinte(self):
        return self.__pvinte

    def getPartitePerse(self):
        return self.__pperse

    def getPpar(self):
        return self.__ppar

    def getGolf(self):
        return self.__golf

    def getGols(self):
        return self.__gols

    def setNome(self, nome):
        self.__nome = nome

    def setPartiteVinte(self, pvinte):
        self.__pvinte = pvinte

    def setPartitePerse(self, pperse):
        self.__pperse = pperse

    def setPartitePareg(self, ppar):
        self.__ppar = ppar

    def setGoalFatti(self, golf):
        self.__golf = golf

    def setGoalSub(self, gols):
        self.__gols = gols

    def __str__(self):
        return (f"Nome Squadra: {self.__nome}\n" +
                f"Partite vinte: {self.__pvinte}\n" +
                f"Partite perse: {self.__pperse}\n" +
                f"Partite pareggiate: {self.__ppar}\n" +
                f"Gol fatti: {self.__golf}\n" +
                f"Gol subiti: {self.__gols}")

    def Punti(self):
        return self.__pvinte * 3 + self.__ppar

    def inizioAnno(self):
        self.setPartiteVinte(0)
        self.setPartitePerse(0)
        self.setPartitePareg(0)
        self.setGoalFatti(0)
        self.setGoalSub(0)

    def goalFatto(self):
        self.setGoalFatti(self.__golf + 1)

    def goalSubito(self):
        self.setGoalSub(self.__gols + 1)
