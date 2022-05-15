#by Leonardo Roman Leonhardt
#Preguntar si hay datos para ingresar, en caso afirmativo solicitar un número entero y decir si es negativo o no. Preguntar si repite.

respuesta = input("¿Hay datos para ingresar? [s/n] ")

if respuesta == "n":
    print("\n Entonces no moleste.\n")
elif respuesta == "s":
    numero = int(input("\n Ingrese un número entero: "))
    if (0 > numero):
        print("\n El número ingresado es negativo")
    else:
        print("\n El número ingresado es no negativo")
    respuesta2 = input("\n ¿Desea repetir? [s/n] ")
    while respuesta2 == "s":
        numero = int(input("\n Ingrese un número entero: "))
        if (0 > numero):
            print("\n El número ingresado es negativo")
        else:
            print("\n El número ingresado es no negativo")
        respuesta2 = input("\n ¿Desea repetir? [s/n] ")
    else:
        print("\n Entonces no moleste.\n")
