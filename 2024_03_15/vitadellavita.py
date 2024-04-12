#calcola il numero della vita di una persona conoscendo la data di nascita
#esempio: 01/01/1987 0+1+0+1+1+9+8+7=27 -> 2+7= 9 è il numero della vita

data=input("Inserisci la tua data di nascita: (formato YYYYMMDD):\n")
if len(data)!=8 or data.isdigit()!=True:
    print("Hai sbagliato formato")
else:
    while len(data)>1:
        somma = 0
        for d in data:
            somma+=int(d)
        data=str(somma)
print("Il tuo numero della vita è: ", somma)