


#Importamos los módulos necesarios
import math
import numpy as np
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker  # Etiquetas en los ejes

#Generamos los datos para el gráfico
x = np.array(range(20))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])

# Creamos el gráfico

plt.plot(x,y)
plt.show()

x = np.array(range(500))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])

# Creamos el gráfico

plt.plot(x,y)
plt.show()

x = np.arange(-10,10.5,.5) # (desde, hasta, step)
y = pow(x,3)+2*pow(x,2)+5*x
z=pow(x,3)+pow(x,2) + x

fig = plt.figure(figsize=(15,15))
fig.tight_layout() #Ajusta los gráficos para que no se empalmen

ax1 = fig.add_subplot(1,2,1)  #(fila, columna, ??)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(x,y)
ax2.plot(x,z)

ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

ax1.set_title("Gráfica 1")
ax2.set_title("Gráfica 2")
escala = 10
#ticks_x = ticker.FuncFormatter(lambda x,pos:'{:.2f}'.format(x/10))
#ax1.xaxis.set_mayor_formatter(ticks_x)
plt.show()

