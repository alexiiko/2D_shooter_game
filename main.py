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

pg.mouse.set_visible(False)


#TODO: start to create levels with level data 
#TODO: implement life bar

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
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

        self.width = 100
        self.height = 100

        self.health = 5

        self.dx = 5
        self.dy = 5

        self.accerleration = 7

        self.flipped = False

        self.space_down = False


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
            self.rect.x += self.accerleration
        if key[pg.K_a]:
            self.rect.x-= self.accerleration
        if key[pg.K_w]:
            self.rect.y -= self.accerleration
        if key[pg.K_s]:
            self.rect.y += self.accerleration

    def collision_with_tiles(self):
        for tile in level.tile_list:    
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.accerleration = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                self.accerleration = 0

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
            self.space_down = True
        elif self.space_down:
            if not self.flipped:
                bullet_group.add(Bullet(self.rect.midright, self.flipped))
            else:
                bullet_group.add(Bullet(self.rect.midleft, self.flipped))
            self.space_down = False

            

    def update(self):
        self.collision_with_tiles()      	
        self.movement()
        self.shoot()
        self.border()
        self.idle_animation()
        self.run_animation()     

player = pg.sprite.GroupSingle(Player())
    

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

# almost same class but another sprite for the mouse (picture you actually see)
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

        if self.rect.left >= WIDTH or self.rect.right <= 0:
            self.kill()

    def update(self):
        self.move() 

bullet_group = pg.sprite.Group()

class Level():
    def __init__(self, level_data):
        '''
        upper_wall = 0
        left_wall = 1
        right_wall = 2
        downer_wall = 3
        upright_corner = 4
        downright_corner = 5
        upleft_corner = 6
        downleft_corner = 7

        blank = 8
        '''
        self.tile_list = []

        left_wall = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "left_wall.png"))
        right_wall = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "right_wall.png"))
        upper_wall = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "upper_wall.png"))
        downer_wall = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "downer_wall.png"))
        
        corner = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner.png"))
        upright_corner = pg.transform.rotate(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner.png")), 270)
        downright_corner = pg.transform.rotate(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner.png")), 360)
        upleft_corner = pg.transform.rotate(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner.png")), 180)
        downleft_corner = pg.transform.rotate(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner.png")), 90)

        row_counter = 0
        for row in level_data:
            column_counter = 0
            for column in row:
                if column == 0:
                    image = upper_wall
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 1:
                    image = left_wall
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 2:
                    image = right_wall
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 3:
                    image = downer_wall
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 4:
                    image = upright_corner
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 5:
                    image = downright_corner
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 6:
                    image = upleft_corner
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 7:
                    image = downleft_corner
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                    
                column_counter += 1
            row_counter += 1
        
    def draw_tiles(self):
        for sprite in self.tile_list:
            screen.blit(sprite[0], sprite[1])



level_data = [
    [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
    [1,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2],
    [1,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2],
    [1,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2],
    [1,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2],
    [1,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2],
    [1,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2],
    [1,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2],
    [5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,7]
]

level = Level(level_data)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN and pg.K_ESCAPE:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()                

    screen.fill("#6584AA")

    level.draw_tiles()

    player.draw(screen)
    player.update()

    crosshair.draw(screen)
    crosshair.update()
    crosshair_picture.draw(screen)
    crosshair_picture.update()

    bullet_group.draw(screen)
    bullet_group.update()

    pg.display.update()
    clock.tick(FPS)