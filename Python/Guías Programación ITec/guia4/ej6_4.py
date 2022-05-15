# En los siguientes ejercicios (6 a 11) trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”, considerar que una palabra es toda secuencia de caracteres diferentes de los separadores (los caracteres separadores son el espacio, la coma y el punto).

# 6. Buscar una palabra completa en un texto y contar cuántas veces está.

s = "Quiero comer manzanas, solamente manzanas."
print(s)
buscar = input("Inserte una cadena que desee buscar en el texto: ")

veces_aparece = 0
if buscar in s:
    veces_aparece = s.count(buscar)
    print("La cadena \""+ buscar +"\" aparece " + str(veces_aparece) + " veces en el texto")
else:
    print("La cadena no aparece en el texto")