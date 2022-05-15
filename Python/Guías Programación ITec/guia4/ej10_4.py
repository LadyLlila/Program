#Determinar cuál es la vocal que aparece con mayor frecuencia.
s = "Quiero comer manzanas, solamente manzanas."

# s = s.replace(",", "")
# s = s.replace(".", "")
# lista_s = s.split()
s.lower()
# cantidad_a = s.count("a")
# cantidad_e = s.count("e")
# cantidad_i = s.count("i")
# cantidad_o = s.count("o")
# cantidad_u = s.count("u")

lista_cantidades = [s.count("a"), s.count("e"), s.count("i"), s.count("o"), s.count("u")]
lista_vocales = ["a", "e", "i", "o", "u"]
cantidad_mayor = 0
for i in range(len(lista_cantidades)):
    if lista_cantidades[i] > cantidad_mayor:
        cantidad_mayor = lista_cantidades[i]

if lista_cantidades.index(cantidad_mayor) == 0:
    print("La vocal que aparece con mayor frecuencia es: a")
elif lista_cantidades.index(cantidad_mayor) == 1:
    print("La vocal que aparece con mayor frecuencia es: e")
elif lista_cantidades.index(cantidad_mayor) == 2:
    print("La vocal que aparece con mayor frecuencia es: i")
elif lista_cantidades.index(cantidad_mayor) == 3:
    print("La vocal que aparece con mayor frecuencia es: o")
elif lista_cantidades.index(cantidad_mayor) == 4:
    print("La vocal que aparece con mayor frecuencia es: u")

for i in range(len(lista_cantidades)):
    print(lista_vocales[i] + " = " + str(lista_cantidades[i]) + " veces.")