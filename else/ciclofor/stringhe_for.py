#inverte maiuscole con minuscole
st="abc123XYZ"
print(st)
st1=""

for ch in st:
    if ch.isupper():                  #se la lettera è maiuscola:
        ch1=ch.lower()              #converte ch in minuscolo e salva in ch1
        print(ch1, end="")
    elif ch.islower():
        ch1=ch.upper()
        print(ch1, end="")
    else:
        ch1=ch
        print(ch, end="")
    st1+=ch1

print("\nFrase invertita: ", st1)

