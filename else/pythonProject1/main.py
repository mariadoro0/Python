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

