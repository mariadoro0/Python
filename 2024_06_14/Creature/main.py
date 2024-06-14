from Animale import Animale
from FiguraMitologica import FiguraMitologica
from Umano import Umano


def main():
    u1 = Umano("Franco", "francese")
    u2 = Umano("Mauro", "italiano")
    u3 = Umano("Santiago", "portoghese")
    a1 = Animale("toro", "Paolo","muuuuuu")
    a2 = Animale("cane","Principessa","bau bau")
    a3 = Animale("leone","Leopoldo","roar")

    fm1 = FiguraMitologica("centauro", "giargianese", "cavallo", "hihihihi","greca")
    print(fm1)

main()