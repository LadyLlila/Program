##Nombre de alumno: Leonardo Roman Leonhardt
#Pedir un nombre y una opción ('>' o '<') y según esta mostrar por ejemplo.: Juan es menor de edad

nombre = input("\n Ingrese un nombre: ")
opcion = input("\n Ingrese un signo mayor que ( > ) o menor que ( < ) para definir si " + nombre + " es mayor o menor de edad : ")

if (opcion == ">"):
    print("\n" + nombre + " es mayor de edad. \n")
elif (opcion == "<"):
    print("\n" + nombre + " es menor de edad. \n")
else:
    print("\n ¡Operación no válida! \n")