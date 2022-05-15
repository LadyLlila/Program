#Pedir nombres y sexo de personas y mostrar el total de mujeres y el nombre de cada una.

cantidad_personas = int(input("\n¿Cuántas personas se van a cargar? "))

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