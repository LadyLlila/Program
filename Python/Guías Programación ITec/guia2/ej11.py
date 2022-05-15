#Ingresar 7 números enteros y en el caso de que sean naturales de una sola cifra mostrar un cartel en cada uno.

print("\nA continuación, ingresará 7 números enteros:")

lista_numeros = [0 for x in range(7)]

for i in range(len(lista_numeros)):
    lista_numeros[i] = int(input("\nIngrese número {}: " .format(i+1)))

for i in range(len(lista_numeros)):
    if (0 < lista_numeros[i] < 10):
        print(lista_numeros[i], end=" <-- Natural de una sola cifra \n")
