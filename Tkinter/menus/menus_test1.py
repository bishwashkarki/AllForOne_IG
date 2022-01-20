
import tkinter
from tkinter import ttk

def futuro_comando():
    print("error")

win=tkinter.Tk()
win.resizable(False, False)
win.geometry('640x480+450+200')
win.config(background="purple")
win.protocol("WM_DELETE_WINDOW", win.destroy)

label_1=ttk.Label(win, text="Menus",background="yellow")
label_1.pack()

label_image=tkinter.PhotoImage(file="C:\\Users\\Aluno\\Desktop\\PSI\\Tkinter\\menus\\640x480_pic.gif")
label_1.config(image=label_image)

win.wm_iconbitmap("C:\\Users\\Aluno\\Desktop\\PSI\\Tkinter\\menus\\vw_intro.ico")
win.title("leitor de musica")

menubar=tkinter.Menu(win)
win.config(menu=menubar)


#------menu Garamgem----------
garagem=tkinter.Menu(menubar,tearoff=0)
menubar.add_cascade(label="GARAGEM",menu=garagem,underline=0)
garagem.add_command(label="Parque",command=futuro_comando)
garagem.add_command(label="Login",command=futuro_comando)
garagem.add_separator()
garagem.add_command(label="Sair",command=win.destroy)

#------menu clientes----------
clientes=tkinter.Menu(menubar)
menubar.add_cascade(label="CLIENTES",menu=clientes,underline=0)
clientes.add_command(label="Inserir",command=futuro_comando,state="disabled")
clientes.add_command(label="Alterar",command=futuro_comando,state="disabled")
clientes.add_command(label="Consultar",command=futuro_comando,state="normal")

#------menu Administracao----------
administracao=tkinter.Menu(menubar)
menubar.add_cascade(label="ADMINISTRACAO",menu=administracao,underline=0)
administracao.add_command(label="Parque",command=futuro_comando)


#------sub-menu FUNCIONARIOS (administracao)----------
adm_funcionarios=tkinter.Menu(administracao,tearoff=0)
administracao.add_cascade(label="Funcionarios",menu=adm_funcionarios)
adm_funcionarios.add_command(label="Inserir",command=futuro_comando)
adm_funcionarios.add_command(label="Alterar",command=futuro_comando)
adm_funcionarios.add_command(label="Remover",command=futuro_comando)
adm_funcionarios.add_command(label="Consultar",command=futuro_comando)

win.mainloop()
