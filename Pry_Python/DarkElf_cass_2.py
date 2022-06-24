#from subClass_warrior import *

class Elfo_oscuro:
    def __init__(self):
        self.profesion = "Warrior" #input("Ingrese profesión: \n 0 - Warrior \n 1 - Mage \n ")
        self.nombre = "Kain" #input("Nombre: ")
        self.genero = "Male"
        self.healpoints = 400
        self.magicpoints = 250
        self.level = 0
        self.arma = "espada1H, escudo"
        self.armadura = "heavy"
        self.numProfesion = 0
#=====|| Función subir n-niveles ||=======================
    def get_level(self, leveleo = 0): 
        leveleo = int(input("Ingrese cuántos niveles se sube: "))
        self.level = self.level + leveleo
        return self.level
#=====|| Profesión inicial ||=======================
    """def elegirProfesion1(self):
        if self.profesion == "0":
            #class Warrior(Elfo_oscuro):
            self.arma = "espada1H, escudo"
            self.armadura = "heavy"
            self.genero = "Male"
            print("Clase: Warrior")
            return 0
        else:
            self.arma = "báculo"
            self.armadura = "robe"
            self.genero = "Female"
            print("Clase: Mage")
            return 1"""
class PalusKnight(Elfo_oscuro):
    def __init__(self):
        super().__init__()
        self.arma = "espada1H_Dgrade, escudo_Dgrade"
        self.armadura = "heavy_Dgrade"
        self.profesion = "PalusKnight"

class ShillenKnight(PalusKnight):
    def __init__(self):
        super().__init__()
        self.arma = "espada1H_Cgrade, escudo_Cgrade"
        self.armadura = "heavy_Cgrade"
        self.profesion = "ShillenKnight"

class ShillenTemplar(ShillenKnight):
    def __init__(self):
        super().__init__()
        self.arma = "espada1H_Sgrade, escudo_Sgrade"
        self.armadura = "heavy_Sgrade"
        self.profesion = "ShillenTemplar"

class Assasin(Elfo_oscuro):
    def __init__(self):
        super().__init__()
        self.armadura = "light_Dgrade"
        self.arma = "daga_Dgrade, arco_Dgrade"
        self.profesion = "Assasin"



"""
def funcionElegir():  ->  clase
    if numProfesion == 0:
        es de la clase PalusKnight
    else:
        es de la clase Assasin
"""

PJ1 = Elfo_oscuro()
numNivel1 = PJ1.get_level()

if numNivel1 < 20:
    pass
elif numNivel1 > 19 and numNivel1 < 40:
    PJ1 = PalusKnight()
    PJ1.level = numNivel1
elif numNivel1 > 40 and numNivel1 <= 76:
    PJ1 = ShillenKnight()
    PJ1.level = numNivel1
else:
    PJ1 = ShillenTemplar()
    PJ1.level = numNivel1

#PJ1 = PalusKnight()
#PJ2 = Assasin()
#PJ3 = ShillenKnight()


print("\nProfesion: " + PJ1.profesion, "\nNivel: " + str(PJ1.level), "\nNombre: " + PJ1.nombre, "\nArma:" + PJ1.arma, "\nArmadura: " + PJ1.armadura, "\nGénero: " + PJ1.genero)
#print("\nProfesion: " + PJ2.profesion,  "\nNivel: " + str(PJ2.level), "\nNombre: " + PJ2.nombre, "\nArma:" + PJ2.arma, "\nArmadura: " + PJ2.armadura, "\nGénero: " + PJ2.genero)
#print("\nProfesion: " + PJ3.profesion,  "\nNivel: " + str(PJ3.level), "\nNombre: " + PJ3.nombre, "\nArma:" + PJ3.arma, "\nArmadura: " + PJ3.armadura, "\nGénero: " + PJ3.genero)