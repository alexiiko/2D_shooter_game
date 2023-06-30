import pygame as pg
from sys import exit
import settings
import player
import bullet
import level
import crosshair
import crosshair_picture
import health_bar

#TODO: make logic for level switching
#TODO: implement enemys 

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()                

    settings.screen.fill("#6584AA")

    level.level.draw_tiles()

    player.player.draw(settings.screen)
    player.player.update()

    crosshair.crosshair.draw(settings.screen)
    crosshair.crosshair.update()
    crosshair_picture.crosshair_picture.draw(settings.screen)
    crosshair_picture.crosshair_picture.update()

    bullet.bullet_group.draw(settings.screen)
    bullet.bullet_group.update()

    health_bar.health_bar.update()

    pg.display.update()
    settings.clock.tick(settings.FPS)