dizionario = {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval'}
phone = {'boss': 123456789, 'franco': 482342947, 'archimede': 97632478}
diz_vuoto = {}
print(dizionario)
print(dizionario['horse'])
parole = ['cat', 'lion', 'panda', 'dog']
# controllo se una parola della lista è presente nel dizionario e stampa il valore
print("----------------------")
for p in parole:
    if p in dizionario:
        print(p, "è presente nel dizionario e corrisponde a :", dizionario[p])
    else:
        print(p, " non è presente nel dizionario")

# stampa del dizionario tramite la chiave
print("----------------------")
for k in dizionario.keys():
    print(k, "--->", dizionario[k])
print("----------------------")

# stampa ordinata con keys
for k in sorted(phone.keys()):
    print(k, "--->", phone[k])

#stampa con items in ordine decrescente
print("----------------------")
for h, k in sorted(phone.items(), reverse=True):
    print(h, "--->", k)

# converto dizionario in una lista
print("----------------------")
st = list(dizionario.keys())
print(st)
# convertire un dizionario in una lista, crea una lista solo di chiavi
st1 = list(dizionario)
print(st1)

d = dict()
for chiave, valore in sorted(dizionario.items()):
    d.update({chiave : valore})
print(d)

# aggiungo un dizionario ad un altro
d2=dict()
d.update({'frog':'grenouille'})
d2=d
print(d)
print(d2)
