#Dada una lista con números, crear otra con los cuadrados de esos valores. 

lista_numeros = []

numero = int(input("\nIngresar número (0 para finalizar): "))
# pregunta = 's'

while (numero != 0):
    lista_numeros.append(numero)
    numero = int(input("\nIngresar número (0 para finalizar): "))

for i in range(len(lista_numeros)):
    res = lista_numeros[i]*lista_numeros[i]
    print(str(lista_numeros[i])+"^2 = " + str(res))