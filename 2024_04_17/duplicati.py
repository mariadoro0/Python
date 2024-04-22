#eliminare duplicati da una lista
from funzioni import input_maggiore
from random import randint


def dimensione():
    n = input_maggiore("Quanti numero vuoi inserire?\n", int,0)
    return n


def riempi_random(lista1, n):
    for i in range(n):
        lista1.append(randint(1, 10))


def elimina_doppi(lista1):
    lista=[]
    for x in lista1:
        for y in lista1:
            if x==y and lista1.index(x)!=lista1.index(y):
                lista1.pop(lista.index(x))
                break
            elif x!=y or (x==y and lista1.index(x)==lista1.index(y)):
                lista.append(x)
                break
    return lista1

##SBAGLIATO


def main():
    print("Programma che elimina gli elementi duplicati di una lista.")
    lista1 = []
    n = dimensione()
    riempi_random(lista1, n)
    print(lista1)
    lista_fin=elimina_doppi(lista1)
    print(lista_fin)

main()
