import pygame as pg
import os 
from settings import *
from bullet import *
from level import *
from events import *

class Player(pg.sprite.Sprite):
    def idle_animation(self):
        if self.flipped == False:
            self.idle_index += self.idle_animation_speed
            if self.idle_index >= len(self.idle_list):
                self.idle_index = 0

            self.image = pg.transform.scale(self.idle_list[int(self.idle_index)], (self.width, self.height))
        else:
            self.idle_index += self.idle_animation_speed
            if self.idle_index >= len(self.idle_list):
                self.idle_index = 0

            self.image = pg.transform.flip(pg.transform.scale(self.idle_list[int(self.idle_index)], (self.width, self.height)), True, False)

    def run_animation(self):
        key = pg.key.get_pressed()
        if key[pg.K_d]:
            self.run_index += self.run_animation_speed
            if self.run_index >= len(self.run_list):
                self.run_index = 0
            self.image = pg.transform.scale(self.run_list[int(self.run_index)], (self.width, self.height))
            self.flipped = False
        if key[pg.K_a]:
            self.run_index += self.run_animation_speed
            if self.run_index >= len(self.run_list):
                self.run_index = 0
            self.image = pg.transform.flip((pg.transform.scale(self.run_list[int(self.run_index)], (self.width, self.height))), True, False)
            self.flipped = True
        
        if key[pg.K_w] and self.flipped:
            self.run_index += self.run_animation_speed
            if self.run_index >= len(self.run_list):
                self.run_index = 0
            self.image = pg.transform.flip(pg.transform.scale(self.run_list[int(self.run_index)], (self.width, self.height)), True, False)

        if key[pg.K_w] and not self.flipped:
            self.run_index += self.run_animation_speed
            if self.run_index >= len(self.run_list):
                self.run_index = 0
            self.image = (pg.transform.scale(self.run_list[int(self.run_index)], (self.width, self.height)))

        if key[pg.K_s] and self.flipped:
            self.run_index += self.run_animation_speed
            if self.run_index >= len(self.run_list):
                self.run_index = 0
            self.image = pg.transform.flip(pg.transform.scale(self.run_list[int(self.run_index)], (self.width, self.height)), True, False)

        if key[pg.K_s] and not self.flipped:
            self.run_index += self.run_animation_speed
            if self.run_index >= len(self.run_list):
                self.run_index = 0
            self.image = (pg.transform.scale(self.run_list[int(self.run_index)], (self.width, self.height)))

    def __init__(self):
        super().__init__()
        self.run_list = [pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run", f"run_{i}.png")) for i in range(6)]
        self.run_index = 0
        self.run_animation_speed = 0.1

        self.idle_list = [pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "idle", f"idle_{i}.png")) for i in range(5)]
        self.idle_index = 0
        self.idle_animation_speed = 0.05

        self.width = 100
        self.height = 100

        self.health = 5

        self.dx = 0
        self.dy = 0

        self.accerleration = 7

        self.flipped = False

        self.space_down = False

        self.image = pg.transform.scale(self.idle_list[self.idle_index], (self.width, self.height))
        self.rect = self.image.get_rect(center = (settings.WIDTH//2, settings.HEIGHT//2))

    def movement(self):
        self.dx = 0
        self.dy = 0

        key = pg.key.get_pressed()
        if key[pg.K_d]:
            self.dx += self.accerleration
        if key[pg.K_a]:
            self.dx -= self.accerleration
        if key[pg.K_w]:
            self.dy -= self.accerleration
        if key[pg.K_s]:
            self.dy += self.accerleration

    def collision_with_tiles(self):
        for tile in level.tile_list:
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                self.dy = 0

        self.rect.x += self.dx
        self.rect.y += self.dy

    def shoot(self):
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self.space_down = True
        elif self.space_down:
            if not self.flipped:
                bullet_group.add(Bullet(self.rect.midright, self.flipped))
            else:
                bullet_group.add(Bullet(self.rect.midleft, self.flipped))
            self.space_down = False

    def loose_health(self):
        # only temporary key for testing; gonna change that for collision with something
        key = pg.key.get_pressed()
        if key[pg.K_k]:
            event = pg.event.Event(LOOSE_HEALTH)
            pg.event.post(event)

    def update(self):
        self.loose_health()
        self.shoot()
        self.idle_animation()
        self.run_animation() 
        self.collision_with_tiles()      	
        self.movement()

player = pg.sprite.GroupSingle(Player())