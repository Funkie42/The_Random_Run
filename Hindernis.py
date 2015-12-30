import pymunk, pygame
from pygame.locals import*

class Hindernis():
    def __init__(self, sprite, moveSpeed, mass):
        self.moveSpeed = moveSpeed
        self.sprite_iterator = 0
        self.sprite = sprite
        self.reihe = 0
        self.spalte = 0
        self.direction = 1
        self.rect = self.current_sprite().get_rect()
        
        self.mass = mass
        self.sprite_counter = 5
        self.body = pymunk.Body(self.mass, pymunk.inf)
        
    def center_rect(self):
        x = self.rect
        x.center = self.body.position
        return x

    def current_sprite(self):
        if self.direction == 1:
            return self.sprite.get_image(self.spalte * self.sprite.sprite_sheet.get_width()/7 , self.reihe * self.sprite.sprite_sheet.get_height()/3, self.sprite.sprite_sheet.get_width()/7, self.sprite.sprite_sheet.get_height()/3)
        else:
            return pygame.transform.flip(self.sprite.get_image(self.spalte * self.sprite.sprite_sheet.get_width()/7 , self.reihe * self.sprite.sprite_sheet.get_height()/3, self.sprite.sprite_sheet.get_width()/7, self.sprite.sprite_sheet.get_height()/3), True, False)



class Gegner(Hindernis):
    def __init__(self, block, moveSpeed, sprite, mass):
        Hindernis.__init__(self,sprite, moveSpeed, mass)
        self.block = block
        self.rect.left = self.block.rect.left + 1
        self.rect.top = self.block.rect.top - self.current_sprite().get_height()
        self.body.position = self.rect.center
        self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
        self.shape.collision_type = 3
        self.shape.sprite_group = 2
        self.direction = 1

    def init(self, space):
        space.add(self.body, self.shape)
        
    def update(self):
        if self.rect.right >= self.block.rect.right:
            self.direction = -1
        if self.rect.left <= self.block.rect.left:
            self.direction = 1
        self.body.position.x += 1 * self.direction
        if self.sprite_iterator >= 1:
                                if self.spalte <= 5:
                                        self.spalte += 1
                                else:
                                        self.spalte = 0
                                        if self.reihe <= 1:
                                                self.reihe += 1
                                        else: self.reihe = 0
                                self.sprite_iterator = 0
        else:
                                self.sprite_iterator += 1

class FliegenderGegner(Hindernis):
    def __init__(self, anfang, ende, top, moveSpeed, sprite, mass):
        Hindernis.__init__(self, sprite, moveSpeed, mass)
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
        if self.rect.left <= self.anfang:
            self.direction = 1
        self.body.position.x += 1 * self.direction
        self.sprite_counter += 1
        if self.sprite_counter >= 3:
            self.sprite_iterator += 1
            self.sprite_counter = 0
        if self.sprite_iterator >= 1:
                                if self.spalte <= 5:
                                        self.spalte += 1
                                else:
                                        self.spalte = 0
                                        if self.reihe <= 1:
                                                self.reihe += 1
                                        else: self.reihe = 0
                                self.sprite_iterator = 0
        else:
                                self.sprite_iterator += 1
        
        
