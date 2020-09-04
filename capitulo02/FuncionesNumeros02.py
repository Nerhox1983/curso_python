Numero1= 1
Numero2= 2
Numero4= 4

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
    return ((b * b) - (Numero4 * a * c)) / (Numero2 * a),

def CalcularReto0201PuntoB(a, b, c):
    return (b * b - Numero4 * a * c) / (Numero4 * a),

def CalcularReto0201PuntoC(a, b, c):
    return b * b - Numero4 * a * c / Numero2 * a,

def CalcularReto0201PuntoD(a, b, c):
    return (b * b) - (Numero4 * a * c / Numero2 * a)

def CalcularReto0201PuntoE(b):
    return Numero1 / Numero2 * b

def CalcularReto0201PuntoF(b):
    return b / Numero2