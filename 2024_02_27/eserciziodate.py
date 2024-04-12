from datetime import datetime
mydate=datetime(2020,11,4,14,53,0)
print(mydate.strftime("%d/%m/%Y %H:%M:%S"))
print(mydate.strftime("%d/%B/%Y  %H:%M:%S"))
print(mydate.strftime("%A %Y %b %d"))
print(mydate.strftime("%A %d %B %Y"))
print(mydate.strftime("Giorno feriale: %w"))
print(mydate.strftime("Giorno dell'anno: %j"))
print(mydate.strftime("Numero della settimana dell'anno: %W"))
