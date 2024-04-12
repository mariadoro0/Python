
iban=input("Inserisci l'IBAN per la verifica: ")
if (len(iban)>30 or len(iban)<15):
    raise Exception("Lunghezza non corrispondente")
naz=iban[0:2]
ctrl=iban[0:4]
if not (naz.isalpha()):
    raise Exception("I primi due caratteri devono essere caratteri maiuscoli")
if (naz.islower()):
    naz=naz.upper()
iban=iban[4:]
iban+=ctrl
newiban=""
for char in iban:
    if char.isalpha():
        char=int(ord(char))
        char=char-55
        char=str(char)
    newiban+=char
print(newiban)
newiban=int(newiban)
if (newiban%97==1):
    print("L'iban è valido")
else:
    print("Iban non valido")

