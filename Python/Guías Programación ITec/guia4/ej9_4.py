#Contar la cantidad de palabras.
s = "Quiero comer manzanas, solamente manzanas."

s = s.replace(",", "")
s = s.replace(".", "")
lista_s = s.split()

cantidad_palabras = len(lista_s)

print("Cantidad de palabras: " + str(cantidad_palabras))