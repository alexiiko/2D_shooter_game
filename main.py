import pygame as pg
import os
from sys import exit

screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
pg.display.set_caption('Shooter Game')

screen_info = pg.display.Info()

WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h

FPS = 60

clock = pg.time.Clock()

#TODO: finish shooting for player (invert bullet direction if player is flipped)
#TODO: make crosshair

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 125
        self.height = 125

        self.move_x = 5
        self.move_y = 5

        self.flipped = False

        self.run_list = []
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run", "run_1.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run", "run_2.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run", "run_3.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run", "run_4.png")))
        self.run_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "run", "run_5.png")))
        self.run_index = 0
        self.run_animation_speed = 0.1

        self.idle_list = []
        self.idle_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "idle", "idle_1.png")))
        self.idle_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "idle", "idle_2.png")))
        self.idle_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "idle", "idle_3.png")))
        self.idle_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "idle", "idle_4.png")))
        self.idle_list.append(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "player", "idle", "idle_5.png")))
        self.idle_index = 0
        self.idle_animation_speed = 0.05

        self.image = pg.transform.scale(self.idle_list[self.idle_index], (self.width, self.height))
        self.rect = self.image.get_rect(center = (WIDTH//2, HEIGHT//2))


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

    def movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_d]:
            self.rect.x += self.move_x
        if key[pg.K_a]:
            self.rect.x -= self.move_x
        if key[pg.K_w]:
            self.rect.y -= self.move_y
        if key[pg.K_s]:
            self.rect.y += self.move_y

    def border(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0
    
    def shoot(self):
         key = pg.key.get_pressed()
         if key[pg.K_SPACE]:
             bullet_group.add(Bullet((self.rect.center)))

    def update(self):
        self.shoot()
        self.border()
        self.idle_animation()
        self.run_animation()     
        self.movement()      	

player = pg.sprite.GroupSingle()
player.add(Player())    

class Bullet(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "flying_bullet.png"))
        self.rect = self.image.get_rect()
        
        self.bullet_speed = 10

        self.rect.center = (center) 

    def move(self):
        self.rect.x += self.bullet_speed    
        if self.rect.left >= WIDTH or self.rect.right <= 0:
            self.kill()

    def update(self):
        self.move()

bullet_group = pg.sprite.Group()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill("white")
    
    player.draw(screen)
    player.update()

    bullet_group.draw(screen)
    bullet_group.update()

    pg.display.update()
    clock.tick(FPS)
