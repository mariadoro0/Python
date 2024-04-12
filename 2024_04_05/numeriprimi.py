def is_primo(num):
    r = True
    for i in range(2, num):
        if (num % i) == 0:
            r = False
            break
    return r


def lista_divisori(num):
    lista = []
    for i in range(2, num):
        if (num % i) == 0:
            r=False
            lista.append(i)
    lista.append(num)
    return lista, r

def main():
    for i in range(1, 20):
        if is_primo(i + 1):
            print(i + 1, "è un numero primo")
        else:
            div,r=lista_divisori(i+1)
            print(i+1, " non è un numero primo.", "Divisori: ", div)





main()
