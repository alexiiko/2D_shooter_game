import pygame as pg
import os
from settings import *

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.walk = [pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "enemy", "walk", f"walk_{i}.png")) for i in range(6)]
        self.walk_index = 0
        self.walk_speed = 0.2

        self.idle = [pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "enemy", "idle", f"idle_{j}.png")) for j in range(4)]
        self.idle_index = 0
        self.idle_speed = 0.050

        self.health = 10
        self.speed = 5

        self.dx = 0
        self.dy = 0

        self.width = 100
        self.height = 100

        self.image = pg.transform.scale(self.idle[self.idle_index], (self.width, self.height))
        self.rect = self.image.get_rect(center = (WIDTH//2 + 100, HEIGHT//2))

    def walk_animation(self):
        pass

    def idle_animation(self):
        self.idle_index += self.idle_speed
        if self.idle_index >= len(self.idle):
            self.idle_index = 0
        self.image = pg.transform.scale(self.idle[int(self.idle_index)], (self.width, self.height))

    def move(self):
        pass

    def attack_player(self):
        pass

    def die(self):
        pass

    def respawn(self):
        pass

    def update(self):
        self.idle_animation()

enemy_group = pg.sprite.Group()
enemy_group.add(Enemy())