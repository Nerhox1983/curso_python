#!/usr/bin/env python
#Un programa sencillo, para calcular cuadrados de números
def main():
    print ("Se calcularán cuadrados de números")

n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número entero: "))

for x in range(n1, n2):
    print (x*x)

print ("Es todo por ahora")

main()