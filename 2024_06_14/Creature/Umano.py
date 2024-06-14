class Umano:
    def __init__(self, nome, lingua):
        self._nome = nome               # singolo underscore = protected, ma non protegge effettivamente da classi
        self._lingua = lingua           # esterne e non solo alle sottoclassi


    def come_sei(self):
        return "Ho solo 2 gambe"


    def __str__(self):
        return f"Sono {self._nome} e parlo {self._lingua}"
