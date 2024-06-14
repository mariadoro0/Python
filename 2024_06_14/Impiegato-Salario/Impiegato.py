from Salario import Salario


class Impiegato:
    def __init__(self, nome, eta, stipendio, bonus):
        self.__nome = nome
        self.__eta = eta
        self.__bonus = stipendio
        self.__stipendio = bonus
        self.__miosalario = Salario(self.__stipendio, self.__bonus)

    def set_nome(self, nome):
        self.__nome = nome

    def set_eta(self, eta):
        self.__eta = eta

    def get_nome(self):
        return self.__nome

    def get_eta(self):
        return self.__eta

    def get_miosalario(self):
        return self.__miosalario

    def tot_sal(self):
        return self.__miosalario.stipendio_annuale()

    def __str__(self):
        return f"Nome: {self.__nome}, Eta: {self.__eta}, {self.__miosalario}"
