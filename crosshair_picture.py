import pygame as pg
import os

class CrosshairPicture(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "ui", "crosshair_sourrounding.png"))
        self.rect = self.image.get_rect()

    def follow_cursor(self):
        self.rect.center = pg.mouse.get_pos()
    
    def update(self):
        self.follow_cursor()

crosshair_picture = pg.sprite.GroupSingle(CrosshairPicture())