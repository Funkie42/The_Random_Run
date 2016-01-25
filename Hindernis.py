import pymunk, pygame, cProfile
from pygame.locals import*


class Hindernis():
    def __init__(self, sprite, moveSpeed, mass, feuerrate):
        self.moveSpeed = moveSpeed
        self.feuerrate = feuerrate
        self.sprite_iterator = 0
        self.sprite = sprite
        self.reihe = 0
        self.spalte = 0
        self.direction = 1
        self.rect = self.current_sprite().get_rect()
        self.hitpoints = 4
        self.mass = mass
        self.sprite_counter = 5
        self.body = pymunk.Body(self.mass, pymunk.inf)
        self.kugel_counter = 0
        
    def center_rect(self):
        x = self.rect
        x.center = self.body.position
        return x


class Gegner(Hindernis):
    def __init__(self, block, moveSpeed, sprite, mass, feuerrate): #########!!!!!!!!!!!!!!!
        Hindernis.__init__(self,sprite, moveSpeed, mass, feuerrate)
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

    def remove(self, space):
        space.remove(self.body, self.shape)

    def engage(self, x): #####!!!!!!!!!!
        self.body.velocity.y = -250
        self.moveSpeed += 3
        if x > self.body.position.x:
            self.body.velocity.x = 200
            self.direction = 1
        else:
            self.body.velocity.x = -200
            self.direction = -1

    def current_sprite(self):
        if self.direction == 1:
            x = self.sprite.get_image(self.spalte * self.sprite.sprite_sheet.get_width()/12 + 25 , 8, self.sprite.sprite_sheet.get_width()/12 - 60 , self.sprite.sprite_sheet.get_height() -25)
            x = pygame.transform.scale(x, (90, 115))
            return x
        else:
            x = pygame.transform.flip(self.sprite.get_image(self.spalte * self.sprite.sprite_sheet.get_width()/12 + 25,8, self.sprite.sprite_sheet.get_width()/12 -60, self.sprite.sprite_sheet.get_height() -25), True, False)
            x = pygame.transform.scale(x, (90, 115))
            return x

        
    def update(self):
        if self.body.position.x > self.block.rect.right + 50:
            self.hitpoints = 0
        if self.body.position.x < self.block.rect.left - 50:
            self.hitpoints = 0
        if self.kugel_counter < self.feuerrate:
            self.kugel_counter += 1
        else:
            self.kugel_counter = 0
        
        if self.rect.right >= self.block.rect.right:
            self.direction = -1
        if self.rect.left <= self.block.rect.left:
            self.direction = 1
        self.body.position.x += self.moveSpeed * self.direction
        if self.sprite_iterator >= 0:
                                if self.spalte <= 10:
                                        self.spalte += 1
                                else:
                                        self.spalte = 0
                                self.sprite_iterator = 0
        else:
                                self.sprite_iterator += 1

class FliegenderGegner(Hindernis):
    def __init__(self, anfang, ende, topOrleft, moveSpeed, sprite, mass, feuerrate, waagrecht=True): ##!!!!
        Hindernis.__init__(self, sprite, moveSpeed, mass, feuerrate) ####!!!!!!
        self.anfang = anfang
        self.ende = ende
        self.waagrecht = waagrecht
        if self.waagrecht:
            self.rect.top = topOrleft
            self.rect.left = self.anfang + 1
        else:
            self.rect.top = self.anfang + 1
            self.rect.left = topOrleft
        #self.body = pymunk.Body()
        self.body.position = self.rect.center
        self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
        self.shape.collision_type = 6
        self.shape.sprite_group = 2 #########!!!!!!!!!!!

    def init(self, space):
        space.add(self.shape)

    def remove(self, space):
        space.remove(self.shape)

    def current_sprite(self):
        if self.direction == 1:
            x = self.sprite.get_image(0, self.reihe*self.sprite.sprite_sheet.get_height()/4, self.sprite.sprite_sheet.get_width(), self.sprite.sprite_sheet.get_height()/4)
            x = pygame.transform.scale(x, (90, 90))
            return x
        else:
            x = pygame.transform.flip(self.sprite.get_image(0, self.reihe*self.sprite.sprite_sheet.get_height()/4, self.sprite.sprite_sheet.get_width(), self.sprite.sprite_sheet.get_height()/4), True, False)
            x = pygame.transform.scale(x, (90, 90))
            return x

    def course(self):
        if self.waagrecht:
            self.body.position.x += self.moveSpeed * self.direction
        else:
            self.body.position.y += self.moveSpeed * self.direction

    def engage(self, x): #####!!!!!!!!!!
        self.moveSpeed += 3

    def update(self):
        self.sprite_counter += 1
        if self.kugel_counter < self.feuerrate: ###############!!!!!!!!!!!!!!!!!!!!!!!
            self.kugel_counter += 1
        else:
            self.kugel_counter = 0
            
        if self.waagrecht:
            if self.rect.right >= self.ende:
                self.direction = -1
            if self.rect.left <= self.anfang:
                self.direction = 1
        else:
            if self.rect.top >= self.ende:
                self.direction = -1
            if self.rect.top <= self.anfang:
                self.direction = 1
        self.course()
        if self.sprite_counter >= 15:
            self.sprite_counter = 0
            if self.reihe < 3:
                self.reihe += 1
            else:
                self.reihe = 0
        
