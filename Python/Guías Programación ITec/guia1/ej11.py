#Nombre de alumno: Leonardo Roman Leonhardt
#El costo del pasaje a Córdoba es de $1700. La empresa realiza un descuento de un 40 % sobre el costo del boleto a los niños que tienen entre 5 y 10 años y a los jubilados (mayores de 65). Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.

nombre = input("\nNombre de pasajero/a: ")
edad = int(input("\nEdad:"))

if (edad > 5 and edad < 10) or (edad >= 65):
    valor_pasaje = 1700 * (1 - 4/10)
else:
    valor_pasaje = 1700

print("\n ||-------------|| Datos y valor final de pasaje ||-------------||\n")
print("Nombre: " + nombre)
print("\nEdad: " + str(edad))
print("\nValor del pasaje: " + str(valor_pasaje) + "\n")