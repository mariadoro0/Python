nblocchi=input("Inserire il numero di blocchi: ")
h = 0
blocco = 1
if nblocchi.isdigit():
    print("Hai inserito",nblocchi,"blocchi")
    nblocchi=int(nblocchi)
    blocchirimasti = nblocchi
    flag = False
    while flag == False:
        blocchirimasti = blocchirimasti - blocco
        if (blocchirimasti) < 0:
            blocchirimasti += blocco
            flag = True
            break
        blocco += 1
        h += 1
else:
    print("Numero non valido.")


print("Altezza: ",h,"\nBlocchi rimasti: ",blocchirimasti)