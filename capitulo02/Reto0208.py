#Ejercicio 2.8. Escribir un programa que use un ciclo definido con rango numérico, que averigue
#a cuántos amigos quieren saludar, les pregunte los nombres de esos amigos/as, y los salude.
numeroMejoresAmigos = int(input ("Cuantos mejores amigos tienes?: "))

for miMejorAmigoActual in range (1,numeroMejoresAmigos):
    miMejorAmigo = input ("Dame el nombre de uno de tus mejores amigos: ")
    print ("Hola ", miMejorAmigo)