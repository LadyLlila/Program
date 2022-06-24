# Cargar letras en una lista (while). Contar las vocales (for). Mostrar el total.

from operator import le


lista_letras = ["" for x in range (10)]
i = 0
numVocales = 0
while i < len(lista_letras):
    letra = input("Ingrese una letra: ")
    if len(letra) != 1:
        print("¡Debe ingresar una letra!")
        continue
    lista_letras[i] = letra
    i += 1
    if (letra == "a" or letra == "e" or letra == "i" or letra =="o" or letra =="u"):
        numVocales += 1



print(lista_letras)
print(f"La cantidad de vocales es de : {numVocales}")