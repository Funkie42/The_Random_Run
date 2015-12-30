import pygame, pymunk
from pygame.locals import*

class Power_Up(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class High_Jump(Power_Up):
    def __init__(self, block, sprite_list):
        self.sprite_list = sprite_list
        self.sprite_iterator = 0
        self.body = pymunk.Body(500, pymunk.inf)
        self.rect = self.sprite_list[0].get_rect()
        self.rect.left = block.rect.left
        self.rect.top = block.rect.top - self.sprite_list[0].get_height()
        self.body.position = self.rect.center
        self.shape = pymunk.Poly.create_box(self.body, (self.sprite_list[0].get_width(), self.sprite_list[0].get_height()))
        self.shape.collision_type = 5
        self.shape.group = 2



        
