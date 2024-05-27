import operator

from inputDati import *
import os

stringa_menu = """=============== RUBRICA ==============
***************************** MENU SCELTA ******************************************
        1) Inserimento del numero di telefono.
        2) Modifica del numero di telefono.
        3) Stampa rubrica ordinata (per Nominativo o Città)
        4) Eliminazione numero di telefono.
        5) Scrittura su file 'Rubrica.txt'
        6) Lettura dal file 'Rubrica.txt'
        0) Uscita dal programma.
****************************************************************************************
"""


def menu():
    while True:
        os.system("cls")
        print(stringa_menu)
        sc = input_range("Scelta: ", int, 0, 6)
        break
    return sc


def inserimento_dati(rubrica):
    scelta = 'A'
    print("----------Inserimento dati-------------")
    while scelta != 'N':
        nome = input_gen("Inserire il nominativo: ", str)
        tel1 = input_telefono("Inserire numero di telefono 1: ", str)
        tel2 = input_telefono("Inserire numero di telefono 2: ", str)
        indirizzo = input_gen("Inserire indirizzo: ", str)
        citta = input_gen("Inserire città: ", str)
        societa = input_gen("Inserire società: ", str)
        diz = {"Nominativo": nome, "Telefono 1": tel1, "Telefono 2": tel2, "Indirizzo": indirizzo, "Città": citta,
               "Società": societa}
        rubrica.append(diz)
        print("Record inserito.")
        print("------------------------------------------")
        scelta = input_str("Continuare? [S]ì, [N]o. ", str, 'S', 'N')


def modifica_numero(rubrica, rmod, tmod):
    telnew = input_telefono("Inserire il nuovo numero: ", str)
    if tmod == 1:
        rubrica[rmod].update({'Telefono 1': telnew})
    else:
        rubrica[rmod].update({'Telefono 2': telnew})


def ordina_rubrica(rubrica, mode):
    rubricaord = []
    match mode:
        case 'N':
            rubricaord = (sorted(rubrica, key=operator.itemgetter("Nominativo")))
        case 'C':
            rubricaord = (sorted(rubrica, key=operator.itemgetter("Città")))

    return rubricaord


def stampa_rubrica(rubrica):
    txt = "{:<20} {:<15} {:<15} {:<30} {:<15} {:<30}"
    print(txt.format("Nominativo", "Telefono1", "Telefono2", "Indirizzo", "Città", "Società"))
    for r in rubrica:
        print(txt.format(r['Nominativo'], r['Telefono 1'], r['Telefono 2'], r['Indirizzo'], r['Città'], r['Società']))


def scelta_record(rubrica):
    for i in range(len(rubrica)):
        print(f"{i + 1}) {rubrica[i]}")
    rmod = input_range("Quale record si intende modificare?", int, 1, len(rubrica))
    print("Modifica del record ", rmod)
    rmod = rmod - 1
    return rmod


def elimina_numero(rubrica, rmod, tmod):
    if tmod == 1:
        rubrica[rmod].update({'Telefono 1': ""})
    else:
        rubrica[rmod].update({'Telefono 2': ""})


def apri_file(file, mod, enc):
    f = None
    try:
        f = open(file, mod, encoding=enc)
    except IOError as e:
        print(os.strerror(e.errno))
    return f



def scrittura_file(f, rubrica):
    for r in rubrica:
        f.write(f"{r['Nominativo']};{r['Telefono 1']};{r['Telefono 2']};{r['Indirizzo']};{r['Città']};{r['Società']}")
        f.write("\n")
