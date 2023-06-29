import pygame as pg
import os 
import settings
import level

class Bullet(pg.sprite.Sprite):
    def __init__(self, player_pos, player_flipped):
        super().__init__()
        self.image = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "flying_bullet.png"))
        self.rect = self.image.get_rect()
        
        self.bullet_speed = 10

        self.rect.center = (player_pos)

        self.direction = player_flipped

    def move(self):
        if self.direction == False:
            self.rect.x += self.bullet_speed    
        else:
            self.rect.x -= self.bullet_speed

    def out_of_bounce(self):
        if self.rect.left >= settings.WIDTH or self.rect.right <= 0:
            self.kill()

    def collision_with_wall(self):
        for tile in level.level.tile_list:
            if tile[1].colliderect(self.rect):
                self.kill()

    def update(self):
        self.collision_with_wall()
        self.move() 
        self.out_of_bounce()

bullet_group = pg.sprite.Group()