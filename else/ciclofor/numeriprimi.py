
n=input("Inserisci un numero: ")
nprimo=True
st=""
if n.isdigit():
    n=int(n)
    for i in range(2, n - 1):
        r = n % i
        if r==0:
            nprimo=False
         # print("Divisore: ", i)
            st=st+str(i)+" "
    if nprimo==True:
        print("Il numero è primo")
    else:
        print("Il numero non è primo. I divisori sono: ", st)
else:
    print("Il valore inserito non è un numero")

