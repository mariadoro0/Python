import datetime
import operator

from funzioni import *


def inserimento_articoli(scontrino):
    risp = 'A'
    while risp != 'N':
        nomeart = input_gen("Inserire il nome dell'articolo: ", str)
        prezzo = input_gen("Inserire il prezzo: ", float)
        qnt = input_gen("Inserire la quantità: ", float)
        tot = prezzo * qnt
        sconto = calcola_sconto(tot, qnt)
        diz = dict({"Articolo": nomeart, "Prezzo": prezzo, "Quantità": qnt, "Totale": tot, "Sconto": sconto})
        scontrino.append(diz)
        risp = input_str("Continuare? [S]ì o [N]o", str, 'S', 'N')


def calcola_sconto(tot, qnt):
    sconto = 0
    if tot > 50:
        sconto = tot / 10
        tot = tot - sconto
        if qnt > 5:
            sconto += (tot * 5) / 100
            tot = tot - sconto
    return sconto


def tot_articoli(scontrino):
    totart = 0
    for r in scontrino:
        totart += r["Quantità"]
    return totart


def tot_sconti(scontrino):
    somma = 0
    for i in range(len(scontrino)):
        somma += scontrino[i].get("Sconto")
    return somma


def totalescontrino(scontrino):
    somma = 0
    for i in range(len(scontrino)):
        somma += scontrino[i].get("Totale")
    return somma


def stampa_nosconto(scontrino):
    print("Scontrino:")
    print("Data: ", datetime.datetime)
    print("Articolo:       Prezzo:        Quantità:      Totale:")
    for r in scontrino:
        print(r["Articolo"], r["Prezzo"], r["Quantità"], r["Totale"], sep="             ")


def stampa_sconto(scontrino, totscontrino, totalesconti):
    print("Scontrino:")
    print("Data: ", datetime.datetime)
    print("Articolo:       Prezzo:        Quantità:      Totale:        Sconto:")
    for r in scontrino:
        print(r["Articolo"], r["Prezzo"], r["Quantità"], r["Totale"], r["Sconto"], sep="             ")
    print("     Totale scontrino: ", totscontrino, "      Totale sconto:", totalesconti)


def ordina(scontrino, ordine):
    for r in scontrino:
        r.sort(key=operator.itemgetter(ordine))


def menu(scontrino):
    scelta = -1
    ins = False
    while scelta != 7:
        print("---------------")
        print("         MENU'       ")
        print("Scegli una delle seguenti opzioni:")
        print("1. Inserimento articoli")
        print("2. Totale articoli venduti.")
        print("3. Totale degli sconti effettuati.")
        print("4. Stampa scontrino senza sconto.")
        print("5. Stampa scontrino con sconto.")
        print("6. Stampa scontrino con sconto ordinato.")
        print("7. Fine.")
        scelta = input_range("La tua scelta: ", int, 1, 7)
        match scelta:
            case 1:
                inserimento_articoli(scontrino)
                print("Inserimento dati effettuato.")
                ins = True
            case 2:
                if ins:
                    narticoli = tot_articoli(scontrino)
                    print("Sono stati inseriti ", narticoli, " articoli")
                else:
                    print("E' necessario prima inserire i dati.")
            case 3:
                if ins:
                    totalesconti = tot_sconti(scontrino)
                    print("Totale dello sconto: ", totalesconti)
                else:
                    print("E' necessario prima inserire i dati.")
            case 4:
                if ins:
                    totscontrino = totalescontrino(scontrino)
                    stampa_nosconto(scontrino)
                else:
                    print("E' necessario prima inserire i dati.")
            case 5:
                if ins:
                    totscontrino = totalescontrino(scontrino)
                    totalesconti = tot_sconti(scontrino)
                    stampa_sconto(scontrino, totscontrino, totalesconti)
                else:
                    print("E' necessario prima inserire i dati.")
            case 6:
                if ins:
                    ordina = 0
                    print("Ordinare per prezzo o quantità?")
                    print("1. Prezzo")
                    print("2. Quantità.")
                    ordina = input_range("Inserire la scelta: ", int, 1, 2)
                    if ordina == 1:
                        ordine="Prezzo"
                    if ordina == 2:
                        ordine="Quantità"
                    scontrino = ordina(scontrino, ordine)
                    scontrino = stampa_sconto(scontrino, ordine)
                        
                else:
                    print("E' necessario prima inserire i dati")
