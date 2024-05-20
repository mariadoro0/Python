from funzioni import funzioni


def fattoriale(n: int):
    if n < 0:
        fact = None
    elif n < 2:
        fact = 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
    return fact


def main():
    x = funzioni.input_gen("Inserire un numero di cui fare il fattoriale: ", int)
    n=fattoriale(x)
    print("fattoriale di "+str(x)+" = ",n)

main()