import pygame as pg
import os 
import settings

level_0 = [
    [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,7]
]

level_01 = [
    [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,11],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,12],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,7]
]

level_02 = [
    [4,0,0,0,0,10,9,9,9,9,11,0,0,0,0,6],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,11],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,12],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,7]
]

level_03 = [
    [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2],
    [5,3,3,3,3,8,9,9,9,9,12,3,3,3,3,7]
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
                if column == 8:
                    image = corner_block_fyDOWN
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile)                    
                if column == 10:
                    image = corner_block_fyUP
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile)      
                if column == 11:
                    image = corner_block_fx_LEFT_UP
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile)  
                if column == 12:
                    image = corner_block_fx_RIGHT_DOWN
                    image_rect = image.get_rect()

                    image_rect.x = column_counter * 80
                    image_rect.y = row_counter * 80

                    tile = (image, image_rect)
                    self.tile_list.append(tile) 
                column_counter += 1
            row_counter += 1
        
    def draw_tiles(self):
        for sprite in self.tile_list:
            settings.screen.blit(sprite[0], sprite[1])

level = Level(level_0)