def OrdenarDosNumerosAscendentemente(numero1, numero2):
    auxiliar = 0
    if numero1>numero2:
        auxiliar = numero2
        numero2 = numero1
        numero1 = auxiliar
        print ("numero1=> ", numero1)
        print ("numero2=> ", numero2)
        print ("auxiliar=> ", auxiliar)

def CalcularReto0201PuntoA(a, b, c):
    return ((b * b) - (4 * a * c)) / (2 * a),

def CalcularReto0201PuntoB(a, b, c):
    return (b * b - 4 * a * c) / (2 * a),

def CalcularReto0201PuntoC(a, b, c):
    return b * b - 4 * a * c / 2 * a,