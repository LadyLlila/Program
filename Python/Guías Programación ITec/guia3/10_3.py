#Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y el nombre del día que más llovió. (Todos los días llovió distinta cantidad)

dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
lluvia_por_dia = [0 for x in range(7)]

for i in range(7):
    lluvia_por_dia[i] = int(input("Ingrese la precipitación el día {} [en ml]: " .format(dias_semana[i])))

lluvia_total = 0
for i in range(7):
    lluvia_total = lluvia_total + lluvia_por_dia[i]

print("Total de lluvia caída en la semana: " + str(lluvia_total) + " ml.")

lluvia_maxima = 0
for i in range(7):
    if lluvia_maxima <= lluvia_por_dia[i]:
        lluvia_maxima = lluvia_por_dia[i]
print("Día que más llovió: " + dias_semana[lluvia_por_dia.index(lluvia_maxima)])