class Animale:
    def __init__(self, tipo, nome, verso):
        self._tipo = tipo
        self._nome = nome
        self._verso = verso

    def come_sei(self):
        return "Ho solo 4 gambe"

    def __str__(self):
        return f"Sono un {self._tipo} di nome {self._nome} e faccio {self._verso}"