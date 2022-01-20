#importing modules
import tkinter
import tkinter 
import turtle
import random

#setting up the window
start_win=tkinter.Tk()
start_win.title("HANGMAN")
start_win.resizable(False, False)
start_win.geometry("1000x460+50+50")
#background image
background=tkinter.PhotoImage(file="hangman_startmenu.gif")
canvas1 = tkinter.Canvas(start_win, width = 400,height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = background,anchor = "nw")
print(start_win)

loss_count=0
def hangman_game():

    
    def func_turtle():
        global loss_count
        #seting up turtle
        
        turtle.setup(500, 500, startx=1000, starty=300)
        turtle.pencolor("purple")
        turtle.fillcolor("orange")
        turtle.pensize(2)
        turtle.speed(0)
        #turtle drawing hangman
        print(loss_count)
        loss_count=loss_count+1
        print("lost count=",loss_count)
        if loss_count==1:
            turtle.begin_fill()
            turtle.circle(30)
            turtle.end_fill()
        elif loss_count==2:
            turtle.right(90)
            turtle.forward(100)
        elif loss_count==3:
            turtle.left(45)
            turtle.forward(50)
        elif loss_count==4:
            turtle.right(180)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
        elif loss_count==5:
            turtle.right(180)
            turtle.forward(50)
            turtle.left(45)
            turtle.forward(100)
            turtle.right(135)
            turtle.forward(75)
        elif loss_count==6:
            turtle.right(180)
            turtle.forward(75)
            turtle.left(90)
            turtle.forward(75)
            turtle.exitonclick
            loss=tkinter.Label(start_win, text="You lost",height=3,width=10,background="black",foreground="white")
            loss.place(x=700,y=250)
            
    
    
    
    #list of words
    list_words=["now","never","today","yesterday","tomorrow","month","year","date","time","computer","python"]

    #choose a random word from list_words
    random_word=random.choice(list_words)

    
    print(random_word)


    #this breaks the word from random_word and puts it in a list 
    list_chosen_word=list(random_word)
    print(list_chosen_word)

    #label 1
    input_label=tkinter.Label(start_win, text="Write a letter",height=3,width=10,background="black",foreground="white")
    input_label.place(x=700,y=100)
    #textbox

    text=tkinter.Entry(start_win,background="black",foreground="white")
    text.place(x=700,y=150)

    
    

    #takes the input from textbox and puts it in the input_word variable
    def take_input():
        inp= text.get()
        input_word=inp
        text.delete(0,"end")
        
            
            #this verifies whether the input and a letter from the list_chosen_word match
        for i in input_word:
            if i in list_chosen_word:
                print("yes")
            else:
                print("no")
                func_turtle()
                    
                    
    #this button makes the print_input function work
    button3=tkinter.Button(start_win, text="enter", command=take_input,height = 3, width = 20,background="skyblue")
    button3.config(height=2,width=10)
    button3.place(x=700,y=200)
  
    
    
                
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