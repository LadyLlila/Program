#Recibir por teclado una cadena de números e insertar  un punto cada 3 dígitos como divisorio de miles. Ej.  1234567890 debería devolver 1.234.567.890

#---------|| NO FUNCIONA ||---------------------------

numeros = int(input("Inserte una cadena de números: "))

cadena_numeros = str(numeros)

# tres_numeros = []
# for i in range(len(cadena_numeros),0):
#     tres_numeros = numeros[i]
#     cadena_numeros = "." + tres_numeros
#     i = i -3
# print(tres_numeros)

for i in range(len(cadena_numeros)):
    tres_numeros = cadena_numeros[:-i*3]
    print(tres_numeros, end=".")
    i= i-1
    
