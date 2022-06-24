#Cargar en dos listas paralelas nombres y sueldos. Luego mostrar los nombres de las personas que ganan más de $85000.

cant = int(input("Ingrese la cantidad de nombres y sueldos a cargar: "))
lista_nombres = ["" for x in range(cant)]
lista_sueldos = [0 for x in range(cant)]
for i in range(cant):
    nombre = input("Ingrese nombre: ")
    lista_nombres[i] = nombre
    sueldo = int(input(f"Ingrese sueldo de {nombre}: "))
    lista_sueldos[i] = sueldo

print(lista_nombres, lista_sueldos, end="\n")
print("Quienes tienen un sueldo mayor a $85000: ")
for i in range(cant):
    if lista_sueldos[i] > 85000:
        print(lista_nombres[i])