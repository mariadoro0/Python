from funzioniRubrica import *


def main():
    rubrica = []
    ins = False
    while True:
        os.system("cls")
        s = menu()
        match s:
            case 1:
                ins = True
                inserimento_dati(rubrica)
                print("Inserimento dati eseguito con successo.")
            case 2:
                if ins:
                    rmod = scelta_record(rubrica)
                    tmod = input_range("Quale numero di telefono si intende modificare? 1 o 2. ", int, 1, 2)
                    modifica_numero(rubrica, rmod, tmod)
                    print("Numero modificato con successo.")
                else:
                    print("E' prima necessario inserire i dati.")
            case 3:
                if ins:
                    mode = input_str("Ordinare per [N]ominativo o per [C]ittà? Inserire C o N. ", str, 'N', 'C')
                    rubrica = ordina_rubrica(rubrica, mode)
                    print("------Rubrica ordinata per "+mode+"-------")
                    stampa_rubrica(rubrica)
                else:
                    print("E' prima necessario inserire i dati.")

            case 4:
                if ins:
                    scelta = input_str("Cosa si intende eliminare? [R]ecord o [N]umero di telefono. ", str, 'R', 'N')
                    rmod = scelta_record(rubrica)
                    if scelta == 'R':
                        rubrica.pop(rmod)
                        print("Record eliminato.")
                    else:
                        tmod = input_range("Quale numero di telefono si intende eliminare? 1 o 2. ", int, 1, 2)
                        elimina_numero(rubrica, rmod, tmod)
                        print("Numero di telefono eliminato.")
                else:
                    print("E' prima necessario inserire i dati.")

            case 5:
                if ins:
                    f = apri_file("Rubrica.txt", "w", "utf-8")
                    if f is not None:
                        scrittura_file(f, rubrica)
                        f.close()
                        print("Scrittura su file completata.")
                    else:
                        print("Impossibile aprire il file.")
                else:
                    print("E' prima necessario inserire i dati.")

            case 6:
                f = apri_file("Rubrica.txt", "r", "utf-8")
                lines=[]
                if f is not None:
                    for line in f:
                        nome, tel1, tel2, indirizzo, citta, societa = line.strip().split(';')
                        diz = {"Nominativo": nome, "Telefono 1": tel1, "Telefono 2": tel2, "Indirizzo": indirizzo,
                               "Città": citta,
                               "Società": societa}
                        lines.append(diz)
                    f.close()
                    print("Numero di record presenti: ", len(lines))
                else:
                    print("Impossibile aprire il file.")
            case 0:
                break
        input("premi invio per continuare....")


main()
