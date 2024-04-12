#verifica delle variabili
x=2
y=4.0
s=("parola")
lista=[2,4,6]

#type() dice il tipo di variabile
print(type(x))
print(type(y))
print(type(s))
print(type(lista))

if (type(x)==int):
    print("x è un numero intero")
if (type(y)==float):
    print("y è un numero float")
if (type(s)==str):
    print("s è una stringa")
if(type(lista)==list):
    print("lista è una lista")