import tkinter
import pygame

win=tkinter.Tk()
win.title("leitor de musica")
win.resizable(True, True)
win.geometry('400x550')
win.config(background="purple")
print(win)

def activar():
    print("activar")

def desactivar():
    print("desactivar")

l2=tkinter.Label(win, text="Music player",background="yellow")
l2.pack()
print(l2)

Imglabel=tkinter.PhotoImage(file="C:\\Users\\Aluno\\Desktop\\PSI\\Tkinter\\first_tkinter\\player.gif")
l2.img=Imglabel
l2.config(image=l2.img)
l2.config(height=200,width=800) 


def playmusic():
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\Aluno\\Desktop\\PSI\\Tkinter\\music1.mp3")
    pygame.mixer.music.play()

def stopmusic():
    pygame.mixer.music.stop()

def pausemusic():
    pygame.mixer.music.pause()

def continuemusic():
    pygame.mixer.music.unpause()

def quit():
    pygame.mixer.quit()


l2=tkinter.Label(win, text="Audio Track",height=3,width=100,background="black",foreground="red")
l2.pack()
print(l2)


botao = tkinter.Button ( win,height=3,width=100, text="PLAY",command=playmusic)

botao.pack()

botao2 = tkinter.Button ( win,height=3,width=100, text="STOP",command=stopmusic)
botao2.pack()

botao3 = tkinter.Button ( win,height=3,width=100, text="PAUSE",command=pausemusic)
botao3.pack()

botao4 = tkinter.Button ( win,height=3,width=100, text="CONTINUE",command=continuemusic)
botao4.pack()

botao5 = tkinter.Button ( win,height=3,width=100, text="QUIT",command=quit)
botao5.pack()

win.mainloop()