#menu con match case
import os  #operative system, permette di utilizzare funzioni del sistema operativo
scelta=-1
while scelta!=0:
    print("----------------")
    print("1. Operazione 1")
    print("2. Operazione 2")
    print("3. Operazione 3")
    print("4. Operazione 4")
    print("0. Operazione 0")
    print("----------------")
    try:
        scelta=int(input("scegli: "))                       #prova a fare ciò che sta nel try, se non riesce va a except
    except:
        print("\tValore non valido, riprova")
        scelta=None                                         #None sarebbe NULL

    match scelta:
        case 0:
            print("Operazione 0: terminazione")
        case 1:
            pass                            #pass si usa per non fare operazioni
        case 2:
            print("Operazione 2!")
        case 3:
            print("Operazione 3!")
        case 4:
            print("Operazione 4!")
        case _:                             #per tutti gli altri numeri, quindi non validi in questo caso
            print("Scelta errata.")

    input("Premi un tasto per continuare")
    os.system('cls')                        #ripulisce lo schermo, è una funzione del sistema operativo
