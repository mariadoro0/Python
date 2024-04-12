import datetime
oggi=datetime.date.today()

print("Inserisci il giorno e il mese del compleanno: \n")
gg=int(input("Giorno:"))
mm=int(input("mese:"))

bd=datetime.date(oggi.year, mm, gg)         #data del compleanno con anno attuale
if (bd<oggi):
    bd=bd.replace(year=oggi.year+1)             #se il compleanno è gia passato, aggiungo un anno al prossimo
left=bd-oggi                                    #la differenza tra due date è un'altra data
print("Giorni che mancano al tuo compleanno: ", left.days)


