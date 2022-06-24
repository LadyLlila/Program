""" (Esto es un comentario. La PC no lo lee.)
========|| TIPOS DE DATO ||=================
- varString = "un texto"
- varInt = 28   --> Un número entero (-3, 5, 0, 845, etc)
- varFloat = 1.25328  --> Un decimal
- varList = [10, 2, 3, "Leo", "Pri"]
- varBool = True        --> verdadero o falso (True/False)
"""
# Otra forma de hacer comentario por línea

#=========|| Ejemplos de tipo de dato ||===============
nombre = "Priscilla"
edad = 28
altura = 1.70
familiares = ["Caro", "Raúl", "Vilma", "Andrea"]
esMujer = True
#=========|| Funciones print("--")   input("--") ||================
print("Vamos a mostrar datos de " + nombre)
print("Vamos a revelar su edad " + str(edad))
aniosASumar = int(input("Ingrese cuántos años quiere sumarle (O restarle): "))
edadTotal = edad + aniosASumar
print("el total de años es de: " + str(edadTotal))
#=========|| Condicionales ||=======================
#Esto nos dice si será mayor o menor de edad después de sumarle o restale años
if  edadTotal > 17:
    print("Es mayor de edad")
#elif edad < 17:
#    print("Es menor de edad")
else:
    print("Es menor de edad")

#=========|| Funciones ||============================
