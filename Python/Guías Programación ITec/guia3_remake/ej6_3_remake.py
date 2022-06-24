#Ingresar nombres en una lista, luego buscar un nombre y de encontrarlo decir en qué posición está.


cant = int(input("¿Cuántos nombres quiere ingresar? -> "))
lista_nombres = ["" for x in range(cant)]

for i in range(len(lista_nombres)):
    nombre = input("Ingrese un nombre: ")
    lista_nombres[i] = nombre

print(lista_nombres)

#====|| Buscar nombre y posición ||=======
nombreBuscado = input("Ingrese un nombre a buscar: ")
for i in range(len(lista_nombres)):
    if nombreBuscado == lista_nombres[i]:
        posicion = i
        print(f"El nombre {nombreBuscado} se encuentra en la posición {posicion}")
if nombreBuscado not in lista_nombres:
    print("El nombre buscado no se encuentra en la lista")