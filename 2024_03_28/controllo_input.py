#x=input("Inserisci un numero: ")
#x=int(x)                            #se io non metto un numero e non effettuo un controllo, il programma da error

while True:
    try:
        x=int(input("Inserisci un numero: "))   #al posto di int si possono mettere i vari tipi di variabile es float
        break                                   #esce dal while se try va a buon fine
    except:
        print("Numero non valido")
print("hai inserito il numero ",x)


while True:
    try:
        x=float(input("Inserisci un numero: "))
        y=5/x
        break
    except ValueError:                          #si possono specificare i vari tipi di errore
        print("Valore errato")
    except ZeroDivisionError:
        print("Non è possibile effettuare una divisione per 0")
    except:                                     #l'except da solo vale per gli errori trovati che non sono stati specificati
        print("Numero non valido")
print("Risultato di 5/",x,":",y)