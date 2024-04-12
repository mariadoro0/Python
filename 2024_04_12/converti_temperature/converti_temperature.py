from funzioni_input import *
from funzioni_conversione import *


def main():
    while True:
        scelta = menu()
        if scelta == 1:
            temp = input_range("Inserisci la temperatura in Celsius da convertire: ", float, -999.99, 999.99)
            tk, tf = converti_Celsius(temp)
            print(temp, " gradi Celsius")
            print(tk, " gradi Kelvin")
            print(tf, " gradi Farenheit")
        elif scelta == 2:
            temp = input_range("Inserisci la temperatura in Farenheit da convertire ", float, -1830.99, 1830.99)
            tc, tk = converti_Farenheit(temp)
            print(temp, " gradi Farenheit")
            print(tc, " gradi Celsius")
            print(tk, " gradi Kelvin")
        elif scelta == 3:
            temp = input_range("Inserisci la temperatura in Kelvin da convertire ", float, -1272.99, 1272.99)
            tc, tf = converti_Kelvin(temp)
            print(temp, " gradi Kelvin")
            print(tc, " gradi Celsius")
            print(tf, " gradi Farenheit")
        if scelta == 0:
            break


main()
