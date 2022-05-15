#Dada una lista cargada con 7 números enteros, obtener el promedio. Mostrar por pantalla dicho promedio y los números de la lista que sean mayores que él.

lista_numeros = [0 for x in range(7)]

print("A continuación, se calculará el promedio de siete números")

# numero = int(input("\nIngresar número: "))
for i in range(len(lista_numeros)):
    lista_numeros[i] = int(input("\nIngresar número: "))



suma=0
for i in range(len(lista_numeros)):
    suma = suma + lista_numeros[i]

res = suma / len(lista_numeros)

print("\nEl promedio es: " + str(res))
