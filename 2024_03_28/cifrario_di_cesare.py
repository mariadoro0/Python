#cifrario di cesare: le lettere vengono traslate per crittografare il messaggio
txt=input("Inserisci un testo da crifrare:")
cifrario=''

for char in txt:
        code=ord(char)+1                #ord converte il carattere i ASCII
        cifrario+=chr(code)             #chr converte l'ASCII in carattere

print("Testo cifrato:\n",cifrario)

decif=''
for char in cifrario:
        code=ord(char)-1
        decif+=chr(code)
print("Testo originale:\n", decif)