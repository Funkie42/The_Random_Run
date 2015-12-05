import pymunk, pygame
from pygame.locals import*

class Hindernis(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Gegner(Hindernis):
    def __init__(self, block, moveSpeed, sprite_list, mass):
        Hindernis.__init__(self)
        self.block = block
        self.moveSpeed = moveSpeed
        self.sprite_iterator = 0
        self.sprite_list = sprite_list
        self.rect = self.current_sprite().get_rect()
        self.rect.left = self.block.rect.left
        self.rect.top = self.block.rect.top - self.current_sprite().get_height() - 30
        self.rev_sprite_list()
        self.sprite_counter = 5
        
        
        self.mass = mass
        self.body = pymunk.Body(self.mass, pymunk.moment_for_box(self.mass, self.current_sprite().get_width(), self.current_sprite().get_height()))
        self.body.position = self.rect.center
        self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
        self.direction = 1

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

    def blit_surf(self):
        surf = pygame.transform.rotate(self.current_sprite(), self.body.angle)
        return surf


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
        

        
    
