#creating an game in which you can control a character and destroy "bots" comming towards you 



#importing all the modules needed to create this app
import pygame as pg
from pygame.locals import *
import os
#setting up pygame
pg.init()
pg.display.set_mode(size=(500, 500))

#surface = pygame.image.load("background_space.gif").convert()
#surface = pygame.transform.scale(surface=surface, size=(50, 50))
#background=pygame.image.load(file="background_space.gif")
#background = pygame.transform.scale(background, (1280, 720))

def load_image(background, colorkey=None, scale=1):
    fullname = os.path.join("C:\\Users\\Aluno\\Desktop\\10D2021-2022\PSI\\space invaders\\background_space.gif", background)
    image = pg.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()