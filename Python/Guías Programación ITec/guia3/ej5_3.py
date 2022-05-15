#Guardar en una lista los números pares mayores que 0 y menores que 31. 

lista_numeros = []

n=1
while n < 31:
    if (n % 2 == 0):
        res = n
        lista_numeros.append(res)
    n= n+1

for i in range(len(lista_numeros)):
    print(str(lista_numeros[i]))
