#Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad.

import datetime
"""=======|| SINTAXIS y MÉTODOS ||=======
 fechaDeHoy = datetime.datetime.now()
unaFecha = datetime.date(2012, 3, 4)

print(unaFecha)
print(unaFecha.year)
print(unaFecha.month)
print(unaFecha.day)

otraFecha = datetime.date(1992, 4, 29)

dt = datetime.timedelta(100) #Arg en días
print(otraFecha + dt)

print(otraFecha.strftime("%A, %d %b, %Y"))
"""
cant = int(input("Ingrese cantidad de personas a ingresar"))
lista_nombres = [0 for x in range(cant)]
lista_fechas = []
lista_mayores = []
for i in range(cant):
    persona = input("Ingrese nombre de la Persona: ")
    lista_nombres[i] = persona
    dia, mes, anio = int(input("Ingrese día de nacimiento: ")), int(input("Ingrese mes de nacimiento: ")), int(input("Ingrese año de nacimiento: "))
    fecha = datetime.date(anio, mes, dia)
    lista_fechas.append(fecha)
