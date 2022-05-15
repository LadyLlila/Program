#Ingresar nombres en una lista, luego buscar un nombre y de encontrarlo decir en qué posición está.

lista_nombres = []

nombre = input("\nIngresar nombre (0 para finalizar): ")

while (nombre != "0"):
    lista_nombres.append(nombre)
    nombre = input("\nIngresar nombre (0 para finalizar): ")

print("\n -------- LISTA COMPLETA -----------\n")

nombre = input("Ingrese un nombre para encontrar su posición en la lista: ")

if nombre in lista_nombres:
    print("El nombre se encuentra en la posición: " + str(lista_nombres.index(nombre)))
else:
    print("Nombre no encontrado.")