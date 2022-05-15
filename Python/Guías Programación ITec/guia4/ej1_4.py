#Transformar la cadena "River vuelve a las copas", en la cadena "River vuelve a la copa". Resolverlo recorriendo la cadena original como si fuera una lista.

cadena = 'River vuelve a las copas'

cadena3 = cadena.replace("s", "")
# print(cadena2)
print(cadena3)

cadena2 = cadena.split('s')

for i in range(len(cadena2)):
    print(cadena2[i], end="")
print("\n")