#tipi di variabili Lezione 23/02
#----stringhe------
a="la mia prima stringa, in doppie virgolette"
b='la mia seconda stringa, in virgolette singole'
c="""la mia terza stringa, con triple doppie virgolette. 
Le triple doppie virgolette permettono di scrivere su più righe"""
d='''la mia quarta stringa, con tripli apici
funziona come le triple doppie virgolette'''
print(len(d))

stringa="così metto \'apici\' una frase e \"doppie virgolette\": serve il backslash prima dell'apice/virgoletta"

#---numeri----
x=3
y=5

print("\nHo saltato ",x," volte e fatto ",y," capriole!")        #utilizzo di print per le frasi+numeri
print(c[10:20])                                                  #stampa dal carattere 10 al 19, si dice slice
z=4.1                                                            #per i numeri con la virgola si usa il punto
y="casa"                                                         #y è "diventata" stringa, ma è proprio una variabile diversa
                                                                 #viene proprio eliminata y=5 e creata una nuova y="casa"

i=11234                                                          #numero decimale
d=0O23                                                           #numero ottale
ex=0x123                                                         #numero esadecimale
bn=0b1111101                                                     #numero binario
print(i,d,ex,bn, sep="\t***")                                    #quando si stampa, viene stampato l'equivalente in decimale
                                                                 #sep permette di specificare un separatore
#----booleani---
g=1
print(g==1)                                                     #fa un confronto tra g e 1 e restituisce True o False

print(9/2, 9//2, 9%2, 9**2, sep=" ** ")                         #il // fa la divisione intera, il % da il resto, il ** fa la potenza

#---conversione numeri in stringhe----> funzione str() e operatore +
s="-"+str(g)+"-"                                                #str converte il numero in stringa mentre + permette di aggiungere cose (concatenazione di stringhe)
print(s)
r= int("10")                                                    #conversione della stringa in numero
print(r)

t=int(input("inserisci un numero: "))                           #la funzione input() restituisce caratteri, quindi se si scrivono numeri vanno convertiti con int()
w=float(input("inserisci un numero con la virgola: "))          # se si maneggiano float si usa la funzione float()

a=b*3                                                           #se si moltiplica una stringa, viene ripetuta x volte
print(a)

p="atleta"
print("leta" in p)                                              #l'operatore in vede se quello che c'è a sinistra esiste in quello a destra e restituisce vero o falso
n=(1,2,3)
print(1 in n)                                                   #si può usare anche negli elenchi di numeri

a=10
b=15
x="io sono {} {}".format('mario','rossi')                 #mette i parametri di formati nelle parentesi graffe
print(x)
data="20/04/2022"
eta=25
print(f"data nascita {data}, eta {eta}")                       #altro modo di usare .format
print("data nascita {1} età {0}".format(eta,data))       #si possono ordinare
print("data nascita {d} età {e}".format(e=eta,d=data))         #e rinominare
print("data nascita {0} età {1:2.3f}".format(data,eta))  #si può specificare le cifre significative e decimali


a=10
b="15"
print("sono dirigente da %d anni e %s giorni"%(a,b))          #si può utilizzare la print anche così, usano %prima delle variabili

#----formattazione di testo-----
"""
ARTICOLO        PREZZO  QUANTITA        SCONTO APPLICATO    TOTALE SCONTATO
pomodori        5.25    25              23.46               107,41"""

nome="pomodori"
prezzo=5.25
quant=25
sc=23.46
tot=prezzo*quant
txt="{:<20} {:<7} {:<10} {:<18} {:<6}"                        #formattazione dei caratteri: vengono specificati gli spazi, txt funge da "modello"
print("\n")
print(txt.format("ARTICOLO","PREZZO","QUANTITA","SCONTO APPLICATO","TOTALE SCONTATO"))  #usando il formato txt con gli spazi inseriti il risultato è simile ad una tabella
print(txt.format(nome, prezzo, quant, sc, tot))


#---scambio variabili---
n1=int(input("Inserisci il primo numero: "))
n2=int(input("Inserisci secondo numero: "))
print("i due numeri sono: %d e %d"%(n1,n2))                  #posso scrivere anche print("i due numeri sono: ",n1, "e", n2)

#n3=n1                                                       in C viene usata una terza variabile per fare lo scambio
#n1=n2                                                       per non perdere nessun valore
#n2=n3
#print("i due numeri scambiati sono: %d e %d"%(n1,n2))

n1,n2=n2,n1
print("i due numeri sono: %d e %d"%(n1,n2))
print(type(n1))                                             #la funzione type dice il tipo di variabile (in questo caso int)
print(type(n1)==int)                                        #fa il confronto tra il tipo di n1 e int e restituisce true o false

#---funzioni di print--->media di temperature
t1=float(input("Temperatura 1: "))
t2=float(input("Temperatura 2: "))
t3=float(input("Temperatura 3: "))
t4=float(input("Temperatura 4: "))
media=(t1+t2+t3+t4)/4
list=[t1,t2,t3,t4]                                         #creazione di una lista
print(media)
import numpy                                               #importo libreria numerica
#print(numpy.sum(t1,t2,t3,t4)/numpy.len(t1,t2,t3,t4))      per usare numpy si usano le liste
print(numpy.mean(list))                                    #installare libreria da terminale->file->setting->interprete->installa pacchetto
print(sum(list)/len(list))
import statistics
print(statistics.mean(list))

#---date---
from datetime import date
oggi=date.today()                                       #funzione per data odierna
print("oggi: ", oggi)
print("anno: ", oggi.year)
print("mese: ", oggi.month)
print("giorno: ", oggi.day)

miadata=date(2019,3,24)                #di default anno/mese/giorno
print(miadata)
print(miadata.strftime("%d/%m/%Y %H:%M:%S"))           #formattazione dd/mm/yyyy hh:mm:ss

import calendar
print(calendar.calendar(2024))                         #crea il calendario formattato di un anno a scelta






