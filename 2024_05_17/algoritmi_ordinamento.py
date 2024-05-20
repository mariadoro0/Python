# INSERTION SORT
# gli scambi e i confronti avvengono a due a due
# Caso peggiore N*(N-1)/2 ---> O(n^2)
# aumentando il numero di recordla complessità aumenta in ordine quadratico

def insertionSort(lista):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]


# SELECTION SORT
# confronta la prima occorrenza con il resto cercando il minimo
# Caso peggiore: N-1 ---> O(n^2)

def selectionSort(lista):
    j, i, jmin = 0, 0, 0
    for i in range(len(lista) - 1):
        jmin = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[jmin]:
                # se l'elemento minore è in posizione j, assegna j a jmin
                jmin = j
                if (i != jmin):
                    # se (i != jmin) è stato trovato un elemento minore in posizione jmin
                    # SCAMBIO elemento in posizione i con elemento in posizione jmin
                    lista[jmin], lista[i] = lista[i], lista[jmin]


# BUBBLE SORT
# caso peggiore N*(N-1)/2 ---> O(n^2)

def bubbleSort(lista):
    # la variabile Scambio indica se durante una scansione si è verificato almeno uno scambio
    scambio = True
    ultimo = len(lista) - 1
    while ultimo > 0 and scambio:
        scambio = False
        for i in range(ultimo):
            if lista[i] > lista[i + 1]:
                scambio = True
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
        ultimo = ultimo - 1


# RICERCA SEQUENZIALE
# la lista deve essere ordinata
# costo: O(n)
# si ricerca l'elemento 1 a 1 e quando lo trova l'algoritmo viene interrotto

def ricercaSequenziale(lista, item):
    pos = 0
    found = False
    while pos < len(lista) and not found:
        if lista[pos] == item:
            found = True
        else:
            pos = pos + 1


# RICERCA BINARIA O DICOTOMICA
# la lista deve essere già stata ordinata
# costo O(log n)
# si divide l'array a metà ricorsivamente

def ricercaBinaria(lista, item):
    primo = 0
    ultimo = len(lista) - 1
    trovato = False
    while primo <= ultimo and not trovato:
        medio = primo + ultimo // 2
        if lista[medio] == item:
            trovato = True
        else:
            if item < lista[medio]:
                ultimo = medio - 1
            else:
                primo = medio + 1
    return trovato
