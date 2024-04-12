from funzioni_input_e_conversione import *


def main():
    while True:
        scelta = menu()
        nromani = [int_to_roman(i) for i in range(4000)]
        if scelta == 1:
            n = input_range("Inserisci il numero da convertire da arabo a romano: ", int, 1, 3999)
            romano = conversione_arabo_romano(n, nromani)
            print("Il numero ", n, "convertito in numero romano è: ", romano)
        elif scelta == 2:
            n = input_gen("Inserisci il numero da convertire da romano ad arabo: ", str)
            n.upper()
            if input_check(n, nromani):
                arabo = conversione_romano_arabo(n, nromani)
                print("Il numero ", n, "convertito in numero arabo è: ", arabo)
            else:
                print("Il valore inserito non è valido.")

        if scelta == 0:
            break


main()
