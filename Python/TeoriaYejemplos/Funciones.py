"""
------||    FUNCIONES     ||----------> o MÉTODOS (definidas dentro de una CLASE)
Bloque de líneas de código que funcionan como una unidad realizando una tarea específica.
    *Pueden devolver valores (o no).
    *Pueden tener parámetros/argumentos (o no).

SINTAXIS:
                   *---> A estos paréntesis se les llama "zona de parámetros/argumentos"
def nombre_funcion():
    instrucciones de la fcn.

    return (Opcional. Esto cierra la función. De acá en adelante, no se ejecuta ninguna instrucción)

FCN. PREDEFINIDAS:
    * print()
    * input()
    etc...

FCN. PROPIAS
"""
#----|| DECLARACIÓN DE LA FUNCIÓN ||--------
def suma(param1, param2):
    print("def suma(param1, param2): \n Una función de dos parámetros que suma dos números o concatena dos strings:")
    print(param1+param2)
    res = param1 + param2

    return res # -> Para cambiar el scope de una variable, utilizar return
#----|| fin de la declaración ||-------

#----|| LLAMADA A LA FUNCIÓN  ||-----
suma("Leo","Joel")
sumaVariable = suma(1,2)
suma(1,sumaVariable)
suma("Pri", 3)
