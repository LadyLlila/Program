#Elije piedra, papel o tijera para jugar con la PC:
import random

val1 = random.randint(1,3)
val2 = int(input("\n Ingrese 1 para piedra, 2 para papel y 3 para tijera: "))


if (val1 == 1) and (val2 == 2):
    ganador = "Ganaste: papel cubre piedra."
elif (val1 == 2) and (val2 == 1):
    ganador = "Perdiste: papel cubre piedra."
elif (val1 == 2) and (val2 == 3):
    ganador = "Ganaste: tijera corta papel."
elif (val1 == 3) and (val2 == 2):
    ganador = "Perdiste: tijera corta papel."
elif (val1 == 1) and (val2 == 3):
    ganador = "Perdiste: piedra rompe tijera."
elif (val1 == 3) and (val2 == 1):
    ganador = "Ganaste: piedra rompe tijera."
elif val1 == val2:
    ganador = "¡Empate!"
else:
    ganador = "Valor no válido."


print("\n Elegiste: " + str(val2) + ". La pc sacó: " + str(val1) + "\n\n")

print(ganador)