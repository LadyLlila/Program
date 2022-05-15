#Transformar la cadena "Curso de Python" en la cadena "Curso de Programación en Python". Cortar la cadena original, agregarle el literal "Programación en" y concatenar.

cadena = "Curso de Python"

cadena2 = cadena[:8] + " Programación en" + cadena[8:]

print(cadena2)
