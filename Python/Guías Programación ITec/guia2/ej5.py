#Pedir los montos de sueldos de los empleados de una empresa hasta que no haya más y mostrar el total.


cantidad_Sueldos = int(input("\n¿Cuántos sueldos se debe sumar?: "))
sueldos = [0 for x in range(cantidad_Sueldos)]


for i in range(0, len(sueldos)):
    sueldos[i] = int(input("\nIngrese el sueldo {}: " .format(i+1)))

res=0
for i in range(0, len(sueldos)):
    res = sueldos[i] + res
    i = i + 1

print("\nEl total a pagar es de: " + str(res))