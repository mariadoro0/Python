from platform import platform,machine,processor,system,version
# libreria di python per accedere alle informazioni della macchina

print("piattaforma: ", platform())
print("macchina: ", machine())
print("processore: ", processor())
print("sistema: ", system())
print("versione: ", version())

from platform import python_implementation, python_version_tuple
print("Versione py: ", python_implementation())
print(python_version_tuple())

import os
curr_dir=os.getcwd()
#dice la directory corrente
print(curr_dir)
# stampa di tutte le sottocartelle della cartella corrente
for nome in os.listdir():
    print(nome)

# crea una nuova cartella come su bash
# os.mkdir("nuovacartella")

#lista delle sottocartelle
lst=os.listdir()
print(lst)