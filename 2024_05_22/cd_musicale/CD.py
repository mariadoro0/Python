class CD:
    def __init__(self):             # titolo:str, autore:str, annouscita:int
        self.__titolo = ""
        self.__autore = ""
        self.__annouscita = None
        self.__prezzo = None

    def get_titolo(self):
        return self.__titolo

    def get_autore(self):
        return self.__autore

    def get_annouscita(self):
        return self.__annouscita

    def get_prezzo(self):
        return self.__prezzo

    def set_titolo(self, titolo):
        self.__titolo = titolo

    def set_autore(self, autore):
        self.__autore = autore

    def set_annouscita(self, annouscita):
        self.__annouscita = annouscita

    def __set_prezzo(self, prezzo):
        self.__prezzo = prezzo

    def modifica_prezzo(self, prezzo):
        self.__set_prezzo(prezzo)

    def __str__(self):
        return "--------DISCO--------\nTitolo: "+self.__titolo+"\nAutore: "+self.__autore+"\nAnno di uscita: "+str(self.__annouscita)+"\nPrezzo: "+str(self.__prezzo)+"\n--------------------"
