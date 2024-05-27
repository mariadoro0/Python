from Lampadina import Lampadina
from Televisore.inputDati import input_range, input_gen


def menu():
    while True:
        print("********MENU TV***********")
        print("** 1. Accendi/Spegni")
        print("** 2. Stampa stato della lampadina.")
        print("** 3. Crea nuova lampadina. ")
        print("** 0. EXIT")
        print("************************")
        scelta = input_range("Scelta: ", int, 0, 3)
        break
    return scelta



def main():
    lamp = Lampadina()
    lamp.setClickMax(input_gen("Inserire il valore massimo di click: ", int))

    while True:
        scelta=menu()
        match scelta:
            case 1:
                lamp.setStato(lamp.controllaClick())
                if lamp.getStato():
                    lamp.setAccesa(lamp.click())
                else:
                    print("La lampadina è rotta. Creane una nuova per continuare.")

            case 2:
                print(lamp)
                input("Premi invio per continuare...")

            case 3:
                lamp = Lampadina()
                lamp.setClickMax(input_gen("Inserire il valore massimo di click: ", int))

            case 0:
                break








main()