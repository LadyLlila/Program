#Cargar en dos listas paralelas nombres y sueldos. Luego mostrar los nombres de las personas que ganan más de $85000.

lista_nombres = []
lista_sueldos = []

nombre = ''
sueldo = ''
while (nombre != "0"):
    nombre = input("Ingrese nombre (0 para finalizar): ")
    lista_nombres.append(nombre)

for i in range(len(lista_nombres)-1):
    sueldo = int(input("Ingrese sueldo de " + lista_nombres[i] + ": $"))
    lista_sueldos.append(sueldo)

print("\nPersonas que ganan más de $85000:")
for i in range(len(lista_sueldos)):
    if lista_sueldos[i] > 85000:
        print(lista_nombres[i])

        