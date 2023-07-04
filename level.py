import pygame as pg
import os 
from settings import *

level = [
    [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,7]
]

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

        corner_block_fyDOWN = 8
        corner_block_fyUP = 10

        corner_block_fxRIGHT_DOWN = 11
        corner_block_fxLEFT_UP = 12

        blank = 9
        '''
        self.tile_list = []

        corner_block_fyDOWN = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner_block.png"))
        corner_block_fyUP = pg.transform.rotate(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner_block.png")), 270)
        corner_block_fx_LEFT_UP = pg.transform.rotate(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner_block.png")), 180)
        corner_block_fx_RIGHT_DOWN = pg.transform.rotate(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner_block.png")), 90)

        left_wall = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "left_wall.png"))
        right_wall = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "right_wall.png"))
        upper_wall = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "upper_wall.png"))
        downer_wall = pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "downer_wall.png"))
        
        upright_corner = pg.transform.rotate(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner.png")), 270)
        downright_corner = pg.transform.rotate(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner.png")), 360)
        upleft_corner = pg.transform.rotate(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner.png")), 180)
        downleft_corner = pg.transform.rotate(pg.image.load(os.path.join("OneDrive", "Desktop", "shooter_game", "assets", "tiles", "corner.png")), 90)

        self.tile_size = 80

        row_counter = 0
        for row in level_data:
            column_counter = 0
            for column in row:
                if column == 0:
                    image = pg.transform.scale(upper_wall, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 1:
                    image = pg.transform.scale(left_wall, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 2:
                    image = pg.transform.scale(right_wall, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 3:
                    image = pg.transform.scale(downer_wall, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 4:
                    image = pg.transform.scale(upright_corner, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 5:
                    image = pg.transform.scale(downright_corner, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 6:
                    image = pg.transform.scale(upleft_corner, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 7:
                    image = pg.transform.scale(downleft_corner, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                if column == 8:
                    image = pg.transform.scale(corner_block_fyDOWN, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile)                    
                if column == 10:
                    image = pg.transform.scale(corner_block_fyUP, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile)      
                if column == 11:
                    image = pg.transform.scale(corner_block_fx_LEFT_UP, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile)  
                if column == 12:
                    image = pg.transform.scale(corner_block_fx_RIGHT_DOWN, (self.tile_size, self.tile_size))
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * self.tile_size
                    image_rect.y = row_counter * self.tile_size

                    tile = (image, image_rect)
                    self.tile_list.append(tile) 

                column_counter += 1
            row_counter += 1
        
    def draw_tiles(self):
        for sprite in self.tile_list:
            screen.blit(sprite[0], sprite[1])

level = Level(level)