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

class Stein(Boden):
                def __init__(self, block,  sprite):
                        self.x = block.rect.left + 20
                        self.y = block.rect.top - 60
                        self.direction = 1
                        self.sprite = sprite
                        self.sprite_iterator = 0
                        self.reihe = 0
                        self.rect = self.current_sprite().get_rect()
                        self.body = pymunk.Body(100, pymunk.inf)
                        self.body.position = (self.x, self.y)
                        self.body.velocity_func = self.slow_space
                        self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
                        self.shape.collision_type = 8
                        self.sprite_counter = 0

                def slow_space(self, body, gravity, damping, dt):
                        gravity = (0, -500)

                def respawn(self):
                        self.body.position = (self.x, self.y)
                        self.body.velocity.x = 0
                        self.body.velocity.y = 0

                def current_sprite(self):
                        if self.direction == 1:
                            return self.sprite.get_image(0 , self.reihe * self.sprite.sprite_sheet.get_height()/3, self.sprite.sprite_sheet.get_width(), self.sprite.sprite_sheet.get_height()/3)
                        else:
                            return pygame.transform.flip(self.sprite.get_image(0 , self.reihe * self.sprite.sprite_sheet.get_height()/3, self.sprite.sprite_sheet.get_width(), self.sprite.sprite_sheet.get_height()/3), True, False)

                def center_rect(self):
                        x = self.rect
                        x.center = self.body.position
                        return x

                def update(self):
                        keys = pygame.key.get_pressed()
                        if self.direction == 1 and keys[K_LEFT] and not keys[K_RIGHT]:
                                self.direction = -1
                                self.body.position.x += 200
                        elif self.direction == -1 and keys[K_RIGHT] and not keys[K_LEFT]:
                                self.direction = 1
                                self.body.position.x -= 200
                        
                        self.sprite_counter += 1
                        if self.sprite_counter >= 2:
                                        self.sprite_iterator += 1
                                        self.sprite_counter = 0
                                        if self.sprite_iterator >= 1:
                                                if self.reihe < 2:
                                                        self.reihe += 1
                                                else:
                                                        self.reihe = 0
                                        else:
                                                self.sprite_iterator += 1
                                                                                
