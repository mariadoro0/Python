"""questo programma ha un errore, ma se inserisco solo valor positivi termina senza errori
quando si fa il test del codice si devono testare tutti i possibili casi per essere sicuri che il programma non abbia errori"""

temperature=float(input("Inserisci la temperatura: "))
if (temperature>0):
    print("temperatura sopra lo 0")
elif temperature<0:
    print("temperatura sotto zero, che freddo!")
else:
    print("la temperatura è 0")

#il codice così non va bene perchè non c'è controllo sull'input