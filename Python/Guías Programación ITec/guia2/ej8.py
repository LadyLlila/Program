#Ingresar autos y sus precios y contar cuantos valen entre $1.460.000 y $2.850.000. Terminar la carga cuando el valor ingresado sea $0.

precio = int(input("Ingrese precio de vehículo: $"))

cantidad_autos = 0
while (precio != 0):
    if (1460000 < precio < 2850000):
        cantidad_autos = cantidad_autos +1
    precio = int(input("Ingrese precio de vehículo: $"))

print("\nLa cantidad de autos que valen entre $1460k y $2850k es de: " + str(cantidad_autos))
