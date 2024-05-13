# tupla=lista immutabile, non si può modificare
# le tuple occupano meno spazio in memoria, e lavorare con le liste è più costoso per il pc
# quando non c'è bisogno di fare operazioni particolari sui dati, è meglio usare le tuple
# la tupla si identifica con le parentesi tonde

tupla = ('ciao', 'amici')
tupla2 = tuple(range(10, 15))
print(tupla, tupla2)

# concatenare un elemento ad una tupla
tupla2 = tupla2 + (0,)
print(tupla2)

# moltiplicazione:
tupla3 = tupla2 * 3
print(tupla3)

# fa la somma di una tupla di numeri
tot = sum(tupla3)

# converte una lista in una tupla
s = "No me importa"
tuplalist = tuple(s)
print(tuplalist)
# converte una tupla in una lista
ls = list(tuplalist)
print(ls)
