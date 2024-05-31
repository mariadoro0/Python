from Treno import Treno
from inputDati import input_range, input_gen


def inserimento_dati(treno):
    treno.setVagoni(input_gen("Inserire il numero di vagoni: ", int))
    passpervagone = input_gen("Inserire il numero di persone massimo per vagone: ", int)
    treno.passeggeriTotali(passpervagone)



def menu():
    while True:
        print("********MENU TRENO***********")
        print("** 1. Creazione del Treno")
        print("** 2. Salgono persone")
        print("** 3. Scendono persone")
        print("** 4. Stampa.")
        print("** 0. Uscita.")
        print("*****************************")
        scelta = input_range("Scelta: ", int, 0, 4)
        break
    return scelta

def main():
    ins = False
    while True:
        scelta = menu()
        match scelta:
            case 1:
                treno = Treno()
                inserimento_dati(treno)
                input("Inserimento dati completato: premere invio per continuare...")
                ins = True

            case 2:
                if ins:
                    npersone = input_gen("Quante persone sono salite? ", int)
                    msg, npersone = treno.checkCapienzaMax(npersone)
                    print(msg)
                    treno.salgonoPersone(npersone)
                else:
                    print("Prima bisogna creare il treno.")
                input("Premere invio per continuare...")

            case 3:
                if ins:
                    npersone = input_gen("Quante persone sono scese? ", int)
                    msg,npersone = treno.checkCapienzaMin(npersone)
                    print(msg)
                    treno.scendonoPersone(npersone)
                else:
                    print("Prima bisogna creare il treno.")
                input("Premere invio per continuare...")

            case 4:
                print(treno)

            case 0:
                break


main()


