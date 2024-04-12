from datetime import datetime

while True:
    stdata=input("inserisci una data(gg/mm/aaaa): ")
    try:
        d=datetime.strptime(stdata,'%d/%m/%Y')
        break
    except:
        print("Errore, data non valida")

print("Hai inserito: ", d)