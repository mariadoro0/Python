from funzioni_input import *


def menu():
    print("-------------------------")
    print("PROGRAMMA DI CONVERSIONE NUMERI ARABI E ROMANI")
    print("-------------------------")
    print("0. Uscita")
    print("1. Conversione da arabo a romano")
    print("2. Conversione da romano ad arabo")
    print("-------------------------")
    scelta = input_range("Scegli: ", int, 0, 2)
    print("------------------------")
    return scelta


def int_to_roman(num):
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom_symb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    numr = ""
    i = 0
    while num > 0:
        for x in range(num // value[i]):
            numr += rom_symb[i]
            num -= value[i]
        i += 1

    return numr


def conversione_arabo_romano(n, nromani):
    romano = ""
    romano += nromani[n]
    return romano


def input_check(n, nromani):
    global status
    while True:
        if n.isdigit():
            status = True
            break
        for i in range(4000):
            if nromani[i] == n:
                status = True
                break
            else:
                status = False
        break
    return status


def conversione_romano_arabo(r, nromani):
    arabo = 0
    if r.isdigit():
        arabo = r
    else:
        for i in range(4000):
            if nromani[i] == r:
                arabo = i
                break
    return arabo
