#choose the correct city

#import modules
import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH
#setting up window
win=tk.Tk()
win.title("Combo_Box")
win.resizable(True, True)
win.geometry("600x600+50+50")
win.option_add('*Font', '100')
print(win)

#importing photo
label1=tk.Label(win,text="CIDADES")
image1=tk.PhotoImage(file="Eiffletower.gif")
label1.img=image1
label1.config(image=label1.img)
label1.place(x=-300,y=-150)

#subtitle
label2=tk.Label(win,text="CIDADES")
label2.place(x=250,y=500)

#options
cidades=("lisbon","Paris","London")

#print selected opetion
def recebe_opcao():
    print(opcao.get())
    print(combo.state())

#comboBox
opcao=tk.StringVar()#remeber the chosen option
combo=ttk.Combobox(win,state="readonly",values=cidades,textvariable=opcao)#create comboBox
combo.current(0)#current option
combo.bind("option",recebe_opcao)#button to initiate recebe_opcao
combo.place(x=200,y=550)

#button to initiate recebe_opcao
button=tk.Button(win,text="select",command=recebe_opcao)
button.place(x=250,y=570)













win.mainloop()