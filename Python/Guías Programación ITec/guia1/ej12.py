#Nombre de alumno: Leonardo Roman Leonhardt
#Calcular el sueldo a cobrar teniendo en cuenta que los empleados que no han faltado y cuya antigüedad es superior a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000). Pedir la cantidad de días no trabajados y año de ingreso en la empresa.

print("\nA continuación, complete los datos solicitados: ")
dias_no_trabajados = int(input("\nCantidad de días no trabajados: "))
ano_de_ingreso = int(input("\nAño de ingreso en la empresa: "))

if (dias_no_trabajados == 0) and ((2021 - ano_de_ingreso) > 5):
    sueldo = 47000 * (1 + 3/10)
else:
    sueldo = 47000

print("\n --> Sueldo a cobrar: " + str(sueldo) + "\n")
