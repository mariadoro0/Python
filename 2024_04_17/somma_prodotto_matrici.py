from random import randint


def crea_matrice(r, c):
    tab = []
    for j in range(r):
        riga = [0] * c
        tab.append(riga)
    return tab


def stampa_matrice(tab, r, c):
    for i in range(len(tab)):
        for j in range(r):
            print(tab[i][j], end=" ")
        print()
    print()


def carica_matrice(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            tab[i][j] = randint(10, 30)


def somma_matrici(c, a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j] = a[i][j] + b[i][j]


def prodotto_matrici(d, a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            d[i][j] = a[i][j] * b[i][j]


def main():
    rows = 5
    columns = 5
    a = crea_matrice(rows, columns)
    b = crea_matrice(rows, columns)
    c = crea_matrice(rows, columns)
    d = crea_matrice(rows, columns)
    carica_matrice(a)
    carica_matrice(b)
    stampa_matrice(a, rows, columns)
    stampa_matrice(b, rows, columns)
    somma_matrici(c, a, b)
    prodotto_matrici(d, a, b)
    stampa_matrice(c, rows, columns)
    stampa_matrice(d, rows, columns)


main()
