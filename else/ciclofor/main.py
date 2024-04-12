#uso del for

for i in range(1,6):    #diverso dal ciclo for degli altri linguaggi
    if i==2:
        continue       #salta tutto ciò che viene dopo il continue e ricomincia il ciclo
    if i==4:
        break            #interrompe il for
    print (i)

#ciclo while
conta=0
n = int(input("Inserisci un numero oppure -1 per terminare: "))
print(n)
while n!=-1:
    conta = conta + 1
    n = int(input("Inserisci un numero oppure -1 per terminare: "))
    if n==3:
        break
    if n==4:
        continue
    print(n)

print(conta)

for i in range(1, 6):
    print(i)

print("\n")
for i in range(1, 6, 2):  # terzo parametro=incremento, incrementa di due
    print(i)




