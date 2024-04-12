# calcola se bisestile e il numero giorni di un mese
from funzioni import input_gen


def is_bisestile(a: int):
    r = False
    if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
        r = True
    return r


def giorni_in_mese(m, a):
    if m < 1 or m > 12:
        return None
    else:
        giorni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        g = giorni[m - 1]
        if m == 2 and is_bisestile(a):
            g = 29

    return g


def main():
    print("Programma che restituisce il numero di giorni del mese e dell'anno specificato.")
    stdata = input_gen("Inserisci un mese e un anno in formato mm/aaaa: ", str)
    mese, anno = stdata.split("/")
    if mese.isdigit() and anno.isdigit():
        mese = int(mese)
        anno = int(anno)
        giorni = giorni_in_mese(mese, anno)
        if giorni is not None:
            print("giorni del mese ", mese, ": ", giorni)
        else:
            print("Inpur errato.")


main()
