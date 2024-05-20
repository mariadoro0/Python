from funzioni import *


def main():
    n=input_maggiore("Inserisci numero intero: ", int, 0)
    print(n)
    n = input_range("Inserisci numero tra 2 e 10: ", int, 2,10)
    print(n)
    d = input_data("Inserisci data gg/mm/aaaa: ")
    print(d)


main()