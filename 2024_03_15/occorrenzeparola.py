testo=input("Inserire un testo: ")
parola=input("Inserire parola da trovare: ")
start=0
cnt=0
for x in testo:
    pos=testo.find(parola, start)
    if pos!=-1:
        start=pos+len(parola)
        cnt+=1
if cnt>0:
    print("La parola <",parola,"> è contenuta nel testo",cnt,"volte")
else:
    print("La parola <",parola,"> non è contenuta nel testo.")