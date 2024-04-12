#ad una scadenza mancano 5000 minuti, scrivere un programma che indica la scadenza in giorni ore minuti
from datetime import datetime
from datetime import timedelta
now=datetime.now()
print(now)
sc=now+timedelta(minutes=5000)
print(sc)


print(timedelta(minutes=5000))  #modo1

score=5000//60          #modo2
scgiorni=score//24
scmin=5000%60
score1=score%24
print("Mancano:",scgiorni,"giorni,",score1,"ore e",scmin,"minuti")



