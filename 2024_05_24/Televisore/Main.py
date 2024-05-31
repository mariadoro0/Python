from Televisore import Televisore
from inputDati import *


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
                stato = TV.Pulsante_Accensione()
                print("La TV è ora "+stato)
                input("Premere invio per continuare...")

            case 2:
                if TV.getAcceso():
                    canale = input_range("Che canale vuoi vedere?", int, 0, 99)
                    TV.Imposta_Canale(canale)
                    print("Stai guardando canale ",TV.getCanale())
                else:
                    print("La televisione è spenta.")
                input("Premere invio per continuare...")

            case 3:
                if TV.getAcceso():
                    TV.Canale_Successivo()
                    print("Ti trovi a canale: ",TV.getCanale())
                else:
                    print("La televisione è spenta.")
                input("Premere invio per continuare...")

            case 4:
                if TV.getAcceso():
                    TV.Canale_Precedente()
                    print("Ti trovi a canale: ", TV.getCanale())
                else:
                    print("La televisione è spenta.")
                input("Premere invio per continuare...")

            case 5:
                if TV.getAcceso():
                    msg, volume = TV.Aumenta_Volume()
                    print(msg)
                    TV.setVolume(volume)
                else:
                    print("La televisione è spenta.")
                input("Premere invio per continuare...")

            case 6:
                if TV.getAcceso():
                    msg, volume = TV.Abbassa_Volume()
                    print(msg)
                    TV.setVolume(volume)
                else:
                    print("La televisione è spenta.")
                input("Premere invio per continuare...")

            case 7:
                if TV.getAcceso():
                    stato = TV.Pulsante_Silenzioso()
                    print("Il silenzioso è stato "+stato)
                else:
                    print("La televisione è spenta.")
                input("Premere invio per continuare...")

            case 8:
                    print(TV.Print_Tv())
                    input("Premere invio per continuare...")
            case 0:
                break


main()
