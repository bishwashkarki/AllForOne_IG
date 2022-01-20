import tkinter



win=tkinter.Tk()
win.title("Labels com Imagens!")
win.resizable(True, True)
win.geometry('800x200')
print(win)

l2=tkinter.Label(win, text="Linguagem Python",background="yellow")
l2.pack()
print(l2)



s2="C:\\Users\\Aluno\\Desktop\\PSI\\Tkinter\\py.png"
Img_2_label=tkinter.PhotoImage(file=s2)
l2.img=Img_2_label
l2.config(image=l2.img)
l2.config(height=200,width=800) 

l2.config(compound='left')
l2.config(font=('Courier', 18, 'bold'))
l2.config(foreground='red')

win.mainloop()