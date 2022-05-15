#Cargar letras en una lista (while). Contar las vocales (for). Mostrar el total.

lista_letras = []


letra = input("Ingresar letra (0 para finalizar):")
# pregunta = 's'

while (letra != '0'):
    lista_letras.append(letra)
    letra = input("Ingresar letra (0 para finalizar):")

cantidad_vocales = 0
for i in range(len(lista_letras)):
    if (lista_letras[i] == "a") or (lista_letras[i] == "e") or (lista_letras[i] == "i") or (lista_letras[i] == "o") or (lista_letras[i] == "u"):
        cantidad_vocales = cantidad_vocales + 1

print("El total de vocales es de " + str(cantidad_vocales))