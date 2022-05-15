#PRIMER EJEMPLO
import tkinter as tk
from tkinter import *  #para incluir todo lo que venga de tkinter
import os

root = Tk()

root.title("Bienvenido al primer programa con GUI")
frame = tk.Frame(root, bg="#f1f502") #amarillo

root.mainloop() #Fundamental para ejecutarse. Debe permanecer en un "bucle infinito" para poder ejecutarse.

#SEGUNDO EJEMPLO
window = Tk()

window.title("Bienvenido al segundo programa con GUI")
window.geometry('500x300') #establecer el tamaño predeterminado de ventana (en píxeles), usando la función geometry

lbl = Label(window, text="Hola", font=("Arial Bold", 14)) #font=("Arial Bold", 50)
lbl.grid(column=0, row=0)  #Sin llamar a la función grid para label, la etiqueta no aparecerá.

#Manejar el evento click de un botón

def clicked():

    lbl.configure(text="Button was clicked !!") #Esto cambia la etiqueta lbl que antes decía "hello"

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0) #Hay que tener en cuenta que colocamos el botón en la segunda columna de la ventana, que es la 1. Si olvidas eso y colocas el botón en la misma columna (en este caso la 0), se mostrará el botón solamente, ya que el botón estará por encima de la etiqueta.


"""
Puedes cambiar el color de frente del botón o de cualquier otro widget usando la propiedad fg.
También puedes cambiar el color de fondo de cualquier widget usando la propiedad bg."""

#Entrada de datos usando la clase Entry
txt = Entry(window,width=10) #Entrada
txt.grid(column=3, row=0)

def clicked():

    res = txt.get() + " drogón " 

    lbl.configure(text= res)

btn2 = Button(window, text="Click me to change text", bg="orange", fg="red", command=clicked)
btn2.grid(column=2, row=0)


root.mainloop()