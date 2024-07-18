from Dirigente import Dirigente
from FunzionarioJunior import FunzionarioJunior
from FunzionarioSenior import FunzionarioSenior
from GestioneProgetti import GestioneProgetti
from TecnicoEleAut import TecnicoEleAut
from TecnicoInfTel import TecnicoInfTel
from inputDati import input_gen, input_range, input_str


def menu():
    strmenu = """
    =====MENU PROGETTO====
    1. Aggiungi persona.
    2. Elimina persona.
    3. Cerca persone.
    4. Stampa elenco completo.
    5. Stampa il numero totale di persone.
    6. Stampa il costo totale del progetto.
    0. Esci dal programma.
    Scelta:"""
    scelta = input(strmenu)
    return scelta

def creaPersonale(type):
    codice = input("Inserire il codice: ")
    nome = input_gen("Inserire il nome:", str)
    cognome = input_gen("Inserire il cognome:", str)
    annoAssunzione = input_gen("Inserire l'anno di assunzione:", int)
    oreLavorate = input_gen("Inserire le ore lavorate:", int)
    match type:
        case 1:
            p = Dirigente(codice, cognome, nome, annoAssunzione, oreLavorate)
        case 2:
            p = FunzionarioSenior(codice, cognome, nome, annoAssunzione, oreLavorate)
        case 3:
            p = FunzionarioJunior(codice, cognome, nome, annoAssunzione, oreLavorate)
        case 4:
            interno = input_str("Inserire se il tecnico è interno o no: [S]ì o [N]o. ", str, 'S', 'N')
            if interno == 'S':
                interno = True
            else:
                interno = False
            p = TecnicoEleAut(codice, cognome, nome, annoAssunzione, oreLavorate, interno)
        case 5:
            interno = input_str("Inserire se il tecnico è interno o no: [S]ì o [N]o. ", str, 'S', 'N')
            if interno == 'S':
                interno = True
            else:
                interno = False
            p = TecnicoInfTel(codice, cognome, nome, annoAssunzione, oreLavorate, interno)
    return p


def scegliTipo():
    strtype = """
    Inserire il tipo di dipendente da aggiungere:
    1. Dirigente
    2. Funzionario Senior
    3. Funzionario Junior
    3. Tecnico Elettronico/Automazione
    5. Tecnico Informatico/
    Scelta: """
    print(strtype)
    type = input_range("Inserire il tipo dipendente da aggiungere:", int, 1, 5)
    return type


def main():
    elenco = GestioneProgetti()
    elenco.aggiungiPersona(Dirigente(1, "Doro", "Maria", 2012, 80))
    elenco.aggiungiPersona(FunzionarioSenior(2, "Rossi", "Paolo", 2021, 51))
    elenco.aggiungiPersona(FunzionarioJunior(3, "Polo", "Marco", 2023, 48))
    elenco.aggiungiPersona(TecnicoInfTel(4, "Verdi", "Carla", 2022, 58, True))
    elenco.aggiungiPersona(TecnicoEleAut(5, "Gialli", "Stefano", 2019, 70, False))

    while True:
        scelta = menu()
        match scelta:
            case '1':
                persona = creaPersonale(scegliTipo())
                elenco.aggiungiPersona(persona)
            case '2':
                nome = input_gen("Inserire il nome: ", str)
                check = elenco.eliminaPersona(nome)
                if check:
                    print("Persona eliminata correttamente.")
                else:
                    print("Persona non trovata")
            case '3':
                nome = input_gen("Inserire il nome: ", str)
                check, persona = elenco.cercaPersona(nome)
                if check:
                    print("Persona trovata.")
                    print(persona)
                else:
                    print("Persona non trovata.")
            case '4':
                strtot = elenco.elencoPersone()
                print(strtot)
            case '5':
                print("Sono presenti " + str(elenco.getTotPersone()) + " persone in elenco.")
            case '6':
                anno = input_gen("Inserire l'anno del progetto: ", int)
                print("Costo totale del progetto: " + str(elenco.costiProgetto(anno)) + " euro.")
            case '0':
                break


main()
