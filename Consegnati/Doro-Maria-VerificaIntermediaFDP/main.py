from funzioniMenu import menu


def main():
    #lista creata per avere una base nel test, commentabile
    lista = [{"Nome Squadra": "Juve", "Colore della maglia": "bianconero", "Punteggio": 45,
                 "Nome Allenatore": "Paolo", "Cognome Allenatore": "Rossi", "Titoli": 27},
             {"Nome Squadra": "Milan", "Colore della maglia": "rossonero", "Punteggio": 34,
             "Nome Allenatore": "Marco", "Cognome Allenatore": "Polo", "Titoli": 41}]

    menu(lista)


main()
