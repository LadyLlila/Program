#Guardar en una lista los números pares mayores que 0 y menores que 31. 

import random

lista_numeros = []

i= 0
n=0
while i < 30:
    i = i + 2
    lista_numeros.append(i)
    n += 1  #Por curiosidad nomás
    
print(lista_numeros)
print (n)