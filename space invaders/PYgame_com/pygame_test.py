import pygame

background = ['../images/background_space.gif','../images/gm_bg.png']
screen = pygame.display.set_mode((1400, 652))
for i in range(6):
    screen.blit(background[i], (i*10, 0))
playerpos = 3
screen.blit('../images/gm_bg.png', (playerpos*10, 0))