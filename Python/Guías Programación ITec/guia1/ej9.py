#Nombre de alumno: Leonardo Roman Leonhardt
#Realizar un algoritmo que permita ingresar un dato numérico y determinar si es un número positivo de dos dígitos.

numero = int(input("\n Ingrese un número entero: "))

if numero > 0:
    if len(str(numero)) == 2:
        print("\nEl número es positivo de dos dígitos.\n")
    else:
        print("\nEl número es positivo, pero no tiene dos dígitos.\n")
else:
    if len(str(numero))-1 == 2:
        print("\nEl número es no positivo de dos dígitos.\n")
    else:
        print("\nEl número es no positivo y no tiene dos dígitos.\n")