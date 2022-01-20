
import tkinter
from tkinter import ttk
import sys

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

win.wm_iconbitmap("C:\\Users\\Aluno\\Desktop\\PSI\\Tkinter\\menus\\icon.ico")
win.title("leitor de musica")

menubar=tkinter.Menu(win)
win.config(menu=menubar)

#Menu ficheiro
ficheiro=tkinter.Menu(menubar,tearoff=0)
menubar.add_cascade(label="FICHEIRO",menu=ficheiro,underline=0)
ficheiro.add_command(label="Novo",command=futuro_comando)
ficheiro.add_command(label="Abrir",command=futuro_comando)
ficheiro.add_command(label="guardar",command=futuro_comando)
ficheiro.add_separator()
ficheiro.add_command(label="Sair",command=win.destroy)

#Menu Editor
Editar=tkinter.Menu(menubar)
menubar.add_cascade(menu=Editar, label="Editar")
Editar.add_command(label="Anular",command= lambda: print("Anular..."))
Editar.entryconfig("Anular",accelerator="Ctrl+Z")

Editar.add_command(label="Refazer",command= lambda: print("Refazer..."))
Editar.entryconfig("Refazer",accelerator="Ctrl+SHIFT+Z")

Editar.add_separator()

Editar.add_command(label="Copiar",command= lambda: print("Copiar..."))
Editar.entryconfig("Copiar",accelerator="Ctrl+C")

Editar.add_command(label="cortar",command= lambda: print("cortar..."))
Editar.entryconfig("cortar",accelerator="Ctrl+X")

Editar.add_command(label="colar",command= lambda: print("colar..."))
Editar.entryconfig("colar",accelerator="Ctrl+V")

Editar.add_separator()


#sub-Menu fonte
fonte_sub=tkinter.Menu(Editar,tearoff=0)
Editar.add_cascade(label="fonte",menu=fonte_sub)
fonte_sub.add_command(label="Arial",command=lambda: print("Fonte=Arial"))
fonte_sub.add_command(label="verdana",command=lambda: print("Fonte=verdana"))
fonte_sub.add_command(label="Times New Roman",command=lambda: print("Fonte=Times New Roman"))

#sub-Menu fonte
estilo_sub=tkinter.Menu(Editar,tearoff=0)
Editar.add_cascade(label="Estilo",menu=estilo_sub)
estilo_sub.add_command(label="Negrito",command=lambda: print("Negrito"))
estilo_sub.add_command(label="Italico",command=lambda: print("Italico"))
estilo_sub.add_command(label="Sublinhado",command=lambda: print("Sublinhado"))

#---------------------------------------------------------------------------------------------------------------------------------------

Ajuda=tkinter.Menu(menubar,tearoff=0)
menubar.add_cascade(label="AJUDA",menu=Ajuda,underline=0)
Ajuda.add_command(label="Ajuda",command=lambda: print("AJUDA"))
Ajuda.entryconfig("Ajuda",accelerator="F1")

Ajuda.add_command(label="Sobre",command=futuro_comando, state="disabled")

Ajuda.add_command(label="PYTHON",command=lambda: print("Versao:",sys.version))
logo=tkinter.PhotoImage(file="C:\\Users\\Aluno\\Desktop\\PSI\\Tkinter\\menus\\LOGO.gif").subsample(300,300)
Ajuda.entryconfig("PYTHON",image=logo, compound="left")










win.mainloop()