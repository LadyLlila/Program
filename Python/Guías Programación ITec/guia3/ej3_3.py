#Almacenar en dos listas paralelas, nombres y sexos de 8 personas. Recorrerlas y guardar los nombres de las mujeres en una nueva lista. Mostrar los elementos de la lista resultante.

cantidad_personas = 8

lista_nombres = [0 for x in range(cantidad_personas)]
lista_sexos = [0 for x in range(cantidad_personas)]

for i in range(cantidad_personas):
    lista_nombres[i] = input("\nIngrese nombre: ")
    lista_sexos[i] = input("\nIngrese sexo de " + lista_nombres[i] + " [m/f]: ")

total_mujeres = 0
for i in range(cantidad_personas):
    if lista_sexos[i] == 'f':
        total_mujeres = total_mujeres + 1

print("El total de mujeres es de " + str(total_mujeres) + " y es/son: ")
for i in range(cantidad_personas):
    if lista_sexos[i] == 'f':
        print (lista_nombres[i], end="\n")