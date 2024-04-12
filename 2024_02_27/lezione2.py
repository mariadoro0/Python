from time import time
from datetime import date

timestamp=time()            #restituisce il numero di secondi dal 1/01/1970 alla data odierna
print("timestamp: ",timestamp)

d=date.fromtimestamp(timestamp)     #calcolo la data di oggi con timestamp
print("data: ", d)          #stampa la data odierna
print(d.strftime("%d/%m/%Y  %H:%M:%S"))         #stampa data di oggi, ma l'orario è 00:00:00

from datetime import time
t=time(14,53,20,1)      #creo un orario arbitrario
print("orario arbitrario:\n", t)
print("ora arbitraria:\n", t.hour)                      #stampa le singole componenti dell'orario che ho creato
print("minuti arbitrari:\n", t.minute)
print("secondi arbitrari:\n", t.second)
print("microsecondi arbitrari:\n", t.microsecond)

from datetime import datetime
oggi=datetime.today()
print("ora reale:\n", oggi)                         #entrambi i modi stampano l'ora esatta
print("now:\n", datetime.now())

miadata=datetime(2019,3,14)
diff=oggi-miadata
print("Differenza tra ",oggi,"e",miadata,"è:\n", diff)              #per fare operazioni tra date, i formati devono essere uguali (es entrambi datetime, o entrambi date)

import locale
locale.setlocale(locale.LC_ALL, 'italian')                          #serve a settare l'ora locale/data in italiano
