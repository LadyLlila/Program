#Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

lista_dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
lluvia_por_dia = [0 for x in range(7)]

total = 0
for i in range(7):
    lluvia = int(input(f"Ingrese la lluvia [ml] del día {lista_dias[i]}: "))
    lluvia_por_dia[i] = lluvia
    total = total + lluvia

dia_mayor_lluvia = 0
for i in range(len(lista_dias)):
    if dia_mayor_lluvia <= lluvia_por_dia[i]:
        dia_mayor_lluvia = lluvia_por_dia[i]

for i in range(7):
    print(f"{lista_dias[i]}: {lluvia_por_dia[i]} ml")

print(f"Día de mayor lluvia: {lista_dias[lluvia_por_dia.index(dia_mayor_lluvia)]}")
print(f"Lluvia total caída: {total} ml")