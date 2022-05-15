#Pedir el ingreso de 10 números. Contar los mayores de 23. Mostrar el resultado.

datos = [0 for x in range(10)]
for i in range(0,len(datos)):
    datos[i] = int( input( "Ingrese número {}: ".format(i+1) ))

print ("Los números mayores que 23 son: ")
for i in range(0, len(datos)):
    if datos[i] > 23:
        print( datos[i], end= ' ')

cantidad_Numeros = 0
for i in range(0, len(datos)):
    if datos[i] > 23:
        cantidad_Numeros = cantidad_Numeros + 1
print("\nLa cantidad de números mayores a 23 es: " + str(cantidad_Numeros))