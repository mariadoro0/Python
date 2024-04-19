import os

from funzioni import *
from os import *


def dati_persona():
    print("----Dati dell'acquirente----")
    nome = input_gen("Inserire il nome: ", str)
    cognome = input_gen("Inserire il cognome: ", str)

    return nome, cognome


def dati_auto():
    print("----Dati dell'auto----")
    marca = input_gen("Inserire la marca: ", str)
    cilindrata = input_gen("Inserire una cilindrata: ", int)
    anno_imm = input_range("Inserire l'anno di immatricolazione: ", int, 1910, 2024)
    print("-------------------------")
    return marca, cilindrata, anno_imm


def inserimento_dati():
    cars = []
    cntn = "S"
    while cntn != "N":
        persona = []
        nome, cognome = dati_persona()
        marca, cilindrata, anno_imm = dati_auto()
        persona.append(marca)
        persona.append(cilindrata)
        persona.append(anno_imm)
        persona.append(nome)
        persona.append(cognome)
        cars.append(persona)
        flag = True
        while flag:
            try:
                cntn = input_gen("Continuare? [S]i/[N]o. Inserisci S o N. ", str)
                cntn.upper()
                if cntn != "S" and cntn != "N":
                    raise Exception("Input non valido. Inserisci S o N. ")
                else:
                    flag = False
            except Exception as error:
                print(error)

    return cars


def visualizza_cc(auto):
    for p in auto:
        if p[1] > 1500:
            print(p[4])



def auto_tot(auto):
    anno = input_range("Inserire l'anno di immatricolazione ", int, 1910, 2024)
    counter = 0
    for p in auto:
        if p[2] == anno:
            counter += 1
            print(p)
    print("Ci sono ", counter, " auto immatricolate nel ", anno)



def a(auto):
    return auto[2]


def ordina_anno(auto):
    auto.sort(key=a)


def stampa_anno(auto):
    auto.sort(key=a)
    print("Anno: ", auto[0][2])
    for i in range(len(auto)):
        if i > 0 and auto[i][2] == auto[i - 1][2]:
            print("Anno: ", auto[i][2])
        print("\t", auto[i][0], auto[i][1], ",", auto[i][3])



def menu(auto):
    scelta = -1
    while scelta != 0:
        print("-------------------------")
        print("0. Uscita")
        print()
        print("1. Visualizzare il cognome degli acquirenti di auto di cilindrata superiore a 1500cc.")
        print("2. Visualizzare il numero totale di auto immatricolate in un anno specifico.")
        print("3. Ordina l'elenco in base all'anno di immatricolazione.")
        print("4. Stampa l'elenco delle auto ordinato per anno di immatricolazione.")
        print("...")
        print()
        scelta = input_range("Scegli: ", int, 1, 4)
        print("premi invio per continuare...")
        os.system('cls')
        print("------------------------")


        if scelta == 1:
            visualizza_cc(auto)
        elif scelta == 2:
            auto_tot(auto)
        elif scelta == 3:
            ordina_anno(auto)
        elif scelta == 4:
            stampa_anno(auto)


def main():
    #auto = inserimento_dati()
    auto = [["BMW", 1500, 2010, "Maria", "Doro"], ["Audi", 2000, 2008, "Andrea", "Rossi"],
            ["Fiat", 1200, 2010, "Paola", "Bianchi"], ["Citroen", 1700, 2021, "Giulio", "Verdi"]]
    print("-------------------------")
    print("Come desideri procedere?")
    menu(auto)


main()
