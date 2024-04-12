#fattoriale di 8= 8*7*6*5*4*3*2*1
n=int(input("Inserisci un numero positivo di cui fare il fattoriale: "))
if(n<0):
    print("Numero non valido")
else:
    x=1
    for i in range (1,n+1):
        x=x*i
    print("Il fattoriale di",n,"è",x)