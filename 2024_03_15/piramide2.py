nblocchi=input("Inserire il numero di blocchi: ")
h = 0
blocco = 1
if nblocchi.isdigit():
    print("Hai inserito",nblocchi,"blocchi")
    blocchirimasti=int(nblocchi)
    while (blocchirimasti-blocco)>0:
        blocchirimasti = blocchirimasti - blocco
        blocco += 1
        h += 1
    print("Altezza: ", h, "\nBlocchi rimasti: ", blocchirimasti)
else:
    print("Numero non valido.")
