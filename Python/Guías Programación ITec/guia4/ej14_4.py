#Pedir dos nombres y edades respectivas y luego construir una sola cadena con un texto que muestre el nombre #del mayor y cuanto le lleva al menor.
#(Ejemplo:  entrada -> 'Juan' 30 'Pedro' 23 / salida -> 'Juan le lleva 7 años a Pedro')

lista_nombres = []
lista_edades = []

for i in range(2):
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad de "+ nombre +":"))
    lista_nombres.append(nombre)
    lista_edades.append(edad)

# mayor=0
# for i in lista_edades:
#     if lista_edades[i] > mayor:
#         mayor = lista_edades[i]
lista_edades.sort()

diferencia = lista_edades[1] - lista_edades[0]

print(lista_nombres[0] + " le lleva " + str(diferencia) + " años a " + lista_nombres[1])