# prendere in input più numeri e contare i pari e dispari
from funzioni import funzioni


def calc_pari_dispari():
    n = funzioni.input_gen("Inserisci un numero, zero per terminare: ", int)
    ndispari = 0
    npari = 0
    while n != 0:
        if (n % 2 == 1):
            ndispari += 1
        else:
            npari += 1
        n = funzioni.input_gen("Inserisci un numero, zero per terminare: ", int)
    return npari, ndispari


def main():
    p, d = calc_pari_dispari()  # npari finisce nella p e ndispari nella d
    print("Pari = ", p, "\nDispari = ", d)

main()