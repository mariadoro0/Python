from CD import CD
from funzioni import *


def main():
    """   titolo=input_gen("Inserire il titolo del disco: ", str)
    autore=input_gen("Inserire l'autore del disco: ", str)
    annouscita = input_range("Inserire la data di uscita: ", int, 1900, 2024)
    prezzo= input_gen("Inserire il prezzo: ", float)
    Disco1 = CD(titolo,autore,annouscita)

    Disco1.modifica_prezzo(12.50)

    print(Disco1)
    print(Disco1.get_titolo())
    print(Disco1.get_autore())
    print(Disco1.get_annouscita())
    print(Disco1.get_prezzo())

    cnt=0
    dischi=[]
    for cnt in range(3):
        print("--------INSERIMENTO CD------------")
        titolo = input_gen("Inserire il titolo del disco: ", str)
        autore = input_gen("Inserire l'autore del disco: ", str)
        annouscita = input_range("Inserire la data di uscita: ", int, 1900, 2024)
        prezzo = input_gen("Inserire il prezzo: ", float)
        d=CD(titolo, autore, annouscita, prezzo)
        dischi.append(d)

    for d in dischi:
        print(d) """

    dischi = []
    for cnt in range(3):
        d = CD()
        print("-----------INSERIMENTO DISCHI-------------")
        d.set_titolo(input_gen("Inserire il nome del disco: ", str))
        d.set_autore(input_gen("Inserire l'autore del disco: ", str))
        d.set_annouscita(input_range("Inserire l'anno di uscita: ", int, 1900, 2024))
        d.modifica_prezzo(input_maggiore("Inserire il prezzo: ", float, 1))
        dischi.append(d)

    for d in dischi:
        print(d)


main()
