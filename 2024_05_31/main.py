from model.ContoCorrente import ContoCorrente
from model.Persona import Persona
from inputDati import input_range, input_gen, input_maggiore, input_maggioreuguale
import os
from sys import path


def menu():
    stmenu = ''' 
***********************************************
**                   BANCA                   **
***********************************************
**   1) Crea Persona
**   2) Crea Conto Corrente
**   3) Associa persona e conto corrente
**   4) Prelievo
**   5) Versamento
**   6) Bonifico
**   7) Stampa elenco conti associati in ordine crescente di conto.
**   8) Stampa elenco conti associati in ordine crescente di saldo.
**   9) Uscita.
**
***********************************************'''
    while True:
        print(stmenu)
        scelta = input("Scelta: ")
        if scelta.isdigit() and int(scelta) in range(1, 10):
            break
        else:
            print("Input errato.")
        input("Premi invio per continuare...")
        os.system("cls")
    return int(scelta)


def creaOggettoPersona():
    nome = input_gen("Inserire il nome: ", str)
    cognome = input_gen("Inserire il cognome: ", str)
    p = Persona(nome, cognome)
    return p


def creaOggettoConto():
    saldo = input_maggioreuguale("Inserire il saldo: ", float, 0)
    c = ContoCorrente(saldo)
    return c


def associaConto(persona, conto, banca):
    persona.setConto(conto)
    conto.setProprietario(persona)
    banca.append(conto)


def stampaBanca(banca):
    for c in banca:
        print(c.getProprietario(), c)


def prelievo(banca, nconto, valore):
    for c in banca:
        if c.getNumConto() == nconto:
            res = c.prelievo(valore)
    return res


def versamento(banca, nconto, valore):
    for c in banca:
        if c.getNumConto() == nconto:
            res = c.versamento(valore)
    return res

def bonifico(contoprel,contovers,banca, valore):
    trovato1 = False
    trovato2 = False
    for c in banca:
        if c.getNumConto() == contoprel:
            trovato1 = True
            conto1=c
        if trovato1:
            for c in banca:
                if c.getNumConto() == contovers:
                    trovato2=True
                    conto2=c
                    conto1.prelievo(valore)
                    conto2.versamento(valore)
    if not trovato1:
        s = "Conto del prelievo non trovato"
    elif not trovato2:
        s = "Conto del versamento non trovato"
    else:
        s="Bonifico effettuato"
    return s





def main():
    banca = []
    loop = True
    while loop:
        scelta = menu()
        match scelta:
            case 1:
                persona = creaOggettoPersona()
                print("Oggetto 'Persona' creato.\n", persona)

            case 2:
                conto = creaOggettoConto()
                print("Oggetto 'Conto Corrente' creato.\n", conto)

            case 3:
                if persona == None:
                    print("Oggetto 'Persona' non esiste.")
                elif conto == None:
                    print("Oggetto 'Conto Corrente' non esiste. ")
                else:
                    if conto not in banca:
                        associaConto(persona, conto, banca)
                        print("Associazione completata.")
                    else:
                        print("Il conto è già stato associato.")

            case 4:
                if len(banca) > 0:
                    nconto = input_range("Inserisci il numero del conto da cui prelevare: ", int, 1, len(banca))
                    valore = input_gen("Inserire la cifra da prelevare: ", float)
                    done = prelievo(banca, nconto, valore)
                    print(done)
                else:
                    print("Non ci sono conti registrati.")

            case 5:
                if len(banca) > 0:
                    nconto = input_range("Inserisci il numero del conto in cui versare: ", int, 1, len(banca))
                    valore = input_gen("Inserire la cifra da versare: ", float)
                    done = versamento(banca, nconto, valore)
                    print(done)
                else:
                    print("Non ci sono conti registrati.")

            case 6:
                if len(banca) > 1:
                    contoprel = input_range("Inserisci il numero del conto da cui prelevare: ", int, 1, len(banca))
                    contovers = input_range("Inserisci il numero del conto in cui versare: ", int, 1, len(banca))
                    valore = input_gen("Inserire la cifra del bonifico: ", float)
                    s = bonifico(contoprel,contovers,banca,valore)
                    print(s)
                elif len(banca) == 1:
                    print("C'è solo un conto registrato.")
                else:
                    print("Non ci sono conti registrati.")

            case 7:
                banca.sort(key=lambda x: x.getNumConto())
                stampaBanca(banca)
            case 8:
                banca.sort(key=lambda x: x.getSaldo())
                stampaBanca(banca)
            case 9:
                loop = False
        input("Premi invio per continuare....")
        os.system("cls")


main()
