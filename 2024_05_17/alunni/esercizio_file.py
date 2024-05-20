# scrivere un'applicazione in python che permetta di eseguire un menù per
# inserimento e lettura di nome, media, promosso, su file
import os
from os import strerror, system, path
#from sys import path
import sys
from funzInput import input_gen, input_range, input_str


def apriFile(msg, mod, enc):
    f = None
    file = input_gen(msg, str)
    try:
        if os.path.exists(file) and mod == 'w':
            sc = input_str("File già esistente. Vuoi sovrascriverlo? s/n: ", str, 's', 'n')
            if sc == 's':
                f = open(file, mod, encoding=enc)
            else:
                # apre in append
                f = open(file, "a", encoding=enc)

        else:
            f = open(file, mod, encoding=enc)
    except IOError as e:
        print(strerror(e.errno))

    return f


def inserimentoDati():
    alunni = ""
    while True:
        nome = input_gen("Inserire il nome dello studente: ", str)
        media = input_range("Inserire la media: ", float, 1, 10)
        if media >= 6:
            promosso = 'P'
        else:
            promosso = 'R'
        alunni += nome + ";" + str(media) + ";" + promosso + "\n"
        s = input_str("Vuoi terminare? s/n: ", str, 's', 'n')
        if s == "S" or s == "s":
            break
    return alunni


def scriviFile(f, dati):
    f.write(dati)





def menu():
    scelta = 0
    while True:
        system("cls")
        print("*********Menù********")
        print("\t 1) Inserire i dati e scrittura su file.")
        print("\t 2) Leggere i dati dal file e stamparli.")
        print("\t 3) Fine Programma.")
        scelta = input_range("Inserire la scelta:", int, 1, 3)
        break
    return scelta


def main():
    while True:
        system("cls")
        s = menu()
        match s:
            case 1:
                print("Inserimento dati.")
                f = apriFile("Inserisci il nome del file su cui scrivere.", "w", "utf-8")
                if f != None:
                    dati = inserimentoDati()
                    scriviFile(f, dati)
                    f.close()
                else:
                    print("Inserimento dati fallito.")
            case 2:
                f = apriFile("Inserisci il nome del da leggere.", "r", "utf-8")
                if f != None:
                    lines=f.readlines()
                    f.close()
                    print("Numero studenti: ", len(lines))
                    print(lines)
                else:
                    print("Lettura annullata - il file non esiste")
            case 3:
                print("Fine programma.")
                break
        input("premi invio per continuare...")


main()
