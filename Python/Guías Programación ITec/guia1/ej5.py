#Nombre de alumno: Leonardo Roman Leonhardt
#Leer dos números reales y mostrarlos en orden creciente.

num1 = float(input("\n Inserte un número: "))
num2 = float(input("\n Inserte otro número: "))

if (num1 > num2):
    print("\n" + str(num2) + " , " + str(num1))
elif (num1 < num2):
    print("\n" + str(num1) + " , " + str(num2))
else:
    print("\n" + str(num1) + " es igual a " + str(num2))