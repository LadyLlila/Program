"""
Reglas generales de las funciones:
    * no se ejecuta la funcion a menos que la llames
    * la puedo llamar la cantidad de veces que quiera
    * primero hay que definir la funcion, y despues llamarla
    * primero van los parametros requeridos, y al final los opcionales
    * para cambiar el scope de una variable, utilizar return
------------
PARAMETERS or ARGUMENTS? From a function's perspective:
    * A PARAMETER is the variable listed inside the parentheses in the function DEFINITION.
    * An ARGUMENT is the value that is sent to the function WHEN IT'S CALLED.
-----------
INDEX:
    1- Funciones SIN parámetros
    2- Funciones CON parámetros
    3- Funciones con parámetros opcionales
    4- Argumentos (*args y **kwargs)
    5- *args  y  **kwargs  JUNTOS
    6- Expresiones Lamda, Mapas y Filtros
    7- Variables globales, enclosing y locales. Reasignación. Fcn anidadas.
    8- Ejemplo de return en condicionales
    
"""
#==========|| 1- FUNCIONES SIN PARAMETROS ||========================
"""
def miFuncion():
    #conjunto de instrucciones
"""

def derechos_humanos():
    print("Derecho a la vida")
    print("Derecho a la igualdad ante la ley")
    print("Derecho a la libertad")

derechos_humanos()

def derechos_mayorDeEdad():
    print("Derecho a votar")
    print("Derecho al trabajo")


#==========|| 2- FUNCIONES CON PARAMETROS ||=====================
"""
def miFuncion2(parametro1,parametro2):
    #conjunto de instrucciones
"""
def mayoria_de_edad(nombre,edad):
    print(f'Según la edad de {nombre}, sus derechos son:')
    if edad >= 18:
        derechos_humanos()
        derechos_mayorDeEdad()
    else:
        derechos_humanos()

#==========|| 3- FUNCIONES CON PARAMETROS OPCIONALES ||=======================
"""
def miFuncion3(parametro1,parametro2=valorpordefecto):
    #conjunto de instrucciones
"""
def mayoria_de_edad2(edad,nombre='DESCONOCIDO'):    # NOTE: Primero -> parámetros requeridos 
                                                         # Al final -> parámetros opcionales
    print(f'Según la edad de {nombre}, sus derechos son:')
    if edad >= 18:
        derechos_humanos()
        derechos_mayorDeEdad()
    else:
        derechos_humanos()

mayoria_de_edad2(15,'Pepito')

#==========|| 4- Argumentos (*args y **kwargs) ||==================
# Esta forma es LIMITADA:
def func(a,b):  # A estos parámetros se les llama PARÁMETROS POSICIONALES
    # retornar el 5% de la suma de a y b
    return print(sum((a,b))*0.05)
func(4,6)   # 4 y 6 son PARÁMETROS POSICIONALES

#VEAMOS:
#----|| *args (-> Tupla) ||------------
def func(*args): # Así podemos pasar CUANTOS ARGUMENTOS QUERRAMOS!!!!!!!!!!!!!!!!!!!!!
                 # *args -> Tupla   (*args retorna una Tupla)
    return print(sum(args)* 0.05)
func(4,6)
func(4,6,7,10,20)   # CUANTOS ARGUMENTOS QUERRAMOS

#----|| **kwargs (-> Dictionary) ||------------
def func(**kwargs): #hablamos de un diccionario
    if "fruit" in kwargs:
        print("Mi fruta escogida es {}".format(kwargs["fruit"]))
        print(f"Mi fruta escogida es {kwargs['fruit']}")    #==> ¡OJO! Acá me bardeó por 
                                                            # las comillas  dobles y simples
    else:
        print("no hay fruta")

func(fruit="manzana", veggie="lechuga") # -> "Mi fruta escogida es manzana"
func(veggie="lechuga")  # -> "no hay fruta"

#----|| 5- *args  y  **kwargs  JUNTOS  ||------------
def func(*args, **kwargs):
    print(args)
    print(kwargs)                        #|-> este 0 es el índice de la Tupla, en este caso -> 10
    print('me gustaría {} de {} para {}'.format(args[0],kwargs['comida'],kwargs["animal"]))
    print(f"me gustaría {args[1]} de {kwargs['comida']} para {kwargs['animal']}")
func(10,30,50,comida='leche', animal='perros')
    # -> "me gustaría 10 de leche para perros"
    # -> "me gustaría 30 de leche para perros"

#==========|| 6- Expresiones Lamda, Mapas y Filtros ||==========================

#-------|| Mapa ||----------
#Útil para llenar una función con una LISTA de datos
numeros = [1,2,3,4,5]
def square(num):
    res = num**2
    return res

for item in map(square, numeros):
    print(item)
# Otra opción para imprimirlos en forma de lista:
print(list(map(square,numeros)))

#-------|| Filter ||----------
numeros = [1,2,3,4,5,6,7]
def check_even(num):
    return num%2 == 0

for n in filter(check_even,numeros):    # -> Devuelve los números pares para los cuales la función(item) es verdadera
    print(n)
#-------|| LAMBDA ||----------
numeros = [1,2,3,4,5,6,7]
square = lambda num: num ** 2
print(square(5))
print(map(lambda num: num ** 2, numeros))   # -> <map object at 0x000002FC015AFFD0> ERROR!!!
print(list(map(lambda num: num ** 2, numeros))) # -> [1, 4, 9, 16, 25, 36, 49]   ¡Funciona!
print(list(filter(lambda num: num%2 == 0, numeros))) # -> [2, 4, 6]


#==========|| 7- Variables globales, enclosing y locales. Reasignación. Fcn anidadas. ||============
# Variable GLOBAL
name = 'VARIABLE GLOBAL'
def saludo():
    # Variable ENCLOSING (se encuentran entre dos funciones, una de ellas, anidada)
    name = 'Leonardo'   # -> "name" is not accessedPylance
    def hola(): # Función LOCAL / ANIDADA
        # Variable LOCAL
        name = 'Variable local' # Si no la redefino como acá, va a tomar la var ENCLOSING (anterior)
        print('hola ' + name) # -> "hola Variable local" -Toma sólo la local: esta función NO PUEDE acceder a variables externas. ¡Encontré que sí puede!! Sólo a variable ENCLOSING, aparente//

    hola() # ¿necesario llamarla dentro del Scope? ¿Será accesible desde el Scope Global? -¡No lo es!
saludo()
print(name) # -> 'VARIABLE GLOBAL'  - NOTE: sólo accede a la variable del Scope Global

#NOTE: Si defino una función fuera del Scope, ella sólo puedo acceder a la variable GLOBAL:
def despedida():
    print("Variable GLOBAL:",name)  # -> "Variable GLOBAL: VARIABLE GLOBAL"
despedida()

#------|| Reasignación ||--------------
x = 50   # GLOBAL
def func():
    #print(f"X es {x}") # -> SyntaxError: name 'x' is used prior to global declaration
                        # -> local variable 'x' referenced before assignment
                        # -> Implica que NO PUEDE acceder a la variable GLOBAL sin invocarla con "global"
    global x    # -> Ahora que la llamé, puedo usarla
    print(f"X es {x}")
    # Reasignación local
    x = "NUEVO VALOR REASIGNADO"
    print(f"Localmente cambiada de X a {x}")
func()

#==========|| 8- Ejemplo de return en condicionales ||=============================
def chequear_numero_par_en_lista(num_list):
    for number in num_list:
        if number % 2 == 0:
            print(True)
            return True
        else:
            #return False  || ==> Esto está mal. Se hace así:
            pass  # Significa "ignore y siga", cayendo en la siguiente instrucción:
    print(False)
    return False  # Cuando no se retorna el True.

chequear_numero_par_en_lista([1,3,5])   # -> False
chequear_numero_par_en_lista([1,2,5,6]) # -> True  (Existen números pares)