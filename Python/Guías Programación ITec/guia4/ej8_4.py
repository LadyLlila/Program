#Contar la cantidad de letras (no incluir los separadores)

s = "Quiero comer manzanas, solamente manzanas."

s = s.replace(",", "")
s = s.replace(".", "")
lista_s = s.split()

cantidad_letras = 0
cantidad_letras_lista = []
for i in range(len(lista_s)):
    cantidad_letras = len(lista_s[i])
    cantidad_letras_lista.append(cantidad_letras)

cantidad_letras_total = 0
for i in range(len(cantidad_letras_lista)):
    cantidad_letras_total = cantidad_letras_total + cantidad_letras_lista[i]

print("Cantidad de letras en total: " + str(cantidad_letras_total))
print(cantidad_letras_lista)
