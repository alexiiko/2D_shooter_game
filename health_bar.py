import pygame as pg
import settings

class HealthBar():
    def __init__(self):
        self.height = 50
        self.width = 450

    def draw(self):
        self.green_rect = pg.Rect(0,0, self.width, self.height)
        self.red_rect = pg.Rect(0,0,450, self.height)

        self.outline = pg.Rect(0,0,450, self.height)

        pg.draw.rect(settings.screen, "red", self.red_rect)
        pg.draw.rect(settings.screen, "green", self.green_rect)
        pg.draw.rect(settings.screen, "black", self.outline, 3)
    
    def update_life(self):
        self.width -= 50

        if self.width <= 0:
            self.width = 450

health_bar = HealthBar()