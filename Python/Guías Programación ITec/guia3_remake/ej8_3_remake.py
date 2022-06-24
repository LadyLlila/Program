#Cargar una lista con números. Invertir los elementos sin usar otra lista. 
import random
cant = int(input("Ingrese cantidad de números: "))
lista_numeros = [0 for x in range(cant)]

for i in range(0, len(lista_numeros)):
    numero = str(random.randrange(0,30))
    lista_numeros[i] = numero

print(lista_numeros)
for i in range(cant):
    print(lista_numeros[-(i+1)], end=" ")