import pygame as pg
from sys import exit
import os


WIDTH = 650
HEIGHT = 600

screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
pg.display.set_caption('Shooter Game')
#pg.display.set_icon()

FPS = 60

clock = pg.time.Clock()

player_run = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run.png"))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(player_run, (0,0))


    pg.display.update()
    clock.tick(FPS)