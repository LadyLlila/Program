#Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad.
from datetime import *

lista_nombres = []
fechas_nacimiento = []

nombre = input("Insertar nombre (0 para cancelar): ")
while (nombre != "0"):
    lista_nombres.append(nombre)
    
    anio = int(input(f'Ingrese año de nacimiento de {nombre}: '))
    mes = input(f'Ingrese mes de nacimiento de {nombre}: ')
    dia = int(input(f'Ingrese día de nacimiento de {nombre}: '))
    nombre = input("Insertar nombre (0 para cancelar): ")
    fechas_nacimiento.append([{anio}, {mes}, {dia}])

#----------|| PROBLEMAS ||-------------------
for i in range(len(lista_nombres)):
    print(f"{lista_nombres[i]} nació el {dia} de {mes} del {anio}")

#fecha = datetime.date(anio, mes, dia)