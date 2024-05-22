from atleta.Atleta import Atleta
from atleta.funzioni import *
def main():
    nome=input_gen("Inserisci il nome: ", str)
    cognome=input_gen("Inserisci cognome: ",str)
    altezza=input_maggiore("Inserire l'altezza: ", int, 0)
    Ayoub = Atleta(nome,cognome,altezza)
    Ayoub.assegna_squadra("Milan")
    Ayoub.effettua_visita(True)
    print(Ayoub)


main()
