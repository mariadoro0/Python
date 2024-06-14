from Dipendente import Dipendente

class Docente(Dipendente):
    def __init__(self, nome, indirizzo, sesso, disciplina, ruolo):
        Dipendente.__init__(self, nome, indirizzo, sesso)
        self._disciplina = disciplina
        self._ruolo = ruolo

    def get_disciplina(self):
        return self._disciplina
    def get_ruolo(self):
        return self._ruolo
    def set_ruolo(self, ruolo):
        self._ruolo = ruolo
    def set_disciplina(self, disciplina):
        self._disciplina = disciplina

    def __str__(self):
        return Dipendente.__str__(self) + f", Disciplina: {self._disciplina}, Ruolo: {self._ruolo}"

