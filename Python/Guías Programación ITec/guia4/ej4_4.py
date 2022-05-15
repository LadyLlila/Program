#Pasar una palabra a mayúsculas cambiando los caracteres uno por uno usando la tabla ASCII de referencia (googlear la tabla y las funciones de conversión en Python).

palabra = input("Inserte una palabra en minúscula: ")

for i in range(len(palabra)):              #--------------------------------------------------------------#
    mayuscula = chr(ord(palabra[i]) - 32)  # En la tabla ASCII se observa que entre mayúscula y minúscula #
    print(mayuscula, end="")               # hay 32 carácteres de diferencia                              #
print("\n")                                #--------------------------------------------------------------#