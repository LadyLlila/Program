##Nombre de alumno: Leonardo Roman Leonhardt
#Leer dos números y luego una opción (puede ser '+' o '-'), y según la opción elegida realizar el cálculo.

num1 = float(input("\n Inserte primer número: "))
num2 = float(input("\n Inserte segundo número: "))

opcion = input("\n Inserte \" + \" ó \" - \" para realizar una operación entre el primer y segundo número: ")

if (opcion == "+"):
    res = num1 + num2
    print("\n El resultado de la suma es: " + str(res))
elif (opcion == "-"):
    res = num1 - num2
    print("El resultado de restar " + str(num2) + " a " + str(num1) + " es: " + str(res))
else:
    print("\n ¡Operación no válida! \n")