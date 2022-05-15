#Nombre de alumno: Leonardo Roman Leonhardt

#Leer dos números y decir cuál es el mayor.

num1 = float(input("\n Inserte un número: "))
num2 = float(input("\n Inserte otro número: "))

if (num1 > num2):
    print("\n" + str(num1) + " es mayor que " + str(num2))
elif (num1 < num2):
    print("\n" + str(num1) + " es menor que " + str(num2))
else:
    print("\n" + str(num1) + " es igual a " + str(num2))

#    ><