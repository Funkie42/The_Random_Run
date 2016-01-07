import sys, pygame, pymunk, Boden, Hindernis, Power_Ups, SpriteSheet, Speicherpunkt, cProfile, copy
from pygame.locals import*
from copy import deepcopy

from Gameclient import *

playing_Spieler = 0
Multiplayer = False

class Spieler(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.sprite_iterator = 0

                self.reihe = 0
                self.spalte = 0
                
                self.state = 0 # 0 = stand, 1 = move, 2 = jump, 3 = fall, 4 = duck, 5 = roll, 6 = schlittern

                self.jump_force = (0,0)

                self.sprite = woman
                
                self.double_jump_iterator = 0

                self.direction = 1 #1 = rechts, -1 = links

                self.mass = 100
                self.moveSpeed = 1
                self.jumpPower = 650

                self.body = pymunk.Body(self.mass, pymunk.inf)
                self.body.position = (800, 1500)
                self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
                space.add(self.body, self.shape)
                self.shape.collision_type = 1

                self.dash_counter = 0
                self.double_jump_counter = 1

                self.is_Grounded = False
                self.is_alive = True

        def rect(self):
                x = pygame.Rect(0,0, self.current_sprite().get_width(), self.current_sprite().get_height())
                x.center = self.body.position
                return x

        def current_sprite(self):
                #return self.sprite_list[self.state][self.sprite_iterator]
                if self.direction == 1:
                        return self.sprite.get_image(15 + self.spalte * self.sprite.sprite_sheet.get_width()/7 ,  5 +self.reihe * self.sprite.sprite_sheet.get_height()/3, self.sprite.sprite_sheet.get_width()/7 - 35, self.sprite.sprite_sheet.get_height()/3 - 15)
                else:
                         return pygame.transform.flip(self.sprite.get_image(15 + self.spalte * self.sprite.sprite_sheet.get_width()/7 , 5 + self.reihe * self.sprite.sprite_sheet.get_height()/3, self.sprite.sprite_sheet.get_width()/7 - 35, self.sprite.sprite_sheet.get_height()/3 - 15), True, False)


        def state_update(self):
                keys = pygame.key.get_pressed()
                if self.direction == 1 and keys[K_LEFT] and not keys[K_RIGHT] and self.moveSpeed != 0:
                        self.direction = -1
                        #self.rev_sprite_list()
                elif self.direction == -1 and keys[K_RIGHT] and not keys[K_LEFT] and self.moveSpeed != 0:
                        self.direction = 1
                        #self.rev_sprite_list()
                if self.is_Grounded and not (keys[K_RIGHT] or keys[K_LEFT]):
                        self.state = 0
                elif self.is_Grounded and (keys[K_RIGHT] or keys[K_LEFT]):
                        self.state = 1     
                elif not self.is_Grounded:
                        self.state = 2

                        
        def jump(self):
                if s.body.velocity.y > 0:
                        self.body.velocity.y = -self.jumpPower
                else:
                        self.body.velocity.y = -self.jumpPower

        def move(self):
            self.body.position.x += self.direction * self.moveSpeed
            hintergrund_rect.left += 4 * self.direction

        def dash(self):
                if self.dash_counter > 0:
                        self.body.position.x += 60 * self.direction
                        self.dash_counter -= 1

        def selfblit(self):
                #if self.sprite_iterator >= len(self.sprite_list[self.state]):
                if self.state == 0:
                        self.spalte = 5
                        self.reihe = 1
                elif self.state == 1:
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
                elif self.state == 2:
                        self.reihe = 0
                        self.spalte = 0
                                        

                        
                LEVELSURF.blit(self.current_sprite(), self.rect())
                #self.sprite_iterator += 1
              


#WELT/LEVELKLASSE
class Welt():
        def __init__(self, BACKGROUNDSURF, boeden, hindernisse, power_ups, speicherpunkte, portal, spieler):
                self.BACKGROUNDSURF = BACKGROUNDSURF
                self.BACKGROUNDSURF = pygame.transform.scale(self.BACKGROUNDSURF, (int(LEVELSURF.get_width() * 2/3), DISPLAYSURF.get_height() + 25))
                self.boeden = boeden
                self.hindernisse = hindernisse
                self.power_ups = power_ups
                self.speicherpunkte = speicherpunkte
                self.portal = portal
                self.speicherpunkte.insert(0, Speicherpunkt.Speicherpunkt(self.boeden[0], [man1]))
                global current_speicherpunkt, hintergrund_rect, backup_hintergrund_rect
                current_speicherpunkt = self.speicherpunkte[0]
                backup_hintergrund_rect = hintergrund_rect
                self.spieler = spieler
                self.finish = False
                self.init = False

        def addToSpace(self):
                for i in self.boeden:
                        space.add(i.shape)
                for i in self.hindernisse:
                        i.init(space)
                for i in self.power_ups:
                        space.add(i.body, i.shape)
                for i in self.speicherpunkte:
                        space.add(i.shape)
                space.add(self.portal.shape)

        def removeFromSpace(self):
                for i in self.boeden:
                        space.remove(i.shape)
                for i in self.hindernisse:
                        i.remove(space)
                for i in self.power_ups:
                        space.remove(i.body, i.shape)
                for i in self.speicherpunkte:
                        space.remove(i.shape)
                space.remove(self.portal.shape)
               
        def update(self):
                global current_speicherpunkt
                if not self.init:
                        self.spieler.body.position.x = current_speicherpunkt.rect.left + 50
                        self.spieler.body.position.y = current_speicherpunkt.rect.top - 200
                        self.addToSpace()
                        self.init = True
                        
                self.spieler.state_update()
                
                for i in self.boeden:
                        if rect.colliderect(i.center_rect()) and i.center_rect().top < LEVELSURF.get_height() - 200:
                                i.update(rect)
                                LEVELSURF.blit(i.surf, (i.center_rect()))
                                #pygame.draw.polygon(LEVELSURF, ((34,66,34)), i.shape.get_vertices())
                               # pygame.draw.circle(LEVELSURF, ((4,5,6)), (int(i.body.position.x), int(i.body.position.y)), 10)
                               
                for i in self.hindernisse:
                        if i.body.position.y > LEVELSURF.get_height() - 200 and i in self.hindernisse: #evtl zu updaten
                                self.hindernisse.remove(i)
                                space.remove(i.body, i.shape)
                        if rect.colliderect(i.center_rect()):
                                LEVELSURF.blit(i.current_sprite(), i.center_rect())
                        i.update()
                                #pygame.draw.polygon(LEVELSURF, ((34,66,34)), i.shape.get_vertices())
                                #pygame.draw.circle(LEVELSURF, ((4,5,6)), (int(i.body.position.x), int(i.body.position.y)), 10)
                                
                for i in self.power_ups:
                        if i.body.position.y > LEVELSURF.get_height() - 200 and i in self.power_ups: #evtl zu updaten
                                self.power_ups.remove(i)
                                space.remove(i.body, i.shape)
                        i.rect.center = i.body.position
                        i.body.position = i.rect.center
                        i.body.velocity.x = 0
                        if rect.colliderect(i.rect):
                                LEVELSURF.blit(i.sprite_list[i.sprite_iterator], i.rect)

                global backup_hintergrund_rect
                global hintergrund_rect
                for i in self.speicherpunkte:
                         if rect.colliderect(i.rect):
                                LEVELSURF.blit(i.sprite_list[i.sprite_iterator], i.rect)
                         if self.spieler.rect().colliderect(i.rect):
                                 current_speicherpunkt = i
                                 backup_hintergrund_rect.left = hintergrund_rect.left
                                 self.speicherpunkte.remove(i)
                                 space.remove(i.shape)

                if rect.colliderect(self.portal.rect):
                                LEVELSURF.blit(self.portal.sprite_list[self.portal.sprite_iterator], self.portal.rect)
                                  
                if self.spieler.body.position.y > LEVELSURF.get_height() - 200:
                        self.spieler.is_alive = False
                if self.spieler.is_alive == False:
                        hintergrund_rect.left = backup_hintergrund_rect.left
                        self.spieler.body.velocity.y = -50
                        self.spieler.body.position = (current_speicherpunkt.rect.left + 50, current_speicherpunkt.rect.top - 200)
                        self.spieler.is_alive = True
                self.spieler.dash()
                self.spieler.body.reset_forces()
                self.spieler.selfblit()
                #print(self.spieler.spalte)
                #pygame.draw.polygon(LEVELSURF, ((76, 45, 98)), self.spieler.shape.get_vertices())
                #pygame.draw.circle(LEVELSURF, ((45,34,23)), (int(self.spieler.body.position.x), int(self.spieler.body.position.y)), 10)
                


class Kugel(object):
        def __init__(self, vec):
                object.__init__(self)
                self.vec = vec
                self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 10))
                self.body.position = (s.body.position.x +40 * s.direction, s.body.position.y - 40)
                self.shape = pymunk.Circle(self.body, 10)
                space.add(self.body, self.shape)
                self.body.apply_impulse(vec)
                kugeln.append(self)
                self.shape.collision_type = 4
                self.shape.elasticy = 1
                self.lebenszeit = 300
                self.shape.group = 1

        def update(self):
                pygame.draw.circle(LEVELSURF, ((0,0,0)), (int(self.body.position.x), int(self.body.position.y)), 10)
                if self.body.position.y > 7500 and self in kugeln or self.lebenszeit == 0:
                        kugeln.remove(self)
                        space.remove(self.body, self.shape)
                self.lebenszeit -= 1                        

# KAMERAFUNKTIONEN
def camera_blit():
        try:
                rect.center = s.body.position
                surf = LEVELSURF.subsurface(rect)
                return surf         
        except:
                if s.body.position.x < DISPLAYSURF.get_width()/2:
                        rect.left = 0
                if s.body.position.y < DISPLAYSURF.get_height()/2:
                        rect.top = 0
                if s.body.position.y >LEVELSURF.get_height() - DISPLAYSURF.get_height()/2:
                        rect.top = LEVELSURF.get_height() - DISPLAYSURF.get_height()
                if s.body.position.x >LEVELSURF.get_width() - DISPLAYSURF.get_width()/2:
                        rect.left = LEVELSURF.get_width() - DISPLAYSURF.get_width()
                surf = LEVELSURF.subsurface(rect)
                return surf

def hintergrund_blit():
        try:
                surf = current_level.BACKGROUNDSURF.subsurface(hintergrund_rect)
                return surf         
        except:
                hintergrund_rect.left = 0
                surf = current_level.BACKGROUNDSURF.subsurface(hintergrund_rect)
                return surf

#COLLISIONHANDLER

def touch(space, arbiter):
        if arbiter.contacts[0].normal.int_tuple[0] == 0:
                s.is_Grounded = True
                s.double_jump_counter = 1
                if current_level.spieler.body.velocity.x <= -50:
                        current_level.spieler.body.velocity.x += 25
                        current_level.spieler.moveSpeed = 0
                elif current_level.spieler.body.velocity.x >= 50:
                        current_level.spieler.body.velocity.x -= 25
                        current_level.spieler.moveSpeed = 0
                if -50 < current_level.spieler.body.velocity.x < 50:
                        current_level.spieler.body.velocity.x = 0
                        current_level.spieler.moveSpeed = 11
                return True

def cänt_touch_dis(space, arbiter):
        s.is_Grounded = False
        #print(s.is_Grounded)
        return True

def kugel_hits_gegner(space, arbiter):
        arbiter.shapes[0].body.velocity.y -= 400
        arbiter.shapes[0].body.velocity.x += 150 * current_level.spieler.direction
        arbiter.shapes[1].body.velocity.x = -150 * current_level.spieler.direction ##########################################
        return True

def kugel_hits_fliegender_gegner(space, arbiter):
        space.add(arbiter.shapes[0].body)
        arbiter.shapes[0].collision_type = 3
        arbiter.shapes[1].body.velocity.x = -150 * current_level.spieler.direction ########################################
        

def player_hits_kugel(space, arbiter):
        arbiter.shapes[1].body.velocity.y -= 1000
        arbiter.shapes[1].body.velocity.x += 1 * s.direction
        #print("DEPP")
        return True

def player_jumps_gegner(space, arbiter):
        if arbiter.contacts[0].normal.int_tuple[0] == 0:
                current_level.spieler.body.velocity.y = -650
                current_level.spieler.double_jump_counter = 1
                #print("HURA")
        else:
                current_level.spieler.body.velocity.x = -450 * current_level.spieler.direction
                current_level.spieler.body.velocity.y = -750
        return True

def player_jumps_fliegender_gegner(space, arbiter):
        if arbiter.contacts[0].normal.int_tuple[0] == 0:
                current_level.spieler.body.velocity.y = -650
                current_level.spieler.double_jump_counter = 1
                space.add(arbiter.shapes[1].body)
                arbiter.shapes[1].collision_type = 3
        else:
                current_level.spieler.body.velocity.x = -450 * current_level.spieler.direction
                current_level.spieler.body.velocity.y = -750
                current_level.spieler.moveSpeed = 0
        return True

def player_jumps_highjump(space, arbiter):
        if arbiter.contacts[0].normal.int_tuple[0] == 0:
                current_level.spieler.body.velocity.y = -1000
                current_level.spieler.double_jump_counter = 1
        else:
                arbiter.shapes[1].body.position.x += 5 * s.direction
        return True

def kugel_hits_highjump(space, arbiter):
        arbiter.shapes[1].body.position.x += 20 * s.direction
        arbiter.shapes[0].group = 2
        return True

def player_hits_portal(space, arbiter): ############################################## AHSJKLDHSALKDHASLKJDHLKASJDHALSKJDHL
        global current_level
        #current_level.removeFromSpace()
        current_level.removeFromSpace()
        current_level.finish = True
        current_level = game[game.index(current_level) + 1]
        return True
        

# UNIVERSELLE OPTIONEN
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
LEVELSURF = pygame.Surface((6000, 8000))
current_speicherpunkt = False
space = pymunk.Space()
space.collision_bias = 0.00001
current_speicherpunkt = False
#COLLISIONTYPES:
# 1 = SPIELER
# 2 = Böden
# 3 = Bodengegner
# 4 = Kugel
# 5 = Highjump
# 6 = fliegender Gegner
# 7 = Portal

#SPRITEGROUPS
# 1 = Kugel
# 2 = Highjump

space.add_collision_handler(1,2,post_solve=touch, separate=cänt_touch_dis)
space.add_collision_handler(3,4, begin=kugel_hits_gegner)
space.add_collision_handler(6,4, begin=kugel_hits_fliegender_gegner)
space.add_collision_handler(1,4, begin=player_hits_kugel)
space.add_collision_handler(1,3, begin=player_jumps_gegner)
space.add_collision_handler(1,6, begin=player_jumps_fliegender_gegner)
space.add_collision_handler(1,5, post_solve=player_jumps_highjump)
space.add_collision_handler(4,5, begin=kugel_hits_highjump)
space.add_collision_handler(1,7, begin=player_hits_portal)
space.gravity = (0, 1500)
clock = pygame.time.Clock()
fps = 25

#KAMERARECTS
rect = pygame.Rect(0,0,DISPLAYSURF.get_width(),DISPLAYSURF.get_height())
hintergrund_rect =pygame.Rect(0, 0, DISPLAYSURF.get_width() + 25, DISPLAYSURF.get_height() + 25)

#SPIELERSPRITES
man1 = pygame.image.load("Gui/man1.png")
man1 = pygame.transform.scale(man1,(80,100))

woman = SpriteSheet.SpriteSheet("Gui/player.png")

#GELÄNDESPRITES
mars = pygame.image.load("Gui/ground.png")
rinde = pygame.image.load("Gui/Rinde.jpg")
rinde = pygame.transform.scale(rinde, (100, 100))

#SPIELER
s = Spieler()

#LEVEL1
bl = Boden.Block(pygame.Rect(0,2000,1200,50), mars)
bl1 = Boden.Block(pygame.Rect(1700,2000,1200,50), mars)
bl2 = Boden.Block(pygame.Rect(2900,1700,750, 50), mars)
bl3 = Boden.Block(pygame.Rect(3650,1700,50, 800), mars)
bl4 = Boden.Block(pygame.Rect(3650, 2400,1450, 50), mars)
bl5 = Boden.Block(pygame.Rect(4400,2000,100, 50), mars)
bl5_2 = Boden.Block(pygame.Rect(4500,2000,550, 50), mars)
bl6 = Boden.Block(pygame.Rect(5100,2250,200, 200), mars)
bl6_2 = Boden.Block(pygame.Rect(5300,1700,50, 750), mars)
bl6_3 = Boden.Block(pygame.Rect(5100,1700,200, 50), mars)
bl6_4 = Boden.Block(pygame.Rect(5100,1450,50, 250), mars)
bl7 = Boden.Block(pygame.Rect(4550,1450,700, 50), mars)
bl8 = Boden.Block(pygame.Rect(4350,1300,50, 750), mars)
bl9 = Boden.Block(pygame.Rect(5450,1450,300, 50), mars)
bl9_2 = Boden.Block(pygame.Rect(5750,1450,400, 50), mars)
bl10 = Boden.Block(pygame.Rect(5950,1000,50, 450), mars)
bl11 = Boden.Block(pygame.Rect(5600,1800,400, 50), mars)
bl12 = Boden.Block(pygame.Rect(5700,2100,300, 50), mars)
bl13 = Boden.Block(pygame.Rect(5800,2400,200, 50), mars)
bl14 = Boden.Block(pygame.Rect(5800,2700,50, 50), mars)
bl15 = Boden.Block(pygame.Rect(5500,2900,50, 50), mars)
bl16 = Boden.Block(pygame.Rect(5200,3100,50, 50), mars)
bl17 = Boden.Block(pygame.Rect(4200,3100,250, 50), mars)
bl18 = Boden.Block(pygame.Rect(4200,3500, 250, 50), mars)

g = Hindernis.Gegner(bl2, 5, woman, 5)
g1 = Hindernis.Gegner(bl1, 5, woman, 5)
g2 = Hindernis.Gegner(bl4, 5, woman, 5)
g3 = Hindernis.Gegner(bl5_2, 1, woman, 5)
g4 = Hindernis.Gegner(bl7, 1, woman, 5)
g5 = Hindernis.Gegner(bl12, 10, woman, 5)

fg = Hindernis.FliegenderGegner(5350, 5800, 1600, 2, woman, 5)
fg1 = Hindernis.FliegenderGegner(4700, 5100, 3100, 5, woman, 5)
fg2 = Hindernis.FliegenderGegner(2100, 2200, 100, 2, woman, 5, False)

hj = Power_Ups.High_Jump(bl5, [man1])

sp = Speicherpunkt.Speicherpunkt(bl9_2, [man1])

p = Speicherpunkt.Portal(bl13, [man1])


w1 = Welt(pygame.image.load("Gui/mars_back.png"), [bl,bl1,bl2,bl3, bl4, bl5, bl5_2, bl6, bl6_2, bl6_3, bl6_4, bl7, bl8, bl9,bl9_2, bl10, bl11, bl12, bl13, bl14, bl15, bl16, bl17, bl18], [g,g1,g2,g3, g4, g5, fg, fg1, fg2], [hj], [sp], p, s)

#LEVEL2

bla = Boden.Block(pygame.Rect(100,2200,700 ,50), rinde)
blb = Boden.Block(pygame.Rect(1700,2000,1200,50), rinde)
blc = Boden.Block(pygame.Rect(2900,1700,750, 50), rinde)
bld = Boden.Block(pygame.Rect(3650,1700,50, 800), rinde)
ble = Boden.Block(pygame.Rect(3650, 2400,1450, 50), rinde)
blf = Boden.Block(pygame.Rect(4400,2000,100, 50), rinde)

p2 = Speicherpunkt.Portal(ble, [man1])

w2 = Welt( pygame.image.load("Gui/wald.jpg"), [bla, blb, blc, bld, ble, blf], [], [], [], p2, s) #########################asghdjkasdjashkdjaslkdja


#SPIELER
game = [w1, w2]
current_level = w1
backup_hintergrund_rect = copy.deepcopy(hintergrund_rect)
kugeln = []


def main():
        while True:
                for w in game:
                        while not w.finish:
                                for event in pygame.event.get():
                                        if event.type == QUIT:
                                                pygame.quit()
                                                sys.exit()
                                        elif event.type == KEYDOWN:
                                                if event.key == K_SPACE:
                                                        if s.is_Grounded:
                                                                w.spieler.jump()
                                                        else:
                                                                if s.double_jump_counter > 0:
                                                                        w.spieler.jump()
                                                                        w.spieler.double_jump_counter -= 1
                                                if event.key == K_UP:
                                                        k = Kugel((900 * s.direction, -75))
                                                if event.key == K_d:
                                                        if not w.spieler.is_Grounded:
                                                                w.spieler.dash_counter += 5
                                                                
                                keys = pygame.key.get_pressed()
                                if keys[K_RIGHT] or keys[K_LEFT]:
                                        w.spieler.move()
                                LEVELSURF.blit(hintergrund_blit(), (rect.left -10, rect.top -10))
                                w.update()
                                
                                for i in kugeln:
                                        i.update()
                                        
                                space.step(1/35)
                                clock.tick(25)
                                #print(len(space.bodies))
                                #print(current_speicherpunkt)
                                #print(current_level.spieler.body.velocity.x)
                                #print(space.collision_bias)
                                #print(fg2.rect.top)
                                #print(current_level.spieler.direction)
                                #print(backup_hintergrund_rect)
                                #print(current_level.init)
                                DISPLAYSURF.blit(camera_blit(), (0,0))
                                pygame.display.flip()
                                #pygame.quit()
                                #sys.exit()
if Multiplayer:
        pass
else:
        if __name__ == "__main__":
                cProfile.run("main()")
