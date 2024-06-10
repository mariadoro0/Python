import os

from ContoCorrente import ContoCorrente
from Persona import Persona
from inputDati import input_gen, input_maggioreuguale, input_maggiore


def menu():
    stmenu = ''' 
***********************************************
**                   BANCA                   **
***********************************************
**   1) Crea Conto per Persona
**   2) Prelievo dal Conto N.
**   3) Versamento al Conto N.
**   4) Bonifico.
**   5) Stampa elenco conti di una persona.
**   6) Stampa elenco conti in ordine di conti.
**   7) Stampa elenco conti in ordine di saldo.
**   8) Uscita.
**
***********************************************'''
    while True:
        print(stmenu)
        scelta = input("Scelta: ")
        if scelta.isdigit() and int(scelta) in range(1, 9):
            break
        else:
            print("Input errato.")
        input("Premi invio per continuare...")
        os.system("cls")
    return int(scelta)


def creaConto():
    saldo = input_maggioreuguale("Inserire il saldo: ", float, 0)
    return ContoCorrente(saldo)


def creaPersona():
    nome = input_gen("Inserire il nome: ", str)
    cognome = input_gen("Inserire il cognome: ", str)
    return Persona(nome, cognome)


def prelievoConto(banca, nconto):
    for c in banca:
        if c.getNumConto() == nconto:
            valore = input_maggiore("Inserire il valore del prelievo: ", float, 0)
            return c.prelievo(valore)


def versamentoConto(banca, nconto):
    for c in banca:
        if c.getNumConto() == nconto:
            valore = input_maggiore("Inserire il valore del versamento: ", float, 0)
            return c.versamento(valore)


def bonifico(banca, ncontoPrel, ncontoVers):
    valore = input_gen("Inserire il valore del bonifico: ", float)
    flag1 = False
    flag2 = False
    for c1 in banca:
        if c1.getNumConto() == ncontoPrel:
            cp = c1
            flag1 = True
            if flag1:
                for c2 in banca:
                    if c2.getNumConto() == ncontoVers:
                        cv = c2
                        flag2 = True
    if flag1 and flag2:
        checkp = cp.prelievo(valore)
        checkv = cv.versamento(valore)
        if (checkp == 0 and checkv == 0) or (checkp == 1 and checkv == 0):
            return 0
        elif checkp == -1:
            return -3
        elif checkv == -1:
            return -4
    elif not flag1:
        return -1
    elif not flag2:
        return -2


def trovaContiPersona(banca, nome):
    contiPersona = []
    for c in banca:
        for n in c.getProprietari():
            if str(n) == nome:
                contiPersona.append(c)
    return contiPersona


def stampaElenco(banca):
    for c in banca:
        print(c)


def main():
    banca = []
    while True:
        scelta = menu()
        match scelta:
            case 1:
                print("-----CREAZIONE DEL CONTO------")
                conto = creaConto()
                print("Conto creato con successo.")
                npers = input_maggiore("Quante persone sono associate a questo conto? ", int, 0)
                print("-----CREAZIONE DELLE PERSONE------")
                for i in range(npers):
                    print("----Persona ", i + 1, "------")
                    persona = creaPersona()
                    conto.setProprietari(persona)
                print("Le persone sono state correttamente create ed associate al conto " + str(conto.getNumConto()))
                banca.append(conto)
                input("\nPremere invio per continuare...")

            case 2:
                print("-------PRELIEVO-------")
                nconto = input_maggiore("Da quale conto si desidera prelevare?", int, 0)
                check = prelievoConto(banca, nconto)
                match check:
                    case -1:
                        print("Valore inserito non valido.")
                    case 1:
                        print("Il prelievo è superiore al saldo. Verranno applicati degli interessi del 2% annuo sulla "
                              "soglia sconfinante.")
                    case 0:
                        print("Prelievo effettuato correttamente.")
                input("\nPremere invio per continuare...")

            case 3:
                print("-----VERSAMENTO-----")
                nconto = input_maggiore("In quale conto si desidera versare?", int, 0)
                check = versamentoConto(banca, nconto)
                match check:
                    case -1:
                        print("Valore inserito non valido.")
                    case 0:
                        print("Versamento effettuato con successo.")
                input("\nPremere invio per continuare...")

            case 4:
                print("-----BONIFICO-----")
                ncontoPrel = input_maggiore("Inserire il conto dal quale si desidera prelevare: ", int, 0)
                ncontoVers = input_maggiore("Inserire il conto al quale si desidera versare: ", int, 0)
                if ncontoPrel == ncontoVers:
                    print("Impossibile eseguire l'operazione sullo stesso conto: inserire due conti diversi.")
                else:
                    check = bonifico(banca, ncontoPrel, ncontoVers)
                    match check:
                        case 0:
                            print(
                                "Bonifico da Conto " + str(ncontoPrel) + " al Conto " + str(ncontoVers) + " effettuato "
                                                                                                          "correttamente.")
                        case -1:
                            print("Il Conto inserito per il prelievo non esiste.")
                        case -2:
                            print("Il Conto inserito per il versamento non esiste.")
                        case -3:
                            print("Non è stato possibile effettuare il prelievo dal conto " + str(ncontoPrel))
                        case -4:
                            print("Non è stato possibile effettuare il versamento dal conto " + str(ncontoVers))
                input("\nPremere invio per continuare...")

            case 5:
                print("----STAMPA CONTI DI UNA PERSONA-----")
                n = input_gen("Inserire il nome: ", str)
                c = input_gen("Inserire il cognome: ", str)
                nome = n + " " + c
                contiPersona = trovaContiPersona(banca, nome)
                if len(contiPersona) == 0:
                    print("Non sono stati trovati conti associati a " + nome)
                else:
                    print("Sono stati trovati " + str(len(contiPersona)) + " conti per " + nome)
                    stampaElenco(contiPersona)
                input("\nPremere invio per continuare...")

            case 6:
                print("------STAMPA PER NUMERO CONTO-----")
                banca.sort(key=lambda x: x.getNumConto())
                stampaElenco(banca)
                input("\nPremere invio per continuare...")

            case 7:
                print("------STAMPA PER SALDO-----")
                banca.sort(key=lambda x: x.getSaldo())
                stampaElenco(banca)
                input("\nPremere invio per continuare...")

            case 8:
                break


main()
