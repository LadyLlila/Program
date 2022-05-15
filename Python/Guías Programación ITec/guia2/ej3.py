#Mostrar por pantalla una lista de 20 números enteros consecutivos, comenzando con un número ingresado por teclado.

numero = int(input("\nIngrese un número para imprimir los siguientes 20 números: "))
i = 0

while i < 21:
    numero = numero + 1
    i= i +1
    print(numero)