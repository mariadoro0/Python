from Umano import Umano
from Animale import Animale


class FiguraMitologica(Umano, Animale):
    def __init__(self, nome, lingua, tipo, verso, mito):
        Umano.__init__(self, nome, lingua)
        Animale.__init__(self, tipo, nome, verso)
        self._mito = mito

    def __str__(self):
        return (
            f"Sono metà Uomo e metà {self._tipo}, mi chiamo {self._nome}, parlo {self._lingua}, oppure posso fare {self._verso},"
            f" e appartengo al mito {self._mito}")
