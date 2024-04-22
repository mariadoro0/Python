#crea tabella  di numeri interi usando lista di lista
from random import randint


def crea_matrice(r,c):
    tab=[]
    for j in range(r):
        riga=[0]*c
        tab.append(riga)
    return tab

def stampa_matrice(tab,r,c):
    for i in range(len(tab)):
        for j in range(r):
            print(tab[i][j], end=" ")
        print()

def carica_matrice(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            tab[i][j]=randint(1,100)

def main():
    r=10
    c=15
    tab=crea_matrice(r,c)
    carica_matrice(tab)
    stampa_matrice(tab,r,c)

main()