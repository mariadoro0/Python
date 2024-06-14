from GestioneDipendenti import GestioneDipendenti
from funzioniMainDipendenti import *


def main():
    elenco = GestioneDipendenti()
    scelta = -1
    while True:
        scelta = menu()
        match scelta:
            case 1:
                quale = scelta_tipo()
                d = creazione_dipendente(quale)
                elenco.aggiungiDipendente(d)
                print("Dipendente creato ed aggiunto correttamente.")
                input("Premere invio per continuare...")
            case 2:
                controllo = checkLen(elenco)
                if controllo:
                    who = scegli_chi()
                    check = elenco.eliminaDipendente(who)
                    if check:
                        print("Dipendente eliminato con successo.")
                    else:
                        print("Dipendente non trovato nell'elenco.")
                else:
                    print("Non sono presenti dipendenti: l'elenco è vuoto.")
                input("Premere invio per continuare...")
            case 3:
                if checkLen(elenco):
                    who = scegli_chi()
                    check = elenco.cercaDipendente(who)
                    if check:
                        print("Il dipendente " + who + " è presente nella lista")
                    else:
                        print("Il dipendente " + who + " non è presente nella lista")
                else:
                    print("Non sono presenti dipendenti: l'elenco è vuoto.")
                input("Premere invio per continuare...")
            case 4:
                if not checkLen(elenco):
                    print("Non sono presenti dipendenti: l'elenco è vuoto.")
                else:
                    print(elenco.stampaDipendenti())
                input("Premere invio per continuare...")
            case 5:
                print("Numero di dipendenti presenti nell'elenco: ", len(elenco.getElenco()))
                input("Premere invio per continuare...")
            case 6:
                if checkLen(elenco):
                    check = elenco.cancellaTuttiDip()
                    if check:
                        print("Elenco dei dipendenti correttamente eliminato.")
                    else:
                        print("Problema nell'eliminazione dei dipendenti.")
                else:
                    print("L'elenco è gia vuoto.")
                input("Premere invio per continuare...")
            case 0:
                print("Uscita dal programma.")
                break


main()
