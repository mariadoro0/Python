nomi={"paolo","mario","antonio","giacomo"}
alunni={"mario","luigi"}
persone=nomi.union(alunni)
print(persone)
print(alunni.issubset(nomi))
print(nomi.issuperset(alunni))
persone= nomi.difference(alunni)
print(persone)
nomi.clear()
print(nomi)

numeri=set(range(10))
print(numeri)

