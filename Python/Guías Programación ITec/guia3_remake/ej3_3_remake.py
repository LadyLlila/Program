#Almacenar en dos listas paralelas, nombres y sexos de 8 personas. Recorrerlas y guardar los nombres de las mujeres en una nueva lista. Mostrar los elementos de la lista resultante.


lista_nombres = ["" for x in range(8)]
lista_sexos = ["" for x in range(8)]
lista_mujeres = []
numMujeres = 0
for i in range(0, len(lista_nombres)):
    nombre = input("Ingrese nombre: ")
    lista_nombres[i] = nombre
    sexo = input(f"Ingrese el sexo (\"M\" o \"F\") de {nombre}: ")
    if (sexo != "M") and (sexo != "F"):
        print("¡Debe ingresar \"F\" o \"M\"!")
        continue    
    lista_sexos[i] = sexo
    if sexo == "F":
        numMujeres += 1
        lista_mujeres.append(nombre)

print(lista_nombres)
print(lista_sexos)
if numMujeres != 0:
    print(f"Cantidad de mujeres: {numMujeres}. Lista de Mujeres:")
    print(lista_mujeres)
else:
    print("No hay mujeres en la lista")