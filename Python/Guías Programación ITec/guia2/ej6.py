#Preguntar cuántas personas se van a cargar y luego solicitar sus edades, mostrando al final la edad promedio.

cantidad_personas = int(input("¿Cuántas personas se van a cargar? "))

edades = [0 for x in range(cantidad_personas)]
for i in range(0,len(edades)):
    edades[i] = int( input( "Ingrese edad {}: ".format(i+1) ))

suma_edades = 0
for i in range(0, len(edades)):
    suma_edades = suma_edades + edades[i]
    i = i + 1

promedio = suma_edades / cantidad_personas

print("El promedio de edades es de " + str(promedio) + " años.")