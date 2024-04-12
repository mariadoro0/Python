from funzioni import input_gen
import numpy


def conversione_imperiale(h, p):
    kg = p * 0.453592
    m = h * 0.3048
    return kg, m


def calcolo_bmi(h, p):
    bmi = p / (h * h)
    return bmi


def bmi_case(bmi):
    sit = ""
    if bmi < 16.5:
        sit += "Sottopeso severo"
    elif bmi in numpy.arange(16.5, 18.4, 0.1):
        sit += "Sottopeso"
    elif 18.5 <= bmi <= 24.9:
        sit += "Normale"
    elif bmi in range(25, 30):
        sit += "Sovrappeso"
    elif 30.1 <= bmi <= 34.9:
        sit += "Obesità di primo grado"
    elif bmi in range(35, 40):
        sit += "Obesità di secondo grado"
    elif bmi > 40:
        sit += "Obesità di terzo grado"

    return sit


def main():
    while True:
        try:
            misura = input_gen("Misure in sistema metrico o imperiale? Inserisci 'I' o 'M': ", str)
            if misura.isdigit() or (misura != "I" and misura != "M"):
                raise Exception("Valore inserito non valido")
            break
        except Exception as error:
            print(error)

    h = float(input("Inserire altezza: "))
    if h not in range(3, 220):
        print("Altezza non valida.")
    p = float(input("Inserire peso: "))
    if p not in range(10, 400):
        print("Peso non valido.")

    if misura == "I":
        p, h = conversione_imperiale(h, p)
    else:
        h = h / 100

    print("Valori inseriti: altezza=", h, " metri,  peso=", p, " kg.")

    bmi = calcolo_bmi(h, p)
    sit = bmi_case(bmi)
    print("Il BMI è: ", bmi, ".\nSituazione: " + sit)


main()
