lista = ["Ugo", "Ernesto", "Carolina", "Mario", "Roberta"]
print(lista)
lista[2] = "Gianluca"
print(lista)
dim = len(lista)
print(dim)
l = lista[1:3]  #slice: prende gli elementi da 1 a 3-1
print(l)

#scorrere gli elementi
for i in range(len(lista)):
    print(lista[i])
print("\n")
#prende un elemento della lista e lo salva nella variabile elemento
for elemento in lista:
    print(elemento)

#scambiare due elementi di una lista
lista[0], lista[4] = lista[4], lista[0]
print("\n", lista)

#funzione per invertire gli elementi
lista.reverse()
print(lista)

#aggiungere elementi
lista.append("Mario")

#dice quante volte un'elemento appare in una lista
print(lista.count("Mario"))

#aggiunge un elemento ad una posizione specifica e scala in avanti gli altri
lista.insert(3,"Paolo")

#aggiunge una lista ad un altra lista
lista.extend(l)
print(lista)

#estrarre un elemento e cancellarlo dalla lista
#volendo, .pop ritorna un valore, quindi si può salvare ciò che si elimina
lista.pop(2)
a=lista.pop(2)
print(a,lista)

#ordinare una lista: funziona solo se gli elementi sono tutti dello stesso tipo
#l'ordinamento è in ordine alfabetico (str) o crescente(numeri)
lista.sort()
print(lista)
#reverse=True ordina in ordine decrescente/alfabetico inverso
lista.sort(reverse=True)
print(lista)

#index restituisce la posizione dell'elemento indicato, da errore se l'elemento non c'è (usare try)
#a differenza di find, che non da errore se non lo trova
dove=lista.index("Mario")
print(dove)

#rimuove un elemento della lista, se non lo trova da errore (usare try)
lista.remove("Ernesto")
print(lista)

#esegue una copia della lista
lista2=lista.copy()

#elimina tutti gli elementi
lista.clear()
print(lista)

#ricerca del massimo di una lista (nelle stringhe calcola dal codice ASCII
print(max(lista2),min(lista2))