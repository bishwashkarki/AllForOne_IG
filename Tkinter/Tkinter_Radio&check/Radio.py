import tkinter as tk
from tkinter import ttk

def envia():
    print(nome.get())


def apaga():
    nome.delete(0,"end")

win=tk.Tk()
win.title("formulario")

label1=tk.Label(win,text="nome")
label1.config(background="black",foreground="blue")
label1.grid()

nome=ttk.Entry(win)
nome.grid()

button1=tk.Button(win,text="ENVIAR",command=envia)
button1.grid()

button2=ttk.Button(win,text="APAGAR",command=apaga)
button2.grid()

win.mainloop()


































