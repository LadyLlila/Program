#Dada una serie de números reales positivos, determinar el valor máximo y mostrarlo al final. Se deberá ir preguntando si hay más números para ingresar.
#--------------------------------------------------------------
#numero1 = float(input("\n Ingrese un número real positivo: "))
#pregunta = input("\nDesea ingresar más? [s/n] ")
#--------------->
#¡PROBLEMAS! Los números se sobreescriben y no da como resultado el mayor. Podría hacerlo con un arreglo, pero no puedo porque necesito definir su tamaño previamente, lo cual va contra el inciso.

#-----|| RESUELTO ||--------------->
pregunta = 's'
res = 0
while pregunta == 's':
    numero2 = float(input("\n Ingrese un número real positivo: "))
    if numero2 >= res:
        res = numero2
    pregunta = input("\nDesea ingresar más? [s/n] ")

print("El número mayor de la sucesión ingresada es " + str(res))