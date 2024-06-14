from inputDati import *
from Docente import Docente
from Impiegato import Impiegato

def menu():
    str = """******* MENU DIPENDENTI *********
            1) Aggiunta di un nuovo dipendente
            2) Eliminazione di un dipendente
            3) Ricerca di un dipendente
            4) Visualizzazione di tutti i dipendenti 
            5) Stampa del numero totale dei dipendenti
            6) Eliminazione di tutti i dipendenti
            0) Uscita.

            Scelta: """
    scelta = input_range(str, int, 0, 6)
    return scelta


def creazione_dipendente(mode):
    nome = input_gen("Inserire il nome: ", str)
    ind = input_gen("Inserire l'indirizzo: ", str)
    sesso = input_str("Inserire il sesso (uomo o donna): ", str, "uomo", "donna").lower()
    if mode == "D":
        disciplina = input_gen("Inserire la disciplina: ", str)
        ruolo = input_gen("Inserire il ruolo: ", str)
        d = Docente(nome, ind, sesso, disciplina, ruolo)
    elif mode == "I":
        ufficio = input_gen("Inserire l'ufficio: ", str)
        d = Impiegato(nome, ind, sesso, ufficio)
    return d


def scelta_tipo():
    mode = input_str("Vuoi inserire un [D]ocente o un [I]mpiegato?", str, 'D', 'I')
    return mode


def scegli_chi():
    who = input_gen("Inserire il nome del dipendente da eliminare: ", str)
    return who


def checkLen(elenco):
    check = False
    if len(elenco.getElenco()) > 0:
        check = True
    return check

