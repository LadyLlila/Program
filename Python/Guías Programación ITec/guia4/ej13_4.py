#Pedir el ingreso de un nombre completo en la forma <nombre> <apellido> (ejemplo: Juan Pérez) y mostrarlo invertido y con coma <apellido>,<nombre> (ejemplo: Perez, Juan).

lista_nom_ap = []

nombre = input("Ingrese nombre: ")
lista_nom_ap.append(nombre)
apellido = input("Ingrese apellido: ")
lista_nom_ap.append(apellido)
print(lista_nom_ap)
#----------// CAMINO LARGO //------------------------------------------//
lista_nom_ap_inv = []
for i in range(2):
    lista_nom_ap_inv.append(lista_nom_ap[1-i])
for i in range(2):
    print(lista_nom_ap_inv[i], end=", ")
#----------// CAMINO CORTO //------------------------------------------//
