#importing modules
import tkinter
import tkinter 
import pygame
import random

#setting up the window
start_win=tkinter.Tk()
start_win.title("HANGMAN")
start_win.resizable(False, False)
start_win.geometry("1000x460+50+50")
#background image
background=tkinter.PhotoImage(file="C:\\Users\\Aluno\\Desktop\\10D2021-2022\PSI\\test\\hangman_startmenu.gif")
canvas1 = tkinter.Canvas(start_win, width = 400,height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = background,anchor = "nw")
print(start_win)


def hangman_game():
    #takes the input from textbox and puts it in the input_word variable
    def take_input():
        inp= text.get(1.0, "end-1c")
        input_word=inp

    

    count=0
    #list of words
    list_words=["now","never","today","yesterday","tomorrow","month","year","date","time","computer","python"]

    #choose a random word from list_words
    random_word=random.choice(list_words)

    #counts the number of character in random_word
    num_of_letter=len(random_word)
    print(random_word)
    #this breaks the word from random_word and puts it in a list 
    list_chosen_word=list(random_word)
    print(list_chosen_word)
    #label 1
    input_label=tkinter.Label(start_win, text="Write a letter",height=3,width=10,background="black",foreground="white")
    input_label.place(x=700,y=100)
    #textbox
    text=tkinter.Text(start_win,height=2,width=20,background="black",foreground="white")
    text.place(x=700,y=150)
    #this button makes the print_input function work
    button3=tkinter.Button(start_win, text="enter", command=take_input,height = 3, width = 20,background="skyblue")
    button3.place(x=100,y=100)
    #label 2
    input_label2=tkinter.Label(start_win, text="your answer=",height=3,width=10,background="black",foreground="white")
    input_label2.place(x=700,y=200)

    #this verifies whether the input and a letter from the list_chosen_word match
    while count<num_of_letter:
        count+=1
        input_word=input("write a letter:")
        
        
        
        for i in input_word:
            if i in list_chosen_word:
                print("yes")
            else:
                print("no")  
    
    
                
#this closes the window
def quit():
    start_win.quit()
#this button starts the hang_man function 
button1=tkinter.Button(start_win, text="start", command=hangman_game,height = 3, width = 20,background="skyblue")
button1.place(x=100,y=100)
#this button starts the quit funtion
button2=tkinter.Button(start_win, text="Quit", command=quit,height = 3, width = 20,background="skyblue")
button2.place(x=100,y=200)

































start_win.mainloop()