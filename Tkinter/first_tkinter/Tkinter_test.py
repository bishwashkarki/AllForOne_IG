from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import font

root = Tk()
root.title("test")
root.resizable(True, True)
root.geometry('300x150')

botao = ttk.Button ( root, text="clique aqui")
botao.pack()

cor = colorchooser.askcolor(color="#00ff00", title="sfsf")

l1= ttk.Label(root,background=cor[1],text="LABEL")
l1.pack()


root.mainloop()