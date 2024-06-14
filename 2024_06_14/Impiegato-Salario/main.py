from Impiegato import Impiegato
from Salario import Salario


def main():
    i = Impiegato("Maria", 24, 2500,130)

    print(i)

    print("\n"+str(i.get_miosalario()))

    print("\n"+str(i.tot_sal()))


main()