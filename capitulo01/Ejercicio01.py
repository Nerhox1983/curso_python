#Ejercicio 1.1. Correr tres veces el programa cuad con valores de entrada (3,5), (3,3) y (5,3)
#respectivamente. ¿Qué sucede en cada caso?

#import cuad

def main():
    print ("Se calcularan los cuadrados de números")
    n1 = int(input("Ingrese un numero entero: "))
    n2 = int(input("Ingrese otro numero entero: "))

    for x in range(n1, n2):
        print ("x", x)
        print ("resultado: ", x*x)

    print ("Es todo por ahora")

main()