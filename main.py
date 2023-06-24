import pygame as pg
import os
from sys import exit

WIDTH = 650
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Shooter Game')

FPS = 60

clock = pg.time.Clock()

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.run_list = []
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run_1.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run_2.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run_3.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run_4.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run_5.png")))

        self.run_index = 0

        self.idle_list = []
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "idle", "idle_1.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "idle", "idle_2.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "idle", "idle_3.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "idle", "idle_4.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "idle", "idle_5.png")))

        self.idle_index = 0

        self.image = self.idle_list[self.idle_index]

        self.rect = self.image.get_rect(topleft = (0,0))
        
    	

player = pg.sprite.GroupSingle(Player())

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    player.draw(screen)

    pg.display.update()
    clock.tick(FPS)
