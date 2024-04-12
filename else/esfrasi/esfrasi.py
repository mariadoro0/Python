def main():
    i=1
    frase=""
    while i!=0:
        frasetemp=input("Inserire una frase: ")
        frase=frase+" "+frasetemp
        i=int(input("Inserisci 0 per terminare o 1 per continuare"))

    print(frase)



main()