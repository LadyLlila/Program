from tkinter import *

ventana = Tk()
ventana.geometry("500x300")
ventana.config(bg="green")
ventana.title("LA ventana principal")
ventana.resizable(width=True, height=False)
ventana.iconbitmap('imagen.ico')


ventana.mainloop()