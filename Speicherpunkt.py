import pymunk, pygame
from pygame.locals import *

class Speicherpunkt():
    def __init__(self, block, sprite_list):
        self.sprite_list = sprite_list
        self.sprite_iterator = 0
        self.body = pymunk.Body()
        self.rect = self.sprite_list[0].get_rect()
        self.rect.left = block.rect.left
        self.rect.top = block.rect.top - self.sprite_list[0].get_height()
        self.body.position = self.rect.center
        self.shape = pymunk.Poly.create_box(self.body, (self.sprite_list[0].get_width(), self.sprite_list[0].get_height()))

class Portal():
        def __init__(self, block, sprite_list):
            self.sprite_list = sprite_list
            self.sprite_iterator = 0
            self.body = pymunk.Body()
            self.rect = self.sprite_list[0].get_rect()
            self.rect.left = block.rect.left
            self.rect.top = block.rect.top - self.sprite_list[0].get_height()
            self.body.position = self.rect.center
            self.shape = pymunk.Poly.create_box(self.body, (self.sprite_list[0].get_width(), self.sprite_list[0].get_height()))
            self.shape.collision_type = 7
    
