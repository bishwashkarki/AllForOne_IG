import tkinter 
from tkinter import ttk

def verifica():
    opcoes=("escolheu as opcoes: " + op1.get() + op2.get() + op3.get())
    l2.config(text = opcoes, background="red", foreground="white")
    print(opcoes)

root=tkinter.Tk()

l1=tkinter.Label(root,text="que redes socias utilixadas")
l1.config(background="tan", foreground="blue")
l1.pack()

op1=tkinter.StringVar()
op2=tkinter.StringVar()
op3=tkinter.StringVar()

r1=ttk.Checkbutton(root,text="Facebook")
r1.config(variable=op1,onvalue="Facebook",offvalue="Não gosto")
r1.pack()

r2=ttk.Checkbutton(root,text="Instagram")
r2.config(variable=op1,onvalue="Instagram",offvalue="")
r2.pack()

r3=ttk.Checkbutton(root,text="Twitter")
r3.config(variable=op1,onvalue="Twitter")
r3.pack()

b1=ttk.Button(root, text="VERIFICAR", command=verifica)
b1.pack()

l2=tkinter.Label(root,text="As suas opcoes são ...")
l2.pack()

root.mainloop()