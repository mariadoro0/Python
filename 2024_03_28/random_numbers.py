#uso di numeri random
import random

numero= random.random()         #funzione random del modulo random, stampa un numero tra 0 e 0.99999999
print(numero)

from random import random,randrange, randint, sample   #importo solo la funzione dal modulo
numero=random()             #facendo così non c'è bisogno di scrivere random.random
print(numero)
#seed(4)  generatore di numeri casuali, inizializza i numeri casuali da quello che decide l'utente
print("\nCinque numeri random:")
for i in range(5):
    print(random(), end="  -  ")

#randrange(1,20)             #prende un numero casuale in range da 1 a 20
#randrange(1,20,2)          si può specificare anche lo step tra un numero e l'altro
print("\nNumeri random interi tra 1 e 20 con randrange:")
for i in range(5):
    print(randrange(1,20), end="  -  ")

#randint(1,20)              #genera un numero intero nell'intervallo
print("\nNumeri random interi tra 1 e 20 con randint:")
for i in range(5):
    print(randint(1,20),end="  -  ")

#generiamo una lista di numeri casuali
lista_numeri_casuali=[]             #creazione di una lista vuota
for x in range(0,6):                #da 0 a 5
    y=randint(1,45)
    lista_numeri_casuali.append(y)          #.append aggiunge il numero alla lista

print("\nLista di numeri casuali:\n",lista_numeri_casuali)


print("Lista con sample:")
lista=sample(range(1,45),6)             #estrae 6 numeri (k) in quel range
print(lista)



