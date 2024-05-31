def input_gen(st, tipo):
    while True:
        try:
            x = tipo(input(st))
            break
        except:
            print("Errore! Input errato.")
    return x


def input_maggiore(st, tipo, m=0):
    while True:
        n = input_gen(st, tipo)
        if not (n > m):
            print("Numero errato, inserisci un numero maggiore di " + str(m) + ": ")
        else:
            break
    return n


def input_maggioreuguale(st, tipo, m=0):
    while True:
        n = input_gen(st, tipo)
        if not (n >= m):
            print("Numero errato, inserisci un numero maggiore o uguale a " + str(m) + ": ")
        else:
            break
    return n


def input_range(st, tipo, m1, m2):
    while True:
        n = input_gen(st, tipo)
        if not (m1 <= n <= m2):
            print("Input errato. Il numero non rientra nel range richiesto.")
        else:
            break
    return n


def input_data(st):
    from datetime import datetime
    while True:
        stdata = input(st)
        try:
            d = datetime.strptime(stdata, '%d/%m/%Y')
            break
        except:
            print("Formato della data non valido! Formato giusto: gg/mm/aaaa")
    return d


def input_str(st, tipo, type1, type2):
    while True:
        n = input_gen(st, tipo)
        n = n.upper()
        type1 = type1.upper()
        type2 = type2.upper()
        if n == type1:
            break
        elif n == type2:
            break
        else:
            print("Input non valido. Inserire un carattere tra quelli indicati.")
    return n


def input_telefono(st, tipo):
    while True:
        n = input_gen(st, tipo)
        if len(n) != 10:
            print("Numero di telefono non valido. Lunghezza errata. Inserire 10 numeri.")
        else:
            break
    return n
