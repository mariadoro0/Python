#+39 prefisso-10 numeri
telefono = '+392574856985' # True
#telefono = '395851256954' # False (manca il '+')
#telefono = '++7485125874' # False (manca il prefisso)
#telefono = '+39333457Ciao' # False (mi pare ovvio :D )
#telefono = "+3912" # False (troppo corto)
#telefono = '+393481489945' # True

pre=telefono[0:2]
num=telefono[3:11]
nopiu=telefono[1:9]

dig=nopiu.isdigit()
if(pre=='+39'):
    preval=True
plus=telefono.startswith('+')
if(len(num)!=10 || dig==False)

