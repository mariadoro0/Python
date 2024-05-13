# elenco di record nomi di persone con dizionario
from funzioni import *


def aggiunta_diz():
    diz = dict({"nome": "valore", "cognome": "valore", "sesso": "valore", "data di nascita": "valore"})
    nome = input_gen("Nome: ", str)
    diz.update({"nome": nome})
    cognome = input_gen("Cognome: ", str)
    diz.update({"cognome": cognome})
    sesso = input_str("Sesso: ", str, 'M', 'F')
    diz.update({"sesso": sesso})
    datan = input_data("Data di nascita (gg/mm/yyyy): ")
    datan=(str(datan)[:10])
    diz.update({"data di nascita": datan})
    print(diz)
    return diz


def stampa_lista(lista):
    for w in lista:
        print(w)


def ordinaelencoper(elenco, ordine):
    import operator
    elenco.sort(key=operator.itemgetter(ordine))

def menu_ordina():
    while True:
        print("-----------------")
        print("Come vuoi ordinare il dizionario?")
        print("0. Esci")
        print("1. Nome")
        print("2. Cognome")
        print("3. Sesso")
        print("4. Data di nascita")
        print("-----------------")
        scelta=input_range("Scelta: ",int,1,4)
        match scelta:
            case 1:
                ordine="nome"
            case 2:
                ordine="cognome"
            case 3:
                ordine="sesso"
            case 4:
                ordine="data di nascita"
            case 0:
                break
        return ordine



def main():
    lista = []
    f = True
    while f:
        diz = dict()
        diz = aggiunta_diz()
        lista.append(diz)
        risp = input_str("Continuare? Y o N ", str, 'Y', 'N')
        if risp == 'N':
            f = False
    stampa_lista(lista)
    ordine=menu_ordina()
    ordinaelencoper(lista,ordine)
    stampa_lista(lista)


main()
