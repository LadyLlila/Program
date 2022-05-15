#Pedir los montos de sueldos de los empleados de una empresa hasta que no haya más y mostrar el total.

sueldo = int(input("\nIngrese sueldo: "))
respuesta = input("\n¿Ingresar más? [s/n] ")
while respuesta == 's':
    sueldo2 = int(input("\nIngrese sueldo: "))
    sueldo = sueldo + sueldo2
    respuesta = input("\n¿Ingresar más? [s/n] ")

print("Total a pagar: " + str(sueldo))