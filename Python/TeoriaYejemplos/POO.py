#PROGRAMACIÓN ORIENTADA A OBJETOS
"""
- Permite a los programadores crear sus propios objetos, dotados de métodos y atributos
    (Para scripts extensos necesitamos algo más que sólo funciones para organizar todo)
- Podemos llamar distintos métodos que se encuentran en una clase
- Los métodos son funciones que usan información sobre el objeto para retornar resultados
- Podemos crear código repetible y organizado (modularización)
- Las funciones se ponen dentro de las clases para que todo esté mejor organizado y evitar redundancia de código.

============|| SINTAXIS ||====================
class NombreDeClase():
    def __init__(self,param1,param2): # Función que ayuda a
                                        iniciar todos los parámetros de la clase 
                                        (ATRIBUTOS)
                                      # self: siempre necesario para que los
                                      atributos funcionen en la clase
 #-----|| ATRIBUTOS - VARIABLES DE INSTANCIA ||--------
        self.param1 = param1
        self.param2 = param2
 #-----|| MÉTODOS ||------------
    def otraFuncion(self):
        # acciones
        print(self.param1)
"""
#Ejemplo:
class Perro:
    #Variable de clase
    #animal = "perro"
    def __init__(self, raza, nombre, puntos):
    #-----|| ATRIBUTOS - VARIABLES DE INSTANCIA ||--------
        self.raza = raza
        self.nombre = nombre
        self.puntos = puntos # Esperamos un bool

huskie = Perro(raza="Huskie", nombre="Sam", puntos= False)

#============|| HERENCIA Y POLIMORFISMO ||==================

class Animal():
    def __init__(self):
        print("Animal creado")

    def quien_soy(self):
        print("Soy un animal")
    
    def comer(self):
        print("Estoy comiendo")
# Es una BUENA PRÁCTICA separar dos líneas entre una clase y otra
#=======||
class Perro(Animal):
    def __init__(self):
        Animal.__init__(self)  # Estoy iniciando todas los
                               # atributos de Animal
        print("Perro creado")
    
    def quien_soy(self):
        print("Soy un perro") # ¡Estamos reescribiendo la 
                              # función quien_soy !!!!
                              # Ver resultado abajo

nuevoPerro = Perro()

miPerro = Perro()
miPerro.quien_soy()
