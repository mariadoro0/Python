class Dipendente:
    def __init__(self, nome, indirizzo, sesso):
        self._nome = nome
        self._indirizzo = indirizzo
        self._sesso = sesso

    def get_nome(self):
        return self._nome
    def get_indirizzo(self):
        return self._indirizzo
    def get_sesso(self):
        return self._sesso
    def set_nome(self, nome):
        self._nome = nome
    def set_indirizzo(self, indirizzo):
        self._indirizzo = indirizzo
    def set_sesso(self, sesso):
        self._sesso = sesso

    def __str__(self):
        return f'Nome: {self._nome}, Indirizzo: {self._indirizzo}, Sesso: {self._sesso}'