#calcola quanti numeri sono pari e quanti sono dispari
print("Programma che calcola quanti numeri sono pari e dispari.")
n=int(input("inserisci un numero, (0 per terminare): "))
pari=0
dispari=0
while n!=0:
    if(n%2==0):
        print("Il numero è pari")
        pari=pari+1
    else:
        print("Il numero è dispari")
        dispari=dispari+1
    n=int(input("inserisci un numero, (0 per terminare): "))

print("Hai inserito", pari,"numeri pari.\nHai inserito",dispari,"numeri dispari")
