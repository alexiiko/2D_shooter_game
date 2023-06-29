import pygame as pg
import os

screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
pg.display.set_caption("Shooter Game")
pg.display.set_icon(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "idle", "idle_1.png")))

screen_info = pg.display.Info()

WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h

FPS = 60

clock = pg.time.Clock()

pg.mouse.set_visible(False)