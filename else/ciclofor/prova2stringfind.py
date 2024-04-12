#w="dog"
#st="xxxdxxxoxxxgxx"
#str="vcxzxdcybfdstbywuefsas"
w=input("Inserire la parola da cercare: ")
st=input("Inserire la frase: ")


cnt=0
start=0
pos=[0 for z in range(0,len(w))]
#for i in range (0, len(w)):
for l in w:
        f=st.find(l, start)
        if f!=-1:
            pos[cnt]=f
            cnt=cnt+1
            start=f
            #if i!=len(w) and cnt!=len(w):
            if cnt!=len(w):
                continue
            else:
                print("La parola si trova nella stringa")
                for j in range(0,cnt):
                    print("Lettera",w[j]," trovata in posizione ", int(pos[j]))

if f==-1:
    print("La parola non si trova nella stringa")