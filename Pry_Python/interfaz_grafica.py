import tkinter as tk

app = tk.Tk() #Crea la ventana principal

app.geometry("300x600") # Ancho x Alto
app.configure(background="black")
tk.Wm.wm_title(app, "La interfaz de la tertulia")

def saludar():
    print("Hola, entidad.")

palabra = tk.StringVar(app) # Podemos guardar datos tipo String y se puede mapear (leer) en otro objeto
entrada = tk.StringVar(app)
#=======|| BOTÓN ||==================
tk.Button(
    app,
    text="Haceme click!",
    font=("Courier", 14),
    bg="black",
    fg="white",
    command= saludar,
    #command=lambda:print("Hola, qué tal"),
    relief="flat"   #Sin borde
).pack(
    fill=tk.BOTH,
    expand=True # Que ocupe todo el espacio que pueda
) #Embolsa y mete

#=======|| ETIQUETA ||==================
tk.Label(
    app,
    text="Soy una etiqueta",
    fg="white",
    bg="green",
    justify="center",
    command=lambda: print("Hola, " + entrada.get())
).pack(
fill=tk.BOTH,
expand=True
) #Embolsa y mete
#=======|| ENTRADA ||==================

tk.Entry(
    app,
    text="Soy una etiqueta",
    fg="white",
    bg="black",
    justify="center",
    textVariable = entrada,
    
).pack(
fill=tk.BOTH,
expand=True
) #Embolsa y mete



app.mainloop()  #Refresca constantemente la ventana y la mantiene abierta
