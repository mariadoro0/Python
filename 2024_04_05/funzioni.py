def input_gen(st, tipo):
    while True:
        try:
            x = tipo(input(st))
            break
        except:
            print("Errore! Input errato.")
    return x



def input_maggiore(st, tipo, m):
    while True:
        n=input_gen(st,tipo)
        if not (n>m):
            print("Numero errato, inserisci un numero maggiore di "+str(m)+": ")
        else:
            break
    return n

def input_range(st, tipo, m1, m2):
    while True:
        n=input_gen(st,tipo)
        if not(n>=m1 and n<=m2):
            print("Input errato. Il numero non rientra nel range richiesto.")
        else:
            break
    return n

def input_data(st):
    from datetime import datetime
    while True:
        stdata=input(st)
        try:
            d=datetime.strptime(stdata, '%d/%m/%Y')
            break
        except:
            print("Formato della data non valido! Formato giusto: gg/mm/aaaa")
    return d



