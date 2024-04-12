def main():
    print("Programma che calcola quanti numeri sono pari e dispari")
    pari=0 ; dispari=0
    a=True

    while a==True:
        num=int(input("Inserire un numero: "))
        if num%2==0:
            pari=pari+1
        else:
            dispari=dispari+1
        a=bool(int(input("Inserire 0 per terminare, qualsiasi numero per continuare. ")))
    print("\n")
    print("I numeri pari sono: ",pari, "\nI numeri dispari sono: ",dispari)