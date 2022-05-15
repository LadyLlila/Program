#Nombre de alumno: Leonardo Roman Leonhardt
#Preguntar nombre, carrera en la que se inscribe y ciudad donde vive un ingresante al Instituto. Los estudiantes de la carrera de Electromecánica y que no viven en Río Cuarto tendrán un 15% de descuento en la cuota que es de $4500. Mostrar nombre, ciudad, carrera y monto final de la cuota.

#Ingreso de datos
print("\n Rellene los datos. Por favor, respete mayúsculas y puntuación. \n")
nombre = input("Ingrese su nombre: ")
var_ciudad = int(input("\n¿Vive en Río Cuarto? \n 1- Sí \n 0 - no \n --> "))
if var_ciudad == 0 :
    ciudad = input("\nIngrese ciudad donde vive: ")
elif var_ciudad == 1 :
    ciudad = "Río Cuarto"
else:
    ciudad = "Ha ingresado un valor no válido para \"ciudad\""
print("\nA continuación se presenta la lista de carreras. ingrese el número correspondiente: ")
carrera = int(input("\n 1 - Desarrollo de Software \n 2 - Electromecánica \n 3 - Hotelería y turismo \n --> "))
#-----------------------------------------------------------------
if (var_ciudad == 0) and (carrera == 2):
    cuota = 4500 * (1 - 15/100)
else:
    cuota = 4500

print("||------------------------------------------------------------------------------------|| \n")
print("\nMuchas gracias por su inscripción. A continuación sus datos y monto final de la cuota:")
print("\nNombre: " + nombre)
print("\nCiudad: " + ciudad)
if carrera == 1:
    carrera = "Desarrollo de Software"
elif carrera == 2:
    carrera = "Electromecánica"
elif carrera == 3:
    carrera = "Hotelería y turismo"
else:
    carrera = "Ha ingresado un valor no válido para \"carrera\""
print("\nCarrera: " + carrera)
print("\nCuota: " + str(cuota))