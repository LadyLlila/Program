##Nombre de alumno: Leonardo Roman Leonhardt
#Pasar un período expresado en segundos a un período expresado en días, horas, minutos y segundos.

segundos_inicial = int(input("\n Inserte el tiempo en segundos [s]: "))

dias = segundos_inicial // 86400  # --> Cantidad de segundos en un día
segundos = segundos_inicial % 86400

horas = segundos // 3600
segundos= segundos % 3600

minutos = segundos // 60
segundos = segundos % 60


print("\n El período de " + str(segundos_inicial) + " [s] equivale a " + str(dias) + " días, " + str(horas) + " horas, " + str(minutos) + " minutos, " + str(segundos) + " segundos.")