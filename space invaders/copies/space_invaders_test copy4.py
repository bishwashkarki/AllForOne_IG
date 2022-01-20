#creating an game in which you can control a character and destroy "bots" comming towards you 



#importing all the modules needed to create this app

import pygame



def game():
#setting up pygame
    pygame.init()

                            
    screen = pygame.display.set_mode((1400, 652))
    background = pygame.image.load('images/background_space.gif').convert()
    player1=pygame.image.load('images/player1.png').convert()
    # jogo a correr
    running = True

    red=[247,17.4]

    # equanto o jogo estiver a correr
    while running:
        
        
        # adiciona janela do jogo
        pygame.display.flip()
        pygame.time.wait(10)
        screen.blit(background,(0,0))
        position = player1.get_rect()
        screen.blit(player1, position) 
        pygame.draw.rect(screen, (red), (x, y, width, height))

game()