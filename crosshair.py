import pygame as pg
import os

class Crosshair(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((10,10), pg.SRCALPHA)
        self.rect = self.image.get_rect()

        self.image.fill((0, 0, 0, 0))

    def follow_cursor(self):
        self.rect.center = pg.mouse.get_pos()

    def update(self):
        self.follow_cursor()
    
crosshair = pg.sprite.GroupSingle(Crosshair())