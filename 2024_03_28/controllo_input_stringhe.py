#controlla stringhe
while True:
    st=input("Inserisci 'S' o 'F' o 'C':\n")
    if(st!='S' and st!='F' and st!='C'):
        print("Inserimento errato")
    else:
        break

print("Hai inserito: ", st)


while True:
    try:
        st=input("Inserisci 'S' o 'F' o 'C':\n")
        if(st!='S' and st!='F' and st!='C'):
            raise Exception("valore "+st+" non valido.")            #raise Exception solleva un eccezione
        break
    except Exception as error:                                                      #se c'è stata un'eccezione, mette Exception nella variabile error
        print(error)


print("Hai inserito: ", st)
