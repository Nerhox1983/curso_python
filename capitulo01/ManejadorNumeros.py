def OrdenarDosNumerosAscendentemente(numero1, numero2):
    auxiliar = 0
    if numero1>numero2:
        auxiliar = numero2
        numero2 = numero1
        numero1 = auxiliar
        print ("numero1=> ", numero1)
        print ("numero2=> ", numero2)
        print ("auxiliar=> ", auxiliar)