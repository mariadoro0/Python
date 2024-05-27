from Televisore import Televisore
from Televisore.inputDati import *


def menu():
    while True:
        print("********MENU TV***********")
        print("** 1. TV ON/OFF")
        print("** 2. Imposta canale.")
        print("** 3. Canale + ")
        print("** 4. Canale - ")
        print("** 5. Volume + ")
        print("** 6. Volume - ")
        print("** 7. Mute ON/OFF")
        print("** 8. Stampa TV")
        print("** 0. EXIT")
        print("************************")
        scelta = input_range("Scelta: ", int, 0, 8)
        break
    return scelta


def main():
    TV = Televisore()
    while True:
        scelta = menu()
        match scelta:
            case 1:
                acceso = TV.Pulsante_Accensione()
                TV.setAcceso(acceso)
            case 2:
                if TV.getAcceso():
                    canale = input_range("Che canale vuoi vedere?", int, 0, 99)
                    TV.Imposta_Canale(canale)
                else:
                    print("La televisione è spenta.")
            case 3:
                if TV.getAcceso():
                    canale = TV.Canale_Successivo()
                    TV.setCanale(canale)
                else:
                    print("La televisione è spenta.")
            case 4:
                if TV.getAcceso():
                    canale = TV.Canale_Precedente()
                    TV.setCanale(canale)
                else:
                    print("La televisione è spenta.")
            case 5:
                if TV.getAcceso():
                    volume = TV.Aumenta_Volume()
                    if volume == -1:
                        print("Il volume è già al massimo.")
                    else:
                        TV.setVolume(volume)
                else:
                    print("La televisione è spenta.")
            case 6:
                if TV.getAcceso():
                    volume = TV.Abbassa_Volume()
                    if volume == -1:
                        print("Il volume è già al minimo.")
                    else:
                        TV.setVolume(volume)
                else:
                    print("La televisione è spenta.")
            case 7:
                if TV.getAcceso():
                    sil = TV.Pulsante_Silenzioso()
                    TV.setSilzioso(sil)
                else:
                    print("La televisione è spenta.")
            case 8:
                if TV.getAcceso():
                    TV.Print_Tv()
                    input("Premere invio per continuare...")
                else:
                    print("La televisione è spenta.")
            case 0:
                break


main()
