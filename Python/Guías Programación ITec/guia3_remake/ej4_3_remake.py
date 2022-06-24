#Dada una lista con números, crear otra con los cuadrados de esos valores. 

import random

cant = int(input("Ingrese cantidad de números deseada: "))
lista_numeros = [0 for x in range(cant)]
lista_cuadrados = [0 for x in range(cant)]

for i in range(0, len(lista_numeros)):
    numero = random.randrange(-9,9)
    lista_numeros[i] = numero
    cuadrado = numero**2
    lista_cuadrados[i] = cuadrado

print(lista_numeros, lista_cuadrados, sep="\n")