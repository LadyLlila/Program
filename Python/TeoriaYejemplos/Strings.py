""" IMPORTANTE |---> ¡¡¡Al final hay una LISTA COMPLETA DE MÉTODOS para Strings!!!
---------------------------------------------------------------------------------------
STRINGS o CADENAS son secuencias ordenadas de carácteres, son arrays. Usan sintaxis con comillas simples o dobles
    -Texto con muchos caracteres
        * Índice :        0   1   2   3   4   5
        * Índice inverso: 0  -5  -4  -3  -2  -1      <- El 0 sigue siendo el primero!!! Sigue habiendo seis!
    
    -Podemos usar INDEXADO y SLICING para agarrar sub-secciones de una cadena:
        * INDEXADO: permite tomar un character singular de una cadena de palabras.
        * Notación de indexado: [], asignado después de la cadena.

        * SLICING: Permite tomar una subsección de múltiples caracteres, un "slice" de una cadena.
        Tiene la siguiente sintaxis:
            [start:stop:step]   ->  [0:4:2] "del 0 al 4, de 2 en 2"
-------------------------------------------------------------------------------------------"""
a = "tomar"
print(a[0:4:2])

#=======|| Inmutabilidad ||=============
name = "Pam"
#name[0] = "S"   #==> Esto da error ("object does not support item assignment") porque no es mutable, 
                # no se puede reasignar valores

#===|| Métodos ||================================

# upper / lower
print("====|| Métodos: .upper() / .lower() convierten a MAYÚSCULAS o minúsculas ||==========")
x = 'hola mundo'
x = x.upper()
print(x)
x = x.lower()
print(x)

#split: para separar palabras          (Útil en ciencia de datos, como Procesamiento de Lenguaje natural)
print("====|| .split() para separar/cortar palabras ||=========")
x = x.split('o')    #devuelve ->  ['h', 'la mund', '']
print(x)
# ¡Interesante!:
x = 'hola mundo'
x = x.split("|")    #Esto funcionaba como espacio, pero ya no funciona en nuevas versiones (sólo usar " "). Usando "|" devuelve todo el string como único elemento en un array: ['hola mundo']
print(x)
#x.split(" ")    #==>  AttributeError: 'list' object has no attribute 'split' (Esto ocurre porque en el comando anterior convertimos a x en un array)

#---> The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#The strip() method removes any whitespace from the BEGGINING or the END (NOT middle ones):
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#=======|| Python String Methods ||=================
# Note: All string methods returns new values. They do not change the original string.
"""
!!! NOTE: All string methods returns new values. They do not change the original string.

METHOD	        DESCRIPTION
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isascii()	    Returns True if all characters in the string are ascii characters
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Converts the elements of an iterable into a string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of 
                where it was found
rindex()	    Searches the string for a specified value and returns the last position of 
                where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning

NOTE: All string methods returns new values. They do not change the original string.
"""