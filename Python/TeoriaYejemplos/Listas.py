""" IMPORTANTE |---> ¡¡¡Al final hay una LISTA COMPLETA DE MÉTODOS para Listas!!!
---------------------------------------------------------------------------------
LISTAS son secuencias ordenadas que guardan una variedad de tipos de objetos.
    Usan [] brackets y comas para separar objetos.
        [1, 2, "objeto 3", "objeto 4"]
-------------------------------------------------------------------------------"""
#=====|| Métodos básicos ||===============
#Basics
mi_lista = ["primer objeto", 1, 2, 3]
print(mi_lista)
print(mi_lista, "\n", len(mi_lista))
#Acceder al elemento 0
print(f"Esto devuelve el elemento 0 de la lista: {mi_lista[0]}")
#desde-hasta
print(mi_lista[2:])
print(mi_lista[:3])

#=====|| .append() y .pop(): agregar o remover elementos ||===============
otra_lista = ["cuatro", "cinco"]
nueva_lista = mi_lista + otra_lista  # La forma más correcta es con .append()
print(nueva_lista)
otra_lista.append('seis')   #  .append()
print(otra_lista)
otra_lista.pop()            #  .pop()
print(otra_lista)   # "seis" será el item popeado. ¿a dónde fue?
item_popeado = otra_lista.pop()
print(item_popeado) # Acá está el item popeado

#=====|| .sort() y .reverse() ||===============
lista_letras = ["x", "a", "d", "z", "o"]
lista_num = [3, 1, 5, 4, 2]
#print(lista_letras.sort())
#print(lista_letras.reverse())
#print(lista_num.sort())
#print(lista_num.reverse()) # -> None  || Estos .sort() y .reverse() están ocurriendo en su lugar,
                            # por lo que retornan un "None". La forma correcta:
print("Listas desordenadas:", "\n", lista_letras, "\n", lista_num)
print("Listas ordenadas")
lista_letras.sort()     # .sort()
print(lista_letras)
lista_num.sort()        # .sort()
print(lista_num)
lista_num.reverse()     # .reverse()
print(lista_num)
lista_letras.reverse()
print(lista_letras)

#=====|| Looping Through a String ||=====================
for x in "banana":
  print(x)

#=====|| Check String ||========================
    # Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt) # !!! Notar que no imprime "free", sino si es verdadera o falsa la premisa (True/False)

#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt) # !!! Notar que no imprime "free", sino si es verdadera o falsa la premisa (True/False)

#Mediante if
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

"""
=========|| EVERY LIST METHODS ||==============================
NOTE: Python DOES NOT have built-in support for Arrays (No existen Arrays [matrices] per se, sino vectores 1 x n (1 fila x n columnas), but Python Lists can be used instead).

METHOD	DESCRIPTION
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""