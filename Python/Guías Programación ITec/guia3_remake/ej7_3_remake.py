#Dada una lista cargada con 7 números enteros, obtener el promedio. Mostrar por pantalla dicho promedio y los números de la lista que sean mayores que él.

lista_numeros = [0 for x in range(7)]
suma = 0
for i in range(0, len(lista_numeros)):
    lista_numeros[i] = int(input("Ingrese un número entero: "))
    suma = suma + lista_numeros[i]

prom = suma/7
print(f"El promedio es de {prom} y los números mayores que él son: ")
for i in range(0, len(lista_numeros)):
    if lista_numeros[i] > prom:
        print(lista_numeros[i], end=" ")

