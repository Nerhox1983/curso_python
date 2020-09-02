#Ejercicio 1.2. Insertar instrucciones de depuración que permitan ver el valor asociado con la
#variable x en el cuerpo del ciclo for y después que se sale de tal ciclo. Volver a correr tres veces
#el programa cuad con valores de entrada (3,5), (3,3) y (5,3) respectivamente, y explicar lo que
#sucede.

    auxiliar = 0

    if n1>n2:
        auxiliar = n2
        n2 = n1
        n1 = auxiliar
        print ("n1=> ", n1)
        print ("n2=> ", n2)
        print ("auxiliar=> ", auxiliar)

    for x in range(n1, n2):
        print ("x", x)
        print ("resultado: ", x*x)
    
    print ("Es todo por ahora")