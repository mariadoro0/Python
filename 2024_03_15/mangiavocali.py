#mangiavocali: inserire frase da tastiera, converte in maiuscolo e poi elimina tutte le vocali dalla frase e la stampa

frase=input("Inserire una frase:")
frase=frase.upper()
frase2=""
for let in frase:
    if let in "AEIOU":
        continue
    else:
        frase2+=let
print(frase2)

