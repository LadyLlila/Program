#(4 de la guía 2) Pedir el ingreso de 10 números. Contar los mayores de 23. Almacenar los que cumplen la condición.  Mostrar los resultados.

datos = [0 for x in range(10)]
for i in range(0, len(datos)):
    datos[i]= int(input("Ingrese número {}: ".format(i+1)))

n = 0
mayores_a_23 = []
for i in range(0, len(datos)):
    if datos[i] > 23:
        n = n + 1
        mayores_a_23.append(datos[i])

print(f"Los números mayores a 23 son {n}, a saber: ")
print(mayores_a_23)
