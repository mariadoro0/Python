# insieme di coppie chiave-valore, ogni chiave è unica
# una chiave può essere qualsiasi tipo di oggetto immutabile
# per crearlo si usano le graffe
# valore : corrispondenza

diz = {'mamma': 'mom', 'papà': 'dad', 'cane': 'dog'}
dz = dict(mamma="mom", papa="dad", cane="dog")
print(diz, dz)

# restituisce l'elenco delle chiavi
dizionario = diz.keys()
print(dizionario)

# restituisce l'elenco di valori di un dizionario
dizionario2 = diz.values()
print(dizionario2)

# restituisce l'elenco delle coppie chiave:valore
dizionario3 = diz.items()
print(dizionario3)

# i dizionari non si scorrono con gli indici, ma con le parole chiave.
parole = ['cane', 'gatto', 'leone']
for p in parole:
    if p in diz:
        print(p, "-->", diz[p])  # diz[p] non si riferisce alla posizione, ma alla coppia chiave:valore
    else:
        print(p, "non è nel dizionario")

# altri modi di stampare:
print("\n")
for ita, en in diz.items():
    print(ita, "-->", en)

# modifica in un dizionario:
diz['cane'] = "doggo"
print(diz)

# aggiungere una nuova chiave:valore
diz.update({'gatto': 'cat'})
print(diz)

# cancellare una chiave
del diz['gatto']
print(diz)

# cancellare l'ultimo elemento inserito
diz.popitem()
print(diz)

# get(chiave): restituisce il valore corrispondente alla chiave
value = diz.get('mamma')
print(value)
