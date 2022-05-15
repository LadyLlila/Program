#Buscar una palabra y reemplazarla por otra todas las veces que aparezca. Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.'

s = "Quiero comer manzanas, solamente manzanas."
print(s)
buscar = input("Inserte una palabra que desee reemplazar en el texto: ")
reemplazar = input("¿Por qué palabra desea reemplazar " + buscar + "? ")

if (buscar in s):
    posicion_inicial = s.index(buscar)
    posicion_final = posicion_inicial + len(buscar)
    # lista_s = s.split(","), s.split(" "), s.split(".")
    # print(lista_s)
    # indice =lista_s.index(buscar)
    # lista_s.remove(buscar)
    # lista_s.append(reemplazar) in indice
    s_reemp = s.replace(buscar, reemplazar)

    print(s_reemp)
else:
    print("La palabra no está en el texto.")