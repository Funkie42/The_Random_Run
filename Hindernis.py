import pymunk, pygame, cProfile
from pygame.locals import*


class Hindernis():
    def __init__(self, sprite, moveSpeed, mass, feuerrate):
        self.moveSpeed = moveSpeed
        self.baseMoveSpeed = moveSpeed
        self.feuerrate = feuerrate
        self.sprite_iterator = 0
        self.sprite = sprite
        self.reihe = 0
        self.spalte = 0
        self.direction = 1
        self.sprites1 = []
        self.sprites2 = []
        self.make_sprites()
        self.rect = self.current_sprite().get_rect()
        self.hitpoints = 5
        self.baseHitpoints = self.hitpoints
        self.dead = False
        self.mass = mass
        self.sprite_counter = 5
        self.sprite_iterator = 0
        self.body = pymunk.Body(self.mass, pymunk.inf)
        self.kugel_counter = 0

        
        

        
    def center_rect(self):
        x = self.rect
        x.center = self.body.position
        return x

class Gegner(Hindernis):
    def __init__(self, block, moveSpeed, sprite, mass, feuerrate, sprite_type=0): 
        self.sprite_type = sprite_type
        Hindernis.__init__(self,sprite, moveSpeed, mass, feuerrate)
        self.hitpoints = self.hitpoints + 4 * self.sprite_type
        self.block = block
        self.rect.left = self.block.rect.left + 1
        self.rect.top = self.block.rect.top - self.current_sprite().get_height()
        self.body.position = self.rect.center
        self.start = self.rect.center
        self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
        self.shape.collision_type = 3
        self.shape.sprite_group = 2
        self.direction = 1

    def init(self, space):
        space.add(self.body, self.shape)

    def remove(self, space):
        space.remove(self.body, self.shape)

    def engage(self, x): 
        self.body.velocity.y = -250
        self.moveSpeed += 3
        if x > self.body.position.x:
            self.body.velocity.x = 200
            self.direction = 1
        else:
            self.body.velocity.x = -200
            self.direction = -1
            
    def make_sprites(self):
        if self.sprite_type == 0:
            for i in range(0,12):
                x = self.sprite.get_image(i * self.sprite.sprite_sheet.get_width()/12 + 25 , 8, self.sprite.sprite_sheet.get_width()/12 - 60 , self.sprite.sprite_sheet.get_height() -25)
                x = pygame.transform.scale(x, (90, 110)).convert()
                self.sprites1.append(x)
                self.sprites2.append(pygame.transform.flip(x,True,False))
                
        else:
            for i in range(0,13):
                x = self.sprite.get_image(i * self.sprite.sprite_sheet.get_width()/13 + 25 , 8, self.sprite.sprite_sheet.get_width()/13 - 60 , self.sprite.sprite_sheet.get_height() -10)
                x = pygame.transform.scale(x, (90, 120)).convert()
                self.sprites1.append(x)
                self.sprites2.append(pygame.transform.flip(x,True,False))            
    def current_sprite(self):
                if self.direction == 1:
                    return self.sprites1[self.spalte]
                else:
                    return self.sprites2[self.spalte]

        
    def update(self):
        if self.body.position.x > self.block.rect.right + 50:
            self.hitpoints = 0
        if self.body.position.x < self.block.rect.left - 50:
            self.hitpoints = 0
        if self.kugel_counter < self.feuerrate and self.sprite_type == 0:
            self.kugel_counter += 1
        else:
            self.kugel_counter = 0
        
        if self.rect.right >= self.block.rect.right:
            self.direction = -1
        if self.rect.left <= self.block.rect.left:
            self.direction = 1
        self.body.velocity.x = self.moveSpeed * self.direction * 15
        if self.sprite_type == 0:
            if self.spalte <= 10:
                self.spalte += 1
            else:
                self.spalte = 0
        else:
            if self.sprite_iterator >= 1:
                if self.spalte <= 10:
                    self.spalte += 1
                else:
                    self.spalte = 0
                self.sprite_iterator = 0
            else:
                self.sprite_iterator += 1

class FliegenderGegner(Hindernis):
    def __init__(self, anfang, ende, topOrleft, moveSpeed, sprite, mass, feuerrate, waagrecht=True):
        Hindernis.__init__(self, sprite, moveSpeed, mass, feuerrate)
        self.anfang = anfang
        self.ende = ende
        self.waagrecht = waagrecht
        self.start = 0
        if self.waagrecht:
            self.rect.top = topOrleft
            self.rect.left = self.anfang + 1
            self.start = (self.anfang + 1, topOrleft)
        else:
            self.rect.top = self.anfang + 1
            self.rect.left = topOrleft
            self.start = (topOrleft, self.rect.top)
        self.body.position = self.rect.center
        self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
        self.shape.collision_type = 6
        self.shape.sprite_group = 2
        self.hitpoints = 4
        self.baseHitpoints = self.hitpoints

    def make_sprites(self):
        for i in range(0,4):
            x = self.sprite.get_image(i * self.sprite.sprite_sheet.get_width()/4 + 25 , 8, self.sprite.sprite_sheet.get_width()/4 - 60 , self.sprite.sprite_sheet.get_height() -10)
            x = pygame.transform.scale(x, (90, 90)).convert()
            self.sprites1.append(x)
            self.sprites2.append(pygame.transform.flip(x,True,False))            
        
    def init(self, space):
        space.add(self.shape)

    def remove(self, space):
        space.remove(self.shape)

    def current_sprite(self):
        if self.direction == 1:
            return self.sprites1[self.reihe]
        else:
            return self.sprites2[self.reihe]

    def course(self):
        if self.waagrecht:
            self.body.position.x += self.moveSpeed * self.direction
        else:
            self.body.position.y += self.moveSpeed * self.direction

    def engage(self, x):
        self.moveSpeed += 3

    def update(self):
        self.sprite_counter += 1
        if self.kugel_counter < self.feuerrate: 
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
        if self.sprite_counter >= 5:
            self.sprite_counter = 0
            if self.reihe < 3:
                self.reihe += 1
            else:
                self.reihe = 0
        
class Endgegner(FliegenderGegner):
    def __init__(self, anfang, ende, topOrleft, moveSpeed, sprite, mass, feuerrate, waagrecht=True):
        FliegenderGegner.__init__(self, anfang, ende, topOrleft, moveSpeed, sprite, mass, feuerrate, waagrecht)
        self.endgegner = True
        self.hitpoints = 27
        self.body.velocity_func = self.slow_space
        self.shape.collision_type = 6

    def slow_space(self, body, gravity, damping, dt):
        body.velocity.y = 0
        if body.velocity.x > 1:
            body.velocity.x = 1
        elif body.velocity.x < -1:
            body.velocity.x = -1
            
    def make_sprites(self):
        for i in range(0,7):
            x = self.sprite.get_image(self.spalte * self.sprite.sprite_sheet.get_width()/7 + 10 , 80, self.sprite.sprite_sheet.get_width()/7 - 50 , self.sprite.sprite_sheet.get_height() -100).convert()
            x = pygame.transform.scale(x, (250, 175)).convert()
            self.sprites1.append(x)
            self.sprites2.append(pygame.transform.flip(x,True,False))
            
    def update(self):
        if self.kugel_counter < self.feuerrate: 
            self.kugel_counter += 1
        else:
            self.kugel_counter = 0
        if self.rect.right >= self.ende:
            self.direction = -1
        if self.rect.left <= self.anfang:
            self.direction = 1
        self.course()
        
        if self.spalte <= 5:
            self.spalte += 1
        else:
            self.spalte = 0
        
        if self.hitpoints == 10 or self.hitpoints == 5:
            self.moveSpeed += 15
            self.feuerrate = 8
            self.hitpoints -= 1
            

        
