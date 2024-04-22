#contare le parole con più di due caratteri in una frase lunga

def conta_parole(stringa):
    lista = stringa.split(" ")
    counter = 0
    for x in lista:
        x=x.strip(",'’.?!-_+:;")
        word = list(x)
        if len(word) > 2:
            counter += 1
    return counter


def main():
    stringa = "Se ni’ mondo esistesse un po’ di bene, e ognun si honsiderasse suo fratello, ci sarebbe meno pensieri e meno pene,e il mondo ne sarebbe assai più bello"
    count = conta_parole(stringa)
    print("Ci sono", count, "parole con più di due caratteri")


main()
