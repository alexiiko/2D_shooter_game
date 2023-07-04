import pygame as pg
from sys import exit

from settings import *
from player import *
from bullet import *
from level import *
from crosshair import *
from crosshair_picture import *
from health_bar import *
from events import *
from enemy import *

#TODO: make enemy class

class Game():
    def __init__(self):
        pg.init()
        
    def update(self):
        pg.display.update()
        clock.tick(FPS)

    def draw_window(self):
        screen.fill("#6584AA")

        level.draw_tiles()

        player.draw(screen)
        player.update()

        enemy_group.draw(screen)
        enemy_group.update()

        crosshair.draw(screen)
        crosshair.update()
        crosshair_picture.draw(screen)
        crosshair_picture.update()

        bullet_group.draw(screen)
        bullet_group.update()

        health_bar.draw()
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()     
            if event.type == LOOSE_HEALTH:
                health_bar.update_life()    
    
    def run(self):
        while True:
            self.check_events()
            self.draw_window()
            self.update()

if __name__ == "__main__":
    game = Game()
    game.run()