from Lampadina import Lampadina
from Televisore.inputDati import input_range, input_gen


def menu():
    while True:
        print("********MENU LAMPADINA***********")
        print("** 1. Accendi/Spegni")
        print("** 2. Stampa stato della lampadina.")
        print("** 3. Crea nuova lampadina. ")
        print("** 0. EXIT")
        print("************************")
        scelta = input_range("Scelta: ", int, 0, 3)
        break
    return scelta


def main():
    clickmax = input_gen("Inserire il valore massimo di click: ", int)
    lamp = Lampadina(clickmax)


    while True:
        scelta = menu()
        match scelta:
            case 1:
                lamp.controllaClick()
                if lamp.getStato():
                    lamp.click()
                    if lamp.getAccesa():
                        print("La lampadina è accesa.")
                    else:
                        print("La lampadina è spenta.")
                else:
                    print("La lampadina è rotta. Creane una nuova per continuare.")

            case 2:
                print(lamp)
                input("Premi invio per continuare...")

            case 3:
                clickmax = input_gen("Inserire il valore massimo di click: ", int)
                lamp = Lampadina(clickmax)

            case 0:
                break


main()
