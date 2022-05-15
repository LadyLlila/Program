# Cargar una lista con números. Invertir los elementos sin usar otra lista. 

lista_numeros = []

numero = ''
while numero != 0:
    numero = int(input("Ingrese número (0 para finalizar): "))
    lista_numeros.append(numero)

for i in lista_numeros:
    print(lista_numeros[-i])
    