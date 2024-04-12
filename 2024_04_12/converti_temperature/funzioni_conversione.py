def converti_Celsius(temp):
    tk = temp + 273.15
    tf = (temp * 1.8) + 32
    return tk, tf


def converti_Kelvin(temp):
    tc = temp - 273.15
    tf = (9 / 5) * temp - 459.67
    return tc, tf


def converti_Farenheit(temp):
    tc = (temp - 32) / 1.8
    tk = (5 / 9) * temp + 255.37
    return tc, tk


def menu():
    print("-------------------------")
    print("PROGRAMMA DI CONVERSIONE TEMPERATURE")
    print("-------------------------")
    print("0. Uscita")
    print("1. Conversione da Celsius")
    print("2. Conversione da Farenheit")
    print("3. Conversione da Kelvin")
    print("-------------------------")
    print()
    scelta = int(input("Scegli: "))
    print("------------------------")
    return scelta
