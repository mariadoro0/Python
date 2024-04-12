#p1,p2,p3,p4,p5=7,2,4,3,6
p1,p2,p3,p4,p5=8,9,9,4,7

it1=[p1,p2]
min1=min(it1)
print("Massimo trasportabile nel primo itinerario:",min1,"tonnellate")

it2=[p1,p3,p4]
min2=min(it2)
print("Massimo trasportabile nel secondo itinerario:",min2,"tonnellate")

it3=[p1,p5]
min3=min(it3)
print("Massimo trasportabile nel terzo itinerario:",min3,"tonnellate")


if(min(it1)==max(min1,min2,min3)):
    print("\nL'itinerario più conveniente è il numero 1")
else:
    if(min(it2)==max(min1,min2,min3)):
        print("\nL'itinerario più conveniente è il numero 2")
    else:
        if (min(it3)==max(min1,min2,min3)):
            print("\nL'itinerario più conveniente è il numero 3")
