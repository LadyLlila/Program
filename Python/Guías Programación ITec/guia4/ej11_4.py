#Averiguar qué cantidad de letras tiene la palabra más larga y cual es.
s = "Quiero comer manzanas, solamente manzanas."

s = s.replace(",", "")
s = s.replace(".", "")
lista_s = s.split()

mayor_cant_letras=0

for i in range(len(lista_s)):
    if len(lista_s[i]) > mayor_cant_letras:
        mayor_cant_letras = len(lista_s[i])

lista_cantidad = []
for i in range(len(lista_s)):
    cantidad = len(lista_s[i])
    lista_cantidad.append(cantidad)
index = lista_cantidad.index(mayor_cant_letras)
# print(lista_cantidad)
# print(index)    
print("La palabra con mayor cantidad de letras es: \"" + lista_s[index] + "\" (" + str(mayor_cant_letras) + " letras.)")