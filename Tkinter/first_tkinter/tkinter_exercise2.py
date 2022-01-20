import tkinter

win=tkinter.Tk()
win.title("Ativar/disativar")
win.resizable(True, True)
win.geometry('200x200')
print(win)

def activar():
    print("activar")

def desactivar():
    print("desactivar")

l2=tkinter.Label(win, text="admisnistração",background="yellow")
l2.pack()
print(l2)

txt= tkinter.Text(win, background="white")
txt.config(height=3,width=50) 
txt.pack()


botao = tkinter.Button ( win, text="activar",command=activar)

botao.pack()

botao2 = tkinter.Button ( win, text="Desativar",command=desactivar)
botao2.pack()

win.mainloop()