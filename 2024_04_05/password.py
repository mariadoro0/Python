import funzioni


def codifica_Cesare():
    while True:
        try:
            mex = funzioni.input_gen("Inserisci una frase da codificare: ", str)
            mex = mex.upper()
            pw = funzioni.input_gen("Inserisci una password: ", str)
            pw = pw.upper()
            # if mex.isdigit() or pw.isdigit():
            # raise Exception("Devi inserire solo caratteri.")
            if len(mex) < len(pw):
                raise Exception("La password non può essere più lunga della frase")
            else:
                break
        except Exception as error:
            print(error)

    cnt = 0
    parallel = []
    for i in range(len(mex)):
        if cnt >= len(pw):
            cnt = 0
        parallel.append(pw[cnt])
        cnt += 1
        """ if(len(mex)>len(pw):
                for i in range(len(mex)-len(pw)):
                    password+=password[i]
                     copia la password per la lunghezza del mex """

    codemex = ""
    for i in range(len(mex)):
        codemex += chr((ord(mex[i]) + ord(parallel[i]) - 64))

    return codemex


def decodifica_Cesare():
    while True:
        try:
            mex = funzioni.input_gen("Inserisci una frase da decodificare: ", str)
            mex=mex.upper()
            pw = funzioni.input_gen("Inserisci una password: ", str)
            pw = pw.upper()
            # if mex.isdigit() or pw.isdigit():
            # raise Exception("Devi inserire solo caratteri.")
            if len(mex) < len(pw):
                raise Exception("La password non può essere più lunga della frase")
            else:
                break
        except Exception as error:
            print(error)

    cnt = 0
    parallel = []
    for i in range(len(mex)):
        if cnt >= len(pw):
            cnt = 0
        parallel.append(pw[cnt])
        cnt += 1

    codemex = ""
    for i in range(len(mex)):
        codemex += chr((ord(mex[i]) - ord(parallel[i]) + 64))

    return codemex


def main():
    global mode
    while True:
        try:
            mode = funzioni.input_gen("Vuoi cifrare o decifrare? Inserisci C o D: ", str)
            if mode != "C" and mode != "D":
                raise Exception("Input non valido")
            else:
                break
        except Exception as error:
            print(error)

    if mode == 'C':
        mex = codifica_Cesare()
        print("Il messaggio codificato è: ", mex)
    else:
        mex = decodifica_Cesare()
        print("Il messaggio decodificato è: ", mex)


main()
