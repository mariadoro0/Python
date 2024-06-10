import operator

from funzInput import input_range, input_gen, input_str


def menu(lista):
    ins = False
    scelta = -1
    while scelta != 8:
        print("--------------------------------------------------------------------")
        print("                 MENU'               ")
        print("Scegli una delle seguenti opzioni:")
        print("1. Inserimento dati delle squadre")
        print("2. Stampa la classifica in ordine decrescente di punteggio.")
        print("3. Modifica i punti di una squadra")
        print("4. Stampa la classifica dei titoli degli allenatori in ordine decrescente.")
        print("5. Numero di allenatori che hanno vinto X titoli.")
        print("6. Stampa squadre con più di X punti.")
        print("7. Stampa squadre con allenatori che hanno vinto più di X titoli.")
        print("8. Chiudi.")
        print("--------------------------------------------------------------------")
        scelta = input_range("La tua scelta: ", int, 1, 8)

        if scelta == 1:
            inserimento_dati(lista)
            ins = True
        else:
            if not ins and scelta != 1:
                print("E' necessario prima inserire i valori.")
            elif ins and scelta != 1:

                if scelta == 2:
                    lista=ordina_punti_desc(lista)
                    stampa_squadra_desc(lista)

                elif scelta == 3:
                    done = False
                    check = 0
                    while not done:
                        squadra = input_gen("Inserire la squadra della quale si desidera modificare il punteggio: ",
                                            str)
                        for r in lista:
                            check += 1
                            if squadra == r["Nome Squadra"]:
                                pnt = input_gen("Qual è il nuovo punteggio? ", int)
                                modifica_punti(lista, squadra, pnt)
                                done = True
                            else:
                                continue
                        if check == len(lista) and done == False:
                            print("Squadra inserita non presente nell'elenco.")

                elif scelta == 4:
                    lista=ordina_titoli_desc(lista)
                    stampa_titoli_desc(lista)

                elif scelta == 5:
                    titoli = input_gen("Inserisci il numero di titoli da cercare: ", int)
                    cnt = conta_allenatori(lista, titoli)
                    print("Numero di allenatori ad aver vinto ", titoli, " titoli: ", cnt)

                elif scelta == 6:
                    pnt = input_gen("Inserire il numero di punti per filtrare: ", int)
                    lista=ordina_punti_desc(lista)
                    stampa_per_punti(lista, pnt)

                elif scelta == 7:
                    titoli = input_gen("Inserire il numero di titoli per filtrare: ", int)
                    lista=ordina_titoli_desc(lista)
                    stampa_per_allen(lista, titoli)


def inserimento_dati(lista):
    risp = 'A'
    while risp != 'N':
        nome = input_gen("Inserire il nome della squadra: ", str)
        colore = input_gen("Inserire il colore della maglia: ", str)
        punteggio = input_gen("Inserire il punteggio: ", int)
        nomeall = input_gen("Inserire il nome dell'Allenatore: ", str)
        cognomeall = input_gen("Inserire il cognome dell'Allenatore: ", str)
        titoli = input_gen("Inserire il numero di titoli vinti: ", int)
        diz_squadra = {"Nome Squadra": nome, "Colore della maglia": colore, "Punteggio": punteggio,
                       "Nome Allenatore": nomeall, "Cognome Allenatore": cognomeall, "Titoli": titoli}
        lista.append(diz_squadra)
        risp = input_str("\nContinuare? Inserisci 'S' per Sì o 'N' per No.", str, 'S', 'N')


def ordina_punti_desc(lista):
    lista_dec = []
    lista_dec = (sorted(lista, key=operator.itemgetter("Punteggio"), reverse=True))
    return lista_dec
def stampa_squadra_desc(lista):
    print("--------------------------------------------------------------------")
    print("\n")
    print("     LISTA DELLE SQUADRE IN ORDINE DECRESCENTE DI PUNTEGGIO")
    txt = "{:.<20} {:<8} {:<8}"
    print(txt.format("Nome Squadra","Punti","Colore maglia"))
    for r in lista:
        print(txt.format(r["Nome Squadra"], r["Punteggio"], r["Colore della maglia"]))



def modifica_punti(lista, squadra, pnt):
    for r in lista:
        if r["Nome Squadra"] == squadra:
            r.update({"Punteggio": pnt})


def ordina_titoli_desc(lista):
    lista_dec = []
    lista_dec = (sorted(lista, key=operator.itemgetter("Titoli"), reverse=True))
    return lista_dec
def stampa_titoli_desc(lista):
    print("--------------------------------------------------------------------")
    print("\n")
    print("     LISTA DEGLI ALLENATORI IN ORDINE DECRESCENTE DI TITOLI")
    txt = "{:.<20} {:<8} {:<8}"
    print(txt.format("Allenatore", "Titoli", "Squadra"))
    for r in lista:
        print(txt.format(r["Nome Allenatore"]+" "+r["Cognome Allenatore"], r["Titoli"], r["Nome Squadra"]))



def conta_allenatori(lista, titoli):
    cnt = 0
    for r in lista:
        if r["Titoli"] == titoli:
            cnt += 1
    return cnt


def stampa_per_punti(lista, pnt):
    print("--------------------------------------------------------------------")
    print("\n")
    print("     LISTA DELLE SQUADRE AVENTI ALMENO",pnt,"PUNTI")
    txt = "{:.<20} {:<8}"
    print(txt.format("Squadra", "Punti"))
    for r in lista:
        if r["Punteggio"] >= pnt:
            print(txt.format(r["Nome Squadra"], r["Punteggio"]))


def stampa_per_allen(lista, titoli):
    print("--------------------------------------------------------------------")
    print("\n")
    print("     LISTA DEGLI ALLENATORI AVENTI ALMENO ",titoli," TITOLI")
    txt = "{:.<20} {:<8} {:<8}"
    print(txt.format("Squadra", "Titoli", "Allenatore"))
    for r in lista:
        if r["Titoli"] >= titoli:
            print(txt.format( r["Nome Squadra"],r["Titoli"],r["Nome Allenatore"] + " " + r["Cognome Allenatore"]))
