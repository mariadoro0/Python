from funzioni import funzioni


def litri_100km_to_miglia_galloni(litri):
    #gallons=litri/3.785411784
    #miles=100*1000/1609.344
    #return miles/gallons
    lpergallon=3.785411784
    kmpermile=1.609344
    kmallitro=100/litri
    kmalgallone=kmallitro*lpergallon
    milespergallon=kmalgallone/kmpermile
    return milespergallon


def miglia_gallone_to_litri_100km(mpg):
    #km100=miles*1609.344/1000/100
    #litres=3.785411784
    #return litres/km100
    lpergallon = 3.785411784
    kmpermile = 1.609344
    gallonper100=100/mpg
    gper100km=gallonper100/kmpermile
    litriper100km = gper100km*lpergallon
    return litriper100km


def main():
    c=input("Vuoi convertire litri o galloni? Inserisci l o g: ")
    if c=='l':
        litri=float(input("Inserisci il valore l/100km: "))
        consumo=litri_100km_to_miglia_galloni(litri)
        print("Conversione da l/100km a mpg: ", consumo)

    elif c=='g':
        mpg=float(input("Inserisci il valore mpg: "))
        consumo=miglia_gallone_to_litri_100km(mpg)
        print("Conversione da mpg a l/100km: ", consumo)



main()