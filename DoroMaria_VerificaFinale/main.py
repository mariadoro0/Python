from AutoVettura import AutoVettura
from Furgone import Furgone
from GestioneVeicoli import GestioneVeicoli
from inputDati import input_range, input_gen


def menu():
    strmenu="""
******************MENU VEICOLI********************
*   1) Inserisci veicolo
*   2) Cancella veicolo per targa
*   3) Cerca veicolo per targa
*   4) Stampa elenco dei veicoli in ordine crescente di targa
*   5) Stampa numero totale dei veicoli
*   6) Stampa costo totale dei veicoli
*   7) Fine  
**************************************************"""
    print(strmenu)
    scelta = input_range("Scelta: ", int, 1, 7)
    print("**************************************************")
    return scelta


def scegliVeicolo():
    tipo = input_range("Che veicolo si vuole aggiungere alla lista?"
                       "\n1) Autovettura"
                       "\n2) Furgone"
                       "\n Scelta: ", int, 1, 2)
    return tipo


def creaVeicolo(tipo):
    marca = input_gen("Inserire la marca: ",str)
    targa = input_gen("Inserire la targa: ",str)
    costo = input_gen("Inserire il costo: ",float)
    match tipo:
        case 1:
            posti = input_gen("Inserire il numero di posti: ", int)
            veicolo = AutoVettura(marca, targa, costo, posti)
        case 2:
            capacita = input_gen("Inserire il numero di capacita: ", int)
            veicolo = Furgone(marca, targa, costo, capacita)
    return veicolo





def main():
    veicoli = []
    veicoli = GestioneVeicoli(veicoli)

    veicoli.aggiungiVeicolo(AutoVettura("Suzuki","AB345LS",12000,5))
    veicoli.aggiungiVeicolo(Furgone("Fiat", "KS678GV", 32000,15))
    veicoli.aggiungiVeicolo(AutoVettura("Wolkswagen","AA614BX",39000,5))
    veicoli.aggiungiVeicolo(AutoVettura("Fiat", "CB123CD", 15000, 5))
    veicoli.aggiungiVeicolo(Furgone("Toyota", "EF456GH", 20000, 20))
    veicoli.aggiungiVeicolo(Furgone("BMW", "IJ789KL", 35000, 45))
    veicoli.aggiungiVeicolo(AutoVettura("Mercedes", "MN012OP", 40000, 5))
    veicoli.aggiungiVeicolo(AutoVettura("Audi", "QR345ST", 30000, 5))


    while True:
        scelta=menu()
        match scelta:
            case 1:
                tipo = scegliVeicolo()
                veicolo = creaVeicolo(tipo)
                veicoli.aggiungiVeicolo(veicolo)
                input("Veicolo inserito con successo!\nPremere invio per continuare...")
            case 2:
                if veicoli.totaleVeicoli() == 0:
                    input("Elenco vuoto: impossibile eseguire l'operazione.\nPremere invio per continuare...")
                else:
                    targa = input_gen("Inserire la targa del veicolo da eliminare: ",str)
                    check = veicoli.cancellaVeicolo(targa)
                    if check:
                        input("Veicolo eliminato con successo!\nPremere invio per continuare...")
                    else:
                        input("Il veicolo inserito non è stato trovato.\nPremere invio per continuare...")
            case 3:
                if veicoli.totaleVeicoli() == 0:
                    input("Elenco vuoto: impossibile eseguire l'operazione.\nPremere invio per continuare...")
                else:
                    targa = input_gen("Inserire la targa del veicolo da cercare: ", str)
                    check,index = veicoli.cercaVeicolo(targa)
                    if check:
                        print(f"Veicolo trovato in posizione {index}")
                        input("Premere invio per continuare...")
                    else:
                        print("Il veicolo non esiste all'interno dell'elenco.")
                        input("Premere invio per continuare...")
            case 4:
                if veicoli.totaleVeicoli() == 0:
                    input("Elenco vuoto: impossibile eseguire l'operazione.\nPremere invio per continuare...")
                else:
                    veicoli.ordinaVeicoli("targa")
                    print(veicoli.stampaVeicoli())
                    input("Premere invio per continuare...")
            case 5:
                print(f"Il numero totale di veicoli nell'elenco è: {veicoli.totaleVeicoli()}")

            case 6:
                if veicoli.totaleVeicoli() == 0:
                    input("Elenco vuoto: impossibile eseguire l'operazione.\nPremere invio per continuare...")
                else:
                    print(f"Il costo totale dei veicoli presenti nell'elenco è di {veicoli.costoTotale()} euro.")
                    input("Premere invio per continuare...")

            case 7:
                input("Uscita dal programma.\nPremere invio per continuare...")
                break


main()


