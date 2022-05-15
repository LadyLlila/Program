#Mostrar el valor doble del número de dos cifras (que es el único número) encontrado en la cadena. Ej.: 'Juan tiene 25 años' mostraría el número 50, ‘El dólar va a llegar este mes a 57 pesos casi seguro’,  mostraría 114.
s = "El dólar va a llegar este mes a 57 pesos casi seguro"
#s = "Juan tiene 25 años"
print(s)
s = s.replace(",", "")
s = s.replace(".", "")
lista_s = s.split()

for i in range(len(lista_s)):
    if ("1" in lista_s[i]) or ("2" in lista_s[i]) or  ("3" in lista_s[i]) or  ("3" in lista_s[i]) or ("4" in lista_s[i]) or ("5" in lista_s[i]) or  ("6" in lista_s[i]) or  ("7" in lista_s[i]) or  ("8" in lista_s[i]) or  ("9" in lista_s[i]):
        numero1 = int(lista_s[i])
        numero2 = str(numero1 * 2)
        lista_s[i] = numero2

for i in range(len(lista_s)):
    print(lista_s[i], end=" ")