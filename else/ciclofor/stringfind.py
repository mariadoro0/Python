"""w="dog"
st="xxxdxxxoxxxgxx"
#str="vcxzxdcybfdstbywuefsas"

i=0
cnt=0
pos=""
for i in range (0, len(w)):
        f=st.find(w[i])
        if f!=-1:
            pos+=str(f)
            cnt=cnt+1
            if i!=len(w) and cnt!=len(w):
                continue
            else:
                print("La parola si trova nella stringa")
                for j in range(0,cnt):
                    print("Lettera",w[j]," trovata in posizione ", int(pos[j]))

if f==-1:
    print("La parola non si trova nella stringa")"""


w=input("inserire una parola da cercare: ")
st=input("inserire la frase: ")
found=True
start=0
for ch in w:
    pos=st.find(ch,start)
    if(pos<0):
        found=False
        break
    start=pos+1
if found==False:
    print("parola non trovata")
else:
    print("la parola si trova nella frase")