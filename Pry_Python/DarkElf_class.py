class Elfo_oscuro:
    def __init__(self, clase, cabello, rostro, genero):
        self.clase = clase
        self.cabello = cabello
        self.rostro = rostro
        self.genero = genero
        self.healpoints = 400
        self.magicpoints = 250
        self.level = 0
        self.arma = "None"
        self.armadura = "None"
        
    def get_level(self, leveleo = 0): 
        leveleo = int(input("Ingrese cuántos niveles se sube: "))
        self.level = self.level + leveleo
        return self.level

personaje1 = Elfo_oscuro("Warrior", "blanco", "serio", "male")
print(personaje1.clase, "cabello "+ personaje1.cabello, "rostro " + personaje1.rostro, "genero " + personaje1.genero)


nivelPJ = personaje1.get_level()


class Warrior(Elfo_oscuro):
    def __init__(self):
        #super().__init__()
    #def tipoDeArma(self):
        self.arma = "espada1H, escudo, duales, daga, arco"
    #    return self.arma
    #def tipoDeArmadura(self):
        self.armadura = "heavy, light"
    #    print(self.armadura, self.arma)
    #    print("Clase: Warrior")
    #    return self.armadura
print(Warrior.arma)    
if nivelPJ > 19 and nivelPJ < 41:
    class PalusKnight(Warrior):
        def __init__(self):
            #super().__init__()
            self.arma = "espada1H, escudo"
            self.armadura = "heavy"
        #def tipoDeArmadura(self):
            #return self.armadura


if nivelPJ <41:
#========|| Punto de decisión ||==================
    numClase = input("Ingrese:\n    0 - Blade Dancer \n     1 - ShillenKnight \n ")
    #
    if numClase == "0":
        class BladeDancer(PalusKnight):
            def __init__(self):
                super().__init__()
            #def tipoDeArma(self):
                self.arma = "duales"
            #---------------------------
        # def dimeLaClase(self):
        #     print("La clase es BladeDancer.")
    # Ver qué más se agrega
    else:
        class ShillenKnight(PalusKnight):
            def __init__(self):
                super().__init__()
                self.arma = "espada1H, escudo"
    #---------------------------
        # def dimeLaClase(self):
            #    print("La clase es ShillenKnight")

#class SpectralDancer(BladeDancer): 


#class ShillenTemplar(ShillenKnight):
    # Agregar mas
#    class Assasin(Warrior):
#        def tipoDeArma(self):
#            self.arma = "daga, arco"
#        def tipoDeArmadura(self):
#            self.armadura = "light"    

