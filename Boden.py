#<<<<<<< HEAD
import pygame, sys, pymunk
from pygame.locals import*

class Boden(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                
class Block(Boden):
        def __init__(self, rect, sprite):
                self.rect = rect
                self.sprite = sprite
                #self.sprite = pygame.transform.scale(self.sprite, (self.rect[2], self.rect[3]))
                self.surf = pygame.Surface((self.rect.width, self.rect.height))
                self.body = pymunk.Body()
                self.body.position = self.rect.center
                self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))
                self.shape.collision_type = 2
                
                
        def center_rect(self):
                x = self.rect
                x.center = self.body.position
                return x
                
        def update(self, rect):
                for i in range(0, self.surf.get_height(), self.sprite.get_height()):
                        for j in range(0, self.surf.get_width(), self.sprite.get_width()):
                                if rect.collidepoint(self.center_rect().left + j, self.center_rect().top + i):
                                        self.surf.blit(self.sprite, (j,i))
                                #pygame.draw.circle(self.surf, ((0,0,0)), (j, i), 10)

class Stein(Boden):
                def __init__(self, block,  sprite):
                        self.x = block.rect.left + 20
                        radius = 40
                        self.y = block.rect.top - int(radius) -5
                        self.sprite = sprite
                        self.rect = pygame.Rect(0,0,self.sprite.get_width(), self.sprite.get_height())
                        self.body = pymunk.Body(100, pymunk.moment_for_circle(1, 100, 40))
                        self.body.position = (self.x, self.y)
                        self.body.velocity_func = self.slow_space
                        self.shape = pymunk.Circle(self.body, 40)
                        self.shape.collision_type = 8

                def slow_space(self, body, gravity, damping, dt):
                        gravity = (0, -500)

                def center_rect(self):
                        x = self.rect
                        x.center = self.body.position
                        return x
                                                                                
