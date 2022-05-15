
class Perro:
    #Variable de clase
    animal = "perro"

    def __init__(self, raza, edad, color):
    #-----|| ATRIBUTOS - VARIABLES DE INSTANCIA ||--------
        self.raza = raza
        self.edad = edad
        self.color = color
        self.hambre = 10
    #----------------------------

    #-----|| MÉTODOS ||------------
    def ladrar(self):
        print("woof woof")

    def comer(self, comida):
        print(f"Comiendo... {comida}...")
        self.hambre = 0
    #----------------------------

miPerro = Perro("labrador", 3, "dorado")
miOtroPerro = Perro("caniche", 3, "blanco")

miPerro.ladrar()
print("Mi perro tiene "+ str(miPerro.hambre) +" puntos de hambre")
print(f"Mi otro perro es color {miOtroPerro.color}")