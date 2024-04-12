#dati n numeri in input in lire convertire in euro e stampare il totale
def main():
    a="s"
    somma=0
    while a=="s":
        num=float(input("Inserisci un valore in lire: "))
        euro=num/1936.27
        print("conversione di ", num," lire in euro= ", euro)
        somma=somma+euro
        a=input("Vuoi terminare? Se si inserisci un carattere, oppure 's' per continuare. ")

    print("La somma totale delle lire inserite convertite in euro è: ", somma)




main()