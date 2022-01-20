#creating an game in which you can control a character and destroy "bots" comming towards you 



#importing all the modules needed to create this app
import pygame as pg
from pygame.locals import *
import os
#setting up pygame
if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath("C:\\Users\\Aluno\\Desktop\\10D2021-2022\PSI\\space invaders\\background_space.gif"))[0]
data_dir = os.path.join(main_dir, "data")

def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
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

pg.init()
screen = pg.display.set_mode((1280, 480), pg.SCALED)
pg.display.set_caption("Monkey Fever")
pg.mouse.set_visible(False)