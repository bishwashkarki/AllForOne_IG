#creating an game in which you can control a character and destroy "bots" comming towards you 



#importing all the modules needed to create this app
import pygame


def game():
#setting up pygame
    pygame.init()

                            
    screen = pygame.display.set_mode((1400, 652))
    background = pygame.image.load('images/gm_bg.png')



    # jogo a correr
    running = True



    # equanto o jogo estiver a correr
    while running:
        
        
        # adiciona janela do jogo
        screen.blit(background,(0,0))
    pygame.display.flip()


game()



