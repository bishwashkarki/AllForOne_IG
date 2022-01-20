import tkinter
import tkinter 
import random

start_win=tkinter.Tk()
start_win.title("HANGMAN")
start_win.resizable(False, False)
start_win.geometry("600x400+50+50")
background=tkinter.PhotoImage(file="C:\\Users\\Aluno\\Desktop\\10D2021-2022\PSI\\test\\hangman_startmenu.gif")
canvas1 = tkinter.Canvas(start_win, width = 400,height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = background,anchor = "nw")
print(start_win)

def hangman_game():
    
    
    tkinter.Label(start_win, text="").pack()
    count=0
    list_words=["now","never","today","yesterday","tomorrow","month","year","date","time","computer","python"]
    
    random_word=random.choice(list_words)

    num_of_letter=len(random_word)
    print(random_word)
    list_chosen_word=list(random_word)
    print(list_chosen_word)


    

    while count<num_of_letter:
        count+=1
        input_word=input("write a letter:")
        for i in input_word:
            if i in list_chosen_word:
                print("yes")
            else:
                print("no")  
                

def quit():
    start_win.quit()

button1=tkinter.Button(start_win, text="start", command=hangman_game,height = 3, width = 20,background="skyblue")
button1.place(x=100,y=100)

button2=tkinter.Button(start_win, text="Quit", command=quit,height = 3, width = 20,background="skyblue")
button2.place(x=100,y=200)

































start_win.mainloop()