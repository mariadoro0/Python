from Squadra import Squadra
from inputDati import *


def inserimento(squadra: Squadra):
    print("Inserimento dati per " + squadra.getNome())
    squadra.setPartiteVinte(input_gen("Inserire il numero di partite vinte: ", int))
    squadra.setPartitePerse(input_gen("Inserire il numero di partite perse: ", int))
    squadra.setPartitePareg(input_gen("Inserire il numero di partite pareggiate: ", int))
    squadra.setGoalFatti(input_gen("Inserire il numero di goal fatti: ", int))
    squadra.setGoalSub(input_gen("Inserire il numero di goal subiti: ", int))
    print("************************")


def confronta_punti(squadra1, squadra2):
    if squadra1.Punti() > squadra2.Punti():
        return squadra1
    elif squadra1.Punti() < squadra2.Punti():
        return squadra2
    else:
        return False


def confronta_gol_subiti(squadra1, squadra2):
    if squadra1.getGols() > squadra2.getGols():
        return squadra1
    elif squadra1.getGols() < squadra2.getGols():
        return squadra2
    else:
        return False


def confronta_gol_fatti(squadra1, squadra2):
    if squadra1.getGolf() > squadra2.getGolf():
        return squadra1
    elif squadra1.getGolf() < squadra2.getGolf():
        return squadra2
    else:
        return False

def stampa_squadre(squadra1,squadra2):
    print("------STAMPA SQUADRE-------")
    print(squadra1)
    print("--------------------------")
    print(squadra2)



def menu():
    while True:
        print("********MENU SQUADRA***********")
        print("** 1. Confronta punti")
        print("** 2. Confronta gol subiti.")
        print("** 3. Confronta gol fatti.")
        print("** 4. Aggiungi gol fatto.")
        print("** 5. Aggiungi gol subito.")
        print("** 6. Azzera punteggi-inizio nuovo anno.")
        print("** 7. Stampa squadre.")
        print("** 0. EXIT")
        print("************************")
        scelta = input_range("Scelta: ", int, 0, 7)
        break
    return scelta


def scegli_squadra():
    sceltasquadra = input_str("Di quale squadra modificare i dati? [J]uventus o [M]ilan.", str, 'J', 'M')
    if sceltasquadra == 'J':
        return "Juventus"
    else:
        return "Milan"


def main():
    print("-----------SQUADRE-----------")
    juventus = Squadra("Juventus")
    milan = Squadra("Milan")

    inserimento(juventus)
    inserimento(milan)
    input("Inserimento dati completato. Premere invio per continuare...")


    while True:
        scelta = menu()
        match scelta:
            case 1:
                confronto = confronta_punti(juventus, milan)
                if confronto != False:
                    print("La squadra con più punti è: "+confronto.getNome()+"\nPunti: "+str(confronto.Punti()))
                else:
                    print("Le due squadre hanno lo stesso punteggio.")
                input("Premere invio per continuare...")
            case 2:
                confronto = confronta_gol_subiti(juventus, milan)
                if confronto != False:
                    print("La squadra con più gol subiti è: "+confronto.getNome()+"\nGol subiti: "+str(confronto.getGols()))
                else:
                    print("Le due squadre hanno lo numero di gol subiti: "+juventus.getGols())
                input("Premere invio per continuare...")

            case 3:
                confronto = confronta_gol_fatti(juventus, milan)
                if confronto != False:
                    print("La squadra con più gol fatti è: " + confronto.getNome() + "\nGol fatti: " + str(confronto.getGolf()))
                else:
                    print("Le due squadre hanno lo stesso numero di gol fatti: "+juventus.getGolf())
                input("Premere invio per continuare...")

            case 4:
                sceltasquadra = scegli_squadra()
                if sceltasquadra == juventus.getNome():
                    juventus.goalFatto()
                else:
                    milan.goalFatto()
                input("Dati modificati. Premere invio per continuare...")

            case 5:
                sceltasquadra = scegli_squadra()
                if sceltasquadra == juventus.getNome():
                    juventus.goalSubito()
                else:
                    milan.goalSubito()
                input("Dati modificati. Premere invio per continuare...")

            case 6:
                juventus.inizioAnno()
                milan.inizioAnno()
                input("Dati resettati. Premere invio per continuare...")

            case 7:
                stampa_squadre(juventus,milan)
                input("Premere invio per continuare...")
            case 0:
                break


main()
