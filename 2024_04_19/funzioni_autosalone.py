from funzioni import *
def dati_persona():
    print("                 Dati dell'acquirente        ")
    nome = input_gen("Inserire il nome: ", str)
    cognome = input_gen("Inserire il cognome: ", str)

    return nome, cognome


def dati_auto():
    print("                 Dati dell'auto          ")
    marca = input_gen("Inserire la marca: ", str)
    cilindrata = input_gen("Inserire una cilindrata: ", int)
    anno_imm = input_range("Inserire l'anno di immatricolazione: ", int, 1910, 2024)
    print("-----------------------------------------------------------")
    return marca, cilindrata, anno_imm

def inserimento_dati(auto):
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
        auto.append(persona)
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


def visualizza_cc(auto):
    for p in auto:
        if p[1] > 1500:
            print(p[4])


def auto_tot(auto, anno):
    counter = 0
    for p in auto:
        if p[2] == anno:
            counter += 1
            print(p)
    return counter


def a(auto):
    return auto[2]


def ordina_anno(auto):
    auto.sort(key=a)


def stampa_anno(auto):
    print("Anno: ", auto[0][2])
    for i in range(len(auto)):
        if i > 0 and auto[i][2] != auto[i - 1][2]:
            print("Anno: ", auto[i][2])
        print("\t", auto[i][0], auto[i][1], ",", auto[i][3])
