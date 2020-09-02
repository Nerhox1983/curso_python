1 #!/usr/bin/env python
2 """ Un programa sencillo, para calcular cuadrados de números """
3
4 def main():
5 print "Se calcularán cuadrados de números"
6
7 n1 = input("Ingrese un número entero: ")
8 n2 = input("Ingrese otro número entero: ")
9
10 for x in range(n1, n2):
11 print x*x
12
13 print "Es todo por ahora"
14
15 main()