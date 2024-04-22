numeri_giocati=[3,7,11,47,34,49]
estrazione=[3,7,11,9,42,49]
giusti=0
for n in numeri_giocati:
    if n in estrazione:
        giusti += 1

print("numeri centrati=",giusti)