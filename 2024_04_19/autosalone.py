from funzioni_autosalone import *
def menu(auto):
    scelta = -1
    while scelta != 0:
        print("-----------------------------------------------------------")
        print("         Seleziona una delle seguenti opzioni:   ")
        print()
        print("0. Uscita")
        print("1. Visualizzare il cognome degli acquirenti di auto di cilindrata superiore a 1500cc.")
        print("2. Visualizzare il numero totale di auto immatricolate in un anno specifico.")
        print("3. Ordina l'elenco in base all'anno di immatricolazione.")
        print("4. Stampa l'elenco delle auto ordinato per anno di immatricolazione.")
        print("5. Inserire altri dati.")
        print()
        scelta = input_range("Scegli: ", int, 0, 5)
        print("-----------------------------------------------------------")

        if scelta == 1:
            visualizza_cc(auto)
        elif scelta == 2:
            anno = input_range("Inserire l'anno di immatricolazione ", int, 1910, 2024)
            counter = auto_tot(auto, anno)
            print("Ci sono ", counter, " auto immatricolate nel ", anno)
        elif scelta == 3:
            ordina_anno(auto)
        elif scelta == 4:
            ordina_anno(auto)
            stampa_anno(auto)
        elif scelta == 5:
            inserimento_dati(auto)


def main():
    #auto = inserimento_dati()
    auto = [["BMW", 1500, 2010, "Maria", "Doro"], ["Audi", 2000, 2008, "Andrea", "Rossi"],
            ["Fiat", 1200, 2010, "Paola", "Bianchi"], ["Citroen", 1700, 2021, "Giulio", "Verdi"]]
    menu(auto)


main()
