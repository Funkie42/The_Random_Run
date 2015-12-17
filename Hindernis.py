import pymunk, pygame
from pygame.locals import*

class Hindernis():
    def __init__(self, moveSpeed, sprite_list, mass):
        self.moveSpeed = moveSpeed
        self.sprite_iterator = 0
        self.sprite_list = sprite_list
        self.rect = self.current_sprite().get_rect()
        
        self.mass = mass
        self.direction = 1
        self.sprite_counter = 5
        self.body = pymunk.Body(self.mass, pymunk.inf)
        
    def center_rect(self):
        x = self.rect
        x.center = self.body.position
        return x

    def current_sprite(self):
        if self.sprite_iterator >= len(self.sprite_list):
            self.sprite_iterator = 0
        return self.sprite_list[self.sprite_iterator]

    def rev_sprite_list(self):
                for i in range(len(self.sprite_list)):
                            self.sprite_list[i] = pygame.transform.flip(self.sprite_list[i], True, False)


class Gegner(Hindernis):
    def __init__(self, block, moveSpeed, sprite_list, mass):
        Hindernis.__init__(self, moveSpeed, sprite_list, mass)
        self.block = block
        self.rect.left = self.block.rect.left + 1
        self.rect.top = self.block.rect.top - self.current_sprite().get_height()
        self.body.position = self.rect.center
        self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
        self.shape.collision_type = 3

    def init(self, space):
        space.add(self.body, self.shape)
        
    def update(self):
        if self.rect.right >= self.block.rect.right:
            self.direction = -1
            self.rev_sprite_list()
        if self.rect.left <= self.block.rect.left:
            self.direction = 1
            self.rev_sprite_list()
        self.body.position.x += 1 * self.direction
        self.sprite_counter += 1
        if self.sprite_counter >= 3:
            self.sprite_iterator += 1
            self.sprite_counter = 0

class FliegenderGegner(Hindernis):
    def __init__(self, anfang, ende, top, moveSpeed, sprite_list, mass):
        Hindernis.__init__(self, moveSpeed, sprite_list, mass)
        self.anfang = anfang
        self.ende = ende
        self.rect.left = self.anfang + 1
        self.rect.top = top
        #self.body = pymunk.Body()
        self.body.position = self.rect.center
        self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
        self.shape.collision_type = 6

    def init(self, space):
        space.add(self.shape)

    def update(self):
        if self.rect.right >= self.ende:
            self.direction = -1
            self.rev_sprite_list()
        if self.rect.left <= self.anfang:
            self.direction = 1
            self.rev_sprite_list()
        self.body.position.x += 1 * self.direction
        self.sprite_counter += 1
        if self.sprite_counter >= 3:
            self.sprite_iterator += 1
            self.sprite_counter = 0
        
        
