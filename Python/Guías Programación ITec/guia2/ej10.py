#Dada una lista de nombres y de salarios respectivos, determinar el salario mínimo y mostrar el nombre de la persona que menos gana.

lista_nombres = ["Martín", "Lucrecia", "Esteban", "Juana"]


salario_Martin = int(input("\nIngrese el salario de Martín: "))
salario_Lucrecia =  int(input("\nIngrese el salario de Lucrecia: "))
salario_Esteban = int(input("\nIngrese el salario de Esteban : "))
salario_Juana = int(input("\nIngrese el salario de Juana: "))


lista_sueldos = [salario_Martin, salario_Lucrecia, salario_Esteban, salario_Juana]

#print(lista_sueldos)  ||------|| FUNCIONA ||---------||

menor = 99999999999
for i in range(0, len(lista_sueldos)):
    if lista_sueldos[i] <= menor:
        menor = lista_sueldos[i]

menor_indice = lista_sueldos.index(menor)

print("El salario mínimo es de " + lista_nombres[menor_indice] + " y es de: $" + str(menor))

#---|| OTRA FORMA DE EXPRESAR ESTO: ||----------------------------------------------------
print("El salario mínimo es de {} y es de: ${}".format(lista_nombres[menor_indice], menor))