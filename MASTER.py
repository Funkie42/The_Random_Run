import sys, pygame, pymunk, time, random
import Boden, Hindernis, Power_Ups, SpriteSheet, Speicherpunkt, cProfile, copy
from pygame.locals import*
from copy import deepcopy
from Gameclient import *

playing_Spieler = 0 # Zu setzen auf 1 bzw. 2
multiplayer = False
multiplayer_ghostmode = True
survival_time = 0
score = 0
test_startlvl = 0 # Für Testen

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

                self.mass = 10
                self.moveSpeed = 1
                self.jumpPower = 650

                self.body = pymunk.Body(self.mass, pymunk.inf)
                self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
                space.add(self.body, self.shape)
                self.shape.collision_type = 1 # To change for ghostmode to 0

                self.dash_counter = 0
                self.double_jump_counter = 1

                self.is_Grounded = False
                self.onStein = False
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
                if current_level.spieler.body.velocity.y > 0:
                        self.body.velocity.y = -self.jumpPower
                else:
                        self.body.velocity.y = -self.jumpPower

        def move(self):
            self.body.position.x += self.direction * self.moveSpeed
            hintergrund_rect.left += 4 * self.direction

        def dash(self):
                if self.dash_counter > 0:
                        self.body.position.x += 60 * self.direction
                        ###################################self.dash_counter -= 1

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
              


#WELT/LEVELKLASSE
class Welt():
        def __init__(self, BACKGROUNDSURF, boeden, hindernisse, power_ups, steine, speicherpunkte, portal, spieler1, spieler2, textboxes = []):
                self.BACKGROUNDSURF = BACKGROUNDSURF
                self.BACKGROUNDSURF = pygame.transform.scale(self.BACKGROUNDSURF, (int(LEVELSURF.get_width() * 2/3), DISPLAYSURF.get_height() + 25))
                self.boeden = boeden
                self.hindernisse = hindernisse
                self.steine = steine
                self.power_ups = power_ups
                self.speicherpunkte = speicherpunkte
                self.portal = portal
                self.textboxes = textboxes
                self.speicherpunkte.insert(0, Speicherpunkt.Speicherpunkt(self.boeden[0], [waypoint_sprite]))
                global current_speicherpunkt, hintergrund_rect
                current_speicherpunkt = self.speicherpunkte[0]
                #backup_hintergrund_rect = hintergrund_rect
                self.spieler1 = spieler1 
                self.spieler2 = spieler2
                self.spieler = None 
                self.anderer_spieler = None
                self.finish = False
                self.init = False

        def addToSpace(self):
                for i in self.textboxes:
                        space.add(i.shape)
                for i in self.boeden:
                        space.add(i.shape)
                for i in self.steine:
                        space.add(i.body, i.shape)
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
                for i in self.steine:
                        space.remove(i.body, i.shape)
                for i in self.hindernisse:
                        i.remove(space)
                for i in self.power_ups:
                        space.remove(i.body, i.shape)
                for i in self.speicherpunkte:
                        space.remove(i.shape)
                space.remove(self.portal.shape)
               
        def update(self):
                global current_speicherpunkt
                global rect
                global hintergrund_rect
                hintergrund_rect.left = int(4/11 * rect.left)
############################################################################
                

                for i in self.boeden:
                        if rect.colliderect(i.center_rect()) and i.center_rect().top < LEVELSURF.get_height() - 200:
                                i.update(rect)
                                LEVELSURF.blit(i.surf, (i.center_rect()))
                for i in self.textboxes:
                        i.update(rect)
                        LEVELSURF.blit(i.surf, (i.center_rect()))
                for i in self.steine:
                        if i.body.position.y > LEVELSURF.get_height() - 200 and i in self.steine: 
                                i.respawn()
                        if rect.colliderect(i.center_rect()):
                                if self.spieler.onStein: 
                                        i.update()
                                else:
                                        i.reihe = 0
                                LEVELSURF.blit(i.current_sprite(),i.center_rect())
                               
                for i in self.hindernisse:
                        if (i.body.position.y > LEVELSURF.get_height() - 200 or i.hitpoints < 0 )and i in self.hindernisse: #evtl zu updaten
                                ex = Explotion(i.body)
                                self.hindernisse.remove(i)
                                space.remove(i.body, i.shape)
                        if rect.colliderect(i.center_rect()):
                                LEVELSURF.blit(i.current_sprite(), i.center_rect())
                                random_int = random.randint(0,400)
                                if random_int == 100:
                                        i.engage(self.spieler.body.position.x)
                                if i.kugel_counter == i.feuerrate:
                                        k = Kugel((1200 * i.direction, -50), i.body.position.x, i.body.position.y - 20, False)
                                        k.shape.collision_type = 3
                                        k.shape.sprite_group = 2
                        i.update()
                                
                for i in self.power_ups:
                        if i.body.position.y > LEVELSURF.get_height() - 200 and i in self.power_ups: #evtl zu updaten
                                self.power_ups.remove(i)
                                space.remove(i.body, i.shape)
                        i.rect.center = i.body.position
                        i.body.position = i.rect.center
                        i.body.velocity.x = 0
                        if rect.colliderect(i.rect):
                                LEVELSURF.blit(i.sprite_list[i.sprite_iterator], i.rect)

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

                #############################
                                 #Spieler Position#
                #############################

                alle_spieler = [self.spieler]
                if self.anderer_spieler != None and multiplayer:
                        alle_spieler.append(self.anderer_spieler)
                if not self.init:
                        self.spieler.body.position.x = self.speicherpunkte[0].rect.left
                        self.spieler.body.position.y = self.speicherpunkte[0].rect.top - 250
                        self.addToSpace()
                        self.init = True
                        
                for spieler in alle_spieler:
                        if spieler == self.spieler: # Nur für den eigenen Spieler state-Update!
                                spieler.state_update()
                                if spieler.body.position.y > LEVELSURF.get_height() - 200:
                                        spieler.is_alive = False
                                if spieler.is_alive == False:
                                        spieler.body.velocity.x = 0
                                        spieler.body.velocity.y = -50
                                        spieler.body.position = (current_speicherpunkt.rect.left + 50, current_speicherpunkt.rect.top - 200)
                                        spieler.is_alive = True
                                spieler.dash()
                                spieler.body.reset_forces()
                        spieler.selfblit()
                #print(self.spieler.spalte)
                #pygame.draw.polygon(LEVELSURF, ((76, 45, 98)), self.spieler.shape.get_vertices())
                #pygame.draw.circle(LEVELSURF, ((45,34,23)), (int(self.spieler.body.position.x), int(self.spieler.body.position.y)), 10)
                
class Explotion(object):
        def __init__(self, body):
                self.x = body.position.x
                self.y = body.position.y
                self.reihe = 0
                self.spalte = 0
                self.sprite_iterator = 0
                explosions.append(self)
                global score
                score += 10

        def update(self):
                
                LEVELSURF.blit(explosion_sprite.get_image(self.spalte * explosion_sprite.sprite_sheet.get_width()/10 ,
                                                           self.reihe * explosion_sprite.sprite_sheet.get_height()/3, explosion_sprite.sprite_sheet.get_width()/10, explosion_sprite.sprite_sheet.get_height()/3), (self.x, self.y))
                if self.sprite_iterator >= 3:
                        self.sprite_iterator = 0
                        if self.spalte < 9:     self.spalte += 1
                        else:
                                self.spalte = 0
                                if self.reihe < 2:
                                        self.reihe += 1
                                else:   explosions.remove(self)
                else:   self.sprite_iterator += 1 


class Kugel(object):
        def __init__(self, vec, x_pos = 0, y_pos = 0, spielerdir = 0): ###################XPOS YPOS geändert für Multiplayer
                object.__init__(self)                   #Spielerdir = 0 heißt eigener Player direction
                self.vec = vec
                self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 10, 10))
                ###########################
                if x_pos == 0:
                        x_pos = current_level.spieler.body.position.x
                if y_pos == 0:
                        y_pos = current_level.spieler.body.position.y
                if spielerdir == 0:
                        spielerdir = current_level.spieler.direction
                self.body.position = (x_pos +40 * spielerdir,
                                      y_pos - 40)
                ##############################
                self.shape = pymunk.Circle(self.body, 10)
                space.add(self.body, self.shape)
                self.body.velocity.x = vec[0]
                self.body.velocity.y = vec[1]
                kugeln.append(self)
                self.shape.collision_type = 4
                self.shape.elasticy = 1
                self.lebenszeit = 50
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
                rect.center = current_level.spieler.body.position
                surf = LEVELSURF.subsurface(rect)
                return surf         
        except:
                if current_level.spieler.body.position.x < DISPLAYSURF.get_width()/2:
                        rect.left = 0
                if current_level.spieler.body.position.y < DISPLAYSURF.get_height()/2:
                        rect.top = 0
                if current_level.spieler.body.position.y >LEVELSURF.get_height() - DISPLAYSURF.get_height()/2:
                        rect.top = LEVELSURF.get_height() - DISPLAYSURF.get_height()
                if current_level.spieler.body.position.x >LEVELSURF.get_width() - DISPLAYSURF.get_width()/2:
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
                current_level.spieler.is_Grounded = True
                current_level.spieler.double_jump_counter = 1
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
        current_level.spieler.is_Grounded = False
        return True

def kugel_hits_gegner(space, arbiter):
        arbiter.shapes[0].body.velocity.y -= 400
        arbiter.shapes[0].body.velocity.x += 150 * current_level.spieler.direction
        arbiter.shapes[1].body.velocity.x = -150 * current_level.spieler.direction
        for i in current_level.hindernisse:
                if i.body == arbiter.shapes[0].body:
                        i.hitpoints -= 1
        return True

def kugel_hits_fliegender_gegner(space, arbiter):
        space.add(arbiter.shapes[0].body)
        arbiter.shapes[0].collision_type = 3
        arbiter.shapes[1].body.velocity.x = -150 * current_level.spieler.direction
        return True
        

def player_hits_kugel(space, arbiter):
        arbiter.shapes[1].body.velocity.y -= 1000
        arbiter.shapes[1].body.velocity.x += 1 * current_level.spieler.direction
        return True

def player_jumps_gegner(space, arbiter):
        if arbiter.contacts[0].normal.int_tuple[0] == 0:
                current_level.spieler.body.velocity.y = -650
                current_level.spieler.double_jump_counter = 1
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
                arbiter.shapes[1].body.position.x += 5 * current_level.spieler.direction
        return True

def kugel_hits_highjump(space, arbiter):
        arbiter.shapes[1].body.position.x += 20 * current_level.spieler.direction
        arbiter.shapes[0].group = 2
        return True

def player_hits_portal(space, arbiter):
        global current_level
        #current_level.removeFromSpace()
        current_level.removeFromSpace()
        current_level.finish = True
        if game.index(current_level) + 1 < len(game):
                current_level = game[game.index(current_level) + 1]
                #current_speicherpunkt = current_level.speicherpunkte[0]
        return True

def player_stands_stein(space, arbiter):
        current_level.spieler.is_Grounded = True
        current_level.spieler.body.velocity.x = 0
        current_level.spieler.onStein = True
        keys = pygame.key.get_pressed()
       
        if keys[K_w]:
                arbiter.shapes[1].body.velocity.y -= 10
        elif keys[K_d]:
                arbiter.shapes[1].body.velocity.x += 1
        elif keys[K_a]:
                arbiter.shapes[1].body.velocity.x -= 1
        elif keys[K_s]:
                arbiter.shapes[1].body.velocity.y += 1
        else:
                pymunk.Body.update_velocity(arbiter.shapes[1].body, ((0, -2000)), 0.9, 1/35)
                #rint(arbiter.shapes[1].body.velocity_func)
                pass
               
        return True

def player_leaves_stein(space, arbiter):
        current_level.spieler.onStein = False

def fly_right(body, gravity, damping, dt):
        body.velocity.x = 100
        damping = 0.5

def fly_left(body, gravity, damping, dt):
        body.velocity.x = -100
        damping = 0.5

def fly_down(body, gravity, damping, dt):
        body.velocity.y = 100
        damping = 0.5

def fly_up(body, gravity, damping, dt):
        body.velocity.y = -100
        damping = 0.5


# UNIVERSELLE OPTIONEN
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
LEVELSURF = pygame.Surface((6000, 8000))
current_speicherpunkt = False
space = pymunk.Space()
space.collision_bias = 0.0000001
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
space.add_collision_handler(1,8, post_solve=player_stands_stein, separate=player_leaves_stein)
space.gravity = (0, 1500)
clock = pygame.time.Clock()
fps = 30

#KAMERARECTS
rect = pygame.Rect(0,0,DISPLAYSURF.get_width(),DISPLAYSURF.get_height())
hintergrund_rect =pygame.Rect(0, 0, DISPLAYSURF.get_width() + 25, DISPLAYSURF.get_height() + 25)

#SPIELERSPRITES
man1 = pygame.image.load("Gui/man1.png")
man1 = pygame.transform.scale(man1,(80,100))

woman = SpriteSheet.SpriteSheet("Gui/woman.png")

#GELÄNDESPRITES
mars = pygame.image.load("Gui/ground.png").convert()
rinde = pygame.image.load("Gui/Rinde.jpg").convert()
rinde = pygame.transform.scale(rinde, (100, 100))
space_ground = pygame.image.load("Gui/ground5.png").convert()

#POWERUPSPRITES

highjump_sprite = pygame.image.load("Gui/pad.png")
highjump_sprite = pygame.transform.scale(highjump_sprite,(70,30))
waypoint_sprite = pygame.image.load("Gui/wp.png")
waypoint_sprite = pygame.transform.scale(waypoint_sprite,(130,130))
portal1_sprite =pygame.image.load("Gui/portal1.png")
portal1_sprite = pygame.transform.scale(portal1_sprite,(130,130))
portal2_sprite = pygame.image.load("Gui/portal2.png")
portal2_sprite = pygame.transform.scale(portal2_sprite,(130,130))
turbine_sprite = SpriteSheet.SpriteSheet("Gui/turbine_sprite.png")
explosion_sprite = SpriteSheet.SpriteSheet("Gui/explotion.png")

#SPIELER
s = Spieler()
s2 = Spieler()
#LEVEL1
bl0 = Boden.Block(pygame.Rect(50, 3000, 300, 50), mars)
bl1 = Boden.Block(pygame.Rect(550, 3000, 300, 50), mars)
bl2 = Boden.Block(pygame.Rect(950, 2850, 300, 50), mars)
bl3 = Boden.Block(pygame.Rect(1250, 2850, 50, 450), mars)
bl4 = Boden.Block(pygame.Rect(1550, 2400, 50, 650), mars)
bl5 = Boden.Block(pygame.Rect(1300, 3250, 800, 50), mars)
bl6 = Boden.Block(pygame.Rect(1600, 3000, 350, 50), mars)
bl7 = Boden.Block(pygame.Rect(2100, 2600, 50, 700), mars)
bl8 = Boden.Block(pygame.Rect(1750, 2550, 300, 50), mars)
bl9 = Boden.Block(pygame.Rect(2350, 2550, 150, 50), mars)
bl9_2 = Boden.Block(pygame.Rect(2500, 2550, 150, 50), mars)
bl10 = Boden.Block(pygame.Rect(2650, 2100, 50, 1100), mars)
bl11 = Boden.Block(pygame.Rect(2450, 2750, 200, 50), mars)
bl12 = Boden.Block(pygame.Rect(2550, 2950, 100, 50), mars)
bl13 = Boden.Block(pygame.Rect(2600, 3150, 50, 50), mars)
bl14 = Boden.Block(pygame.Rect(2500, 3350, 50, 50), mars)
bl15 = Boden.Block(pygame.Rect(2400, 3550, 50, 50), mars)
bl16 = Boden.Block(pygame.Rect(2500, 3750, 50, 50), mars)
bl17 = Boden.Block(pygame.Rect(2200, 3950, 250, 50), mars)
bl18 = Boden.Block(pygame.Rect(1500, 3950, 50, 50), mars)
bl19 = Boden.Block(pygame.Rect(600, 3950, 250, 50), mars)
bl19_2 = Boden.Block(pygame.Rect(400, 4200, 50, 50), mars)
bl20 = Boden.Block(pygame.Rect(2700, 2950, 100, 50), mars)
bl21 = Boden.Block(pygame.Rect(2700, 2950, 150, 50), mars)
bl22 = Boden.Block(pygame.Rect(2700, 2700, 100, 50), mars)


g0 = Hindernis.Gegner(bl2, 3, woman, 50, 100)
g1 = Hindernis.Gegner(bl5, 3, woman, 100, 100)
g2 = Hindernis.Gegner(bl8, 3, woman, 1, 100)
g3 = Hindernis.Gegner(bl11, 3, woman, 10, 100)
fg0 = Hindernis.FliegenderGegner(1600, 2100, 3850, 4, woman, 10, 100)
fg1 = Hindernis.FliegenderGegner(900, 1450, 3850, 6, woman, 10, 100)
fg2 = Hindernis.FliegenderGegner(4100, 4500, 1000, 6, woman, 10, 100, False)
fg3 = Hindernis.FliegenderGegner(4100, 4500, 1500, 6, woman, 10, 100, False)
fg4 = Hindernis.FliegenderGegner(4100, 4500, 200, 6, woman, 10, 100, False)


hj1 = Power_Ups.High_Jump(bl6, [highjump_sprite])
hj2 = Power_Ups.High_Jump(bl22, [highjump_sprite])

sp1 = Speicherpunkt.Speicherpunkt(bl9_2, [waypoint_sprite])
sp2 = Speicherpunkt.Speicherpunkt(bl19, [waypoint_sprite])
sp3 = Speicherpunkt.Speicherpunkt(bl21, [waypoint_sprite])

st = Boden.Stein(bl19_2, turbine_sprite)

p1 = Speicherpunkt.Portal(bl9, [portal2_sprite])

#Levels werden gespeichert in "set_everything"



#LEVEL2

bla = Boden.Block(pygame.Rect(100,2200,700 ,50), rinde)
blb = Boden.Block(pygame.Rect(1700,2000,1200,50), rinde)
blc = Boden.Block(pygame.Rect(2900,1700,750, 50), rinde)
bld = Boden.Block(pygame.Rect(3650,1700,50, 800), rinde)
ble = Boden.Block(pygame.Rect(3650, 2400,1450, 50), rinde)
blf = Boden.Block(pygame.Rect(4400,2000,100, 50), rinde)

p2 = Speicherpunkt.Portal(ble, [portal2_sprite])

#Levels werden gespeichert in "set_everything"


#LEVEL3
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
blockkoordinaten = [(50,2000,350,80),
                    (500,3000,100,100),
                    (0,1500,50,580),
                    (0,1400,900,100),
                    (200,1250,50,50), #[4]
                    (300,650,200,50),
                    (850,650,400,50),
                    (800,3000,500,100), #[7]
                    (900,2700,400,100),
                    (800,1640,100,1160),
                    (1300,2950,100,150),
                    (1400,2500,100,1000),
                    (900,1900,1100,100), #[12]
                    (1600,2000,200,1000),
                    (1700,3200,250,500), # [14]
                    (1200,3700,400,100),
                    (1800,2700,50,50),
                    (2000,2500,50,50),
                    (2200,2400,50,50),
                    (2400,2300,50,50),
                    (2800,2200,200,50),#[20]
                    (3000,2100,50,150),
                    (2400,2050,50,100)] 
leveldesign_block = rinde
w3_bl = []
for blockkoord in blockkoordinaten:
    w3_bl.append(Boden.Block(pygame.Rect(blockkoord[0],blockkoord[1],
                                              blockkoord[2],blockkoord[3]), leveldesign_block))
###########Gegner###################
gegner_in_lvl = []
#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
boden_gegner = [(1,2,woman,1,10),
                (6,8,woman,5,10),
                (7,5,woman,1,5)] # TODO
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
flug_gegner = [(400,600,2250,3,woman,5,10,True),
                (400,600,2500,3,woman,5,10,True),
                (400,600,2500,3,woman,5,10,True),
               (1000,1300,1800,4,woman,10,1000,True),
               (1000,1300,2200,4,woman,10,1000,True)] 

for gegner in boden_gegner:
    gegner_in_lvl.append(Hindernis.Gegner(w3_bl[gegner[0]],gegner[1],gegner[2],gegner[3],gegner[4]))
for gegner in flug_gegner:
    gegner_in_lvl.append(Hindernis.FliegenderGegner(gegner[0],gegner[1],gegner[2],gegner[3],gegner[4],gegner[5],gegner[6],gegner[7]))


w3_powerups = [Power_Ups.High_Jump(w3_bl[4], [highjump_sprite]),Power_Ups.High_Jump(w3_bl[14], [highjump_sprite])]
w3_speichpt = [Speicherpunkt.Speicherpunkt(w3_bl[12], [waypoint_sprite]),Speicherpunkt.Speicherpunkt(w3_bl[8], [waypoint_sprite]),Speicherpunkt.Speicherpunkt(w3_bl[20], [waypoint_sprite])]
w3_gegner = gegner_in_lvl
w3_bild = pygame.image.load("Gui/bg3.jpg").convert()

#Levels werden gespeichert in "set_everything"


#Welt die Bugs behebt
# Gleicht welt 3, wird nie aufgerufen

#Tutorial World
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
blockkoordinaten = [(100,4000,900,500),
                    (1200,4000,800,500),
                    (1600,3800,200,50),
                    (1800,3800,200,50),
                    (1000,4100,200,400),
                    (2200,3800,200,50),#[5]
                    (2600,3800,200,50),
                    (2600,4000,500,500),
                    (3100,4000,50,500),
                    (3150,3500,800,1000),
                    (3350,3050,100,50), #[10]
                    (2800,2800,400,50),
                    (2500,2000,50,50),
                    (2550,1800,50,50),
                    (2700,1600,1000,100),
                    (3700,1300,50,400),
                    (3750,1300,100,50),
                    (3850,1300,50,400), # [17]
                    (3750,1600,100,100),
                    (3900,1600,600,100),
                    (4500,1600,200,100),
                    (4600,1700,400,100),
                    (4900,1600,600,100),
                    (5500,1500,100,200),
                    (5900,0,100,4000),# [24]
                    (5500,3000,400,1500),
                    (4900,2800,50,50),
                    (4500,2600,200,100),
                    (0,0,100,4500), #  [28]
                    (100,0,6000,100),
                    (300,300,150,100)]
leveldesign_block = space_ground # z.B. mars oder so
Bloecke_in_lvl = []
for blockkoord in blockkoordinaten:
    Bloecke_in_lvl.append(Boden.Block(pygame.Rect(blockkoord[0],blockkoord[1],
                                              blockkoord[2],blockkoord[3]), leveldesign_block))
#Tut texte
t1 = Boden.Textbox(pygame.Rect(200,3700,800,60),pygame.font.Font('freesansbold.ttf', 35).render("Welcome to the tutorial of 'The Random Run'",True,(255,255,255)))
t2 = Boden.Textbox(pygame.Rect(600,4100,350,40),pygame.font.Font('freesansbold.ttf', 25).render("Press 'Space' to jump",True,(255,255,255)))
t3 = Boden.Textbox(pygame.Rect(1250,4050,450,40),pygame.font.Font('freesansbold.ttf', 25).render("Press 'Space' twice to doublejump",True,(255,255,255)))
t4 = Boden.Textbox(pygame.Rect(2050,4050,500,200),pygame.font.Font('freesansbold.ttf', 25).render("Don't jump down there though..",True,(255,255,255)))
t5 = Boden.Textbox(pygame.Rect(2900,4050,500,100),pygame.font.Font('freesansbold.ttf', 25).render("To jump extra high, use the highjump!",True,(255,255,255)))
t6 = Boden.Textbox(pygame.Rect(2700,3250,400,100),pygame.font.Font('freesansbold.ttf', 20).render("You then can still use the doublejump",True,(255,255,255)))
t7 = Boden.Textbox(pygame.Rect(3650,3200,200,50),pygame.font.Font('freesansbold.ttf', 25).render("Sometimes...",True,(255,255,255)))
t8 = Boden.Textbox(pygame.Rect(4000,3300,400,100),pygame.font.Font('freesansbold.ttf', 20).render("You have to jump into the unknown",True,(255,255,255)))
t9 = Boden.Textbox(pygame.Rect(3650,3950,250,100),pygame.font.Font('freesansbold.ttf', 20).render("..But not this time",True,(255,255,255)))
t10 = Boden.Textbox(pygame.Rect(2850,2550,300,50),pygame.font.Font('freesansbold.ttf', 20).render("Well Done! I'm surprised",True,(255,255,255)))
t11 = Boden.Textbox(pygame.Rect(2875,2250,250,50),pygame.font.Font('freesansbold.ttf', 20).render("You seem quite fit",True,(255,255,255)))
t12 = Boden.Textbox(pygame.Rect(2500,2250,300,50),pygame.font.Font('freesansbold.ttf', 20).render("Then let's turn it up a notch",True,(255,255,255)))
t13 = Boden.Textbox(pygame.Rect(2500,1350,1050,50),pygame.font.Font('freesansbold.ttf', 20).render("You see.. you can shoot surreal-space-balls with the 'Up' Button! They sometimes shoot through walls!",True,(255,255,255)))
t14 = Boden.Textbox(pygame.Rect(4100,1350,300,50),pygame.font.Font('freesansbold.ttf', 20).render("Ready for some fighting?",True,(255,255,255)))
t15 = Boden.Textbox(pygame.Rect(4900,1350,500,50),pygame.font.Font('freesansbold.ttf', 20).render("Each Enemy gives you a number of extra points",True,(255,255,255)))
t16 = Boden.Textbox(pygame.Rect(5400,1250,500,50),pygame.font.Font('freesansbold.ttf', 20).render("I think you should go down now",True,(255,255,255)))
t17 = Boden.Textbox(pygame.Rect(5500,1300,400,50),pygame.font.Font('freesansbold.ttf', 20).render("Your shuttle is waiting",True,(255,255,255)))
t18 = Boden.Textbox(pygame.Rect(4400,2300,400,50),pygame.font.Font('freesansbold.ttf', 20).render("You can control it with 'WASD'",True,(255,255,255)))
t19 = Boden.Textbox(pygame.Rect(4200,2100,400,50),pygame.font.Font('freesansbold.ttf', 20).render("It may be a bit difficult at first..'",True,(255,255,255)))
t20 = Boden.Textbox(pygame.Rect(3900,1900,500,50),pygame.font.Font('freesansbold.ttf', 20).render("The Portal home is in the upper left corner'",True,(255,255,255)))
t21 = Boden.Textbox(pygame.Rect(3500,1900,300,50),pygame.font.Font('freesansbold.ttf', 20).render("Good luck!'",True,(255,255,255)))
t22 = Boden.Textbox(pygame.Rect(200,450,350,50),pygame.font.Font('freesansbold.ttf', 20).render("You did it! Welcome home!'",True,(255,255,255)))
tut_texte = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22]
###########Gegner###################
gegner_in_lvl = []
#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
boden_gegner = [(18,0,woman,5,50000),
                (19,10,woman,5,20)] # TODO

#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse, Waagrecht oder nicht (Bool, standart true))
flug_gegner = [(4700,4900,1600,10,woman,10,50,True),
               (5200,5250,2900,0,woman,10,5000,True),
               (4800,4850,2700,0,woman,10,5000,True)] # TODO
for gegner in boden_gegner:
    gegner_in_lvl.append(Hindernis.Gegner(Bloecke_in_lvl[gegner[0]],gegner[1],gegner[2],gegner[3],gegner[4]))
for gegner in flug_gegner:
    gegner_in_lvl.append(Hindernis.FliegenderGegner(gegner[0],gegner[1],gegner[2],gegner[3],gegner[4],gegner[5],gegner[6],gegner[7]))
#############Power_Ups###############
tut_powerups= [Power_Ups.High_Jump(Bloecke_in_lvl[8], [highjump_sprite])]
#############Speicherpunkte############
tut_speichpt = [Speicherpunkt.Speicherpunkt(Bloecke_in_lvl[3], [waypoint_sprite]),Speicherpunkt.Speicherpunkt(Bloecke_in_lvl[9],
                                                                                                              [waypoint_sprite]),Speicherpunkt.Speicherpunkt(Bloecke_in_lvl[11], [waypoint_sprite]),Speicherpunkt.Speicherpunkt(Bloecke_in_lvl[14],
                                                                                                                                                                                                                                [waypoint_sprite]),Speicherpunkt.Speicherpunkt(Bloecke_in_lvl[25], [waypoint_sprite])]
tut_p = Speicherpunkt.Portal(Bloecke_in_lvl[30], [portal2_sprite])
tut_bl = Bloecke_in_lvl
tut_steine = [Boden.Stein(Bloecke_in_lvl[27], turbine_sprite)]
tut_gegner = gegner_in_lvl
tut_bild = pygame.image.load("Gui/bg_tut.jpg").convert()
#Levels werden gespeichert in "set_everything"


#SPIEL
game = []
current_level = None
backup_hintergrund_rect = copy.deepcopy(hintergrund_rect)
kugeln = []
explosions = []


def main():
        global score
        start_time = time.time()
        pause_time = 0
        bonustime = 300
        frame_counter = 0       
        for w in game:
                        while not w.finish and w == current_level:
                                new_kugel = False
#################################
                                #Event Getter
#################################
                                
                                for event in pygame.event.get():
                                        if event.type == QUIT or  (event.type == KEYUP and event.key == K_ESCAPE):
                                                pygame.quit()
                                                sys.exit()
                                        elif event.type == KEYDOWN:
                                                if event.key == K_q: # Für Beenden und zurück zum startmenü
                                                        w.removeFromSpace()
                                                        return (False,score,bonustime)
                                                if event.key == K_p and not multiplayer: #Pause TODO
                                                        pass
                                                if event.key == K_SPACE:
                                                        if w.spieler.is_Grounded:
                                                                w.spieler.jump()
                                                        else:
                                                                if w.spieler.double_jump_counter > 0:
                                                                        w.spieler.jump()
                                                                        w.spieler.double_jump_counter -= 1
                                                if event.key == K_UP:
                                                        new_kugel = True ####################################
                                                if event.key == K_d:
                                                        if not w.spieler.is_Grounded:
                                                                w.spieler.dash_counter += 5
                                                if event.key == K_F5:
                                                        w.spieler.is_alive = False
                                frame_counter += 1                               
                                keys = pygame.key.get_pressed()
                                if keys[K_RIGHT] or keys[K_LEFT]:
                                        w.spieler.move()
                                if new_kugel:
                                        k = Kugel((900 * current_level.spieler.direction, -75))        

#################################################################
                                #Mulitplayer Datenaustausch#
#################################################################
                                if multiplayer and frame_counter > 2:
                                        if frame_counter % 1 == 0:  
                                                if not multiplayer_ghostmode:
                                                        p2_data = send_data((playing_Spieler, # Spieler 1 oder 2
                                                                           (current_level.spieler.direction,current_level.spieler.state), #  Richtung in die er schaut und sprite_in_use
                                                                           (current_level.spieler.body.position.x,current_level.spieler.body.position.y), # Positition des Spielers
                                                                           ((current_level.spieler.direction,
                                                                             new_kugel)))) # "Neue Kugel" (De facto alles um eine zu erstellen)
                                                        if p2_data != None: # Sobald ein 2ter Spieler im Spiel ist
                                                                (p2_direction, p2_koords, p2_kugel) = p2_data
                                                                if p2_kugel[1]:
                                                                        Kugel((900 * p2_direction[0], -75), p2_koords[0],p2_koords[1],p2_direction[0])

                                                                        #Anderen Spieler Daten setzten für Anzeige
                                                                current_level.anderer_spieler.state = p2_direction[1]
                                                                current_level.anderer_spieler.body.position.x = p2_koords[0]
                                                                current_level.anderer_spieler.body.position.y = p2_koords[1]
                                                                current_level.anderer_spieler.direction = p2_direction[0]
                                                else: # Ghostmode
                                                        p2_data = send_data((playing_Spieler, # Spieler 1 oder 2
                                                                           (current_level.spieler.direction,current_level.spieler.state), #  Richtung in die er schaut und sprite_in_use
                                                                           (current_level.spieler.body.position.x,current_level.spieler.body.position.y),())) # Positition des Spielers
                                                        if p2_data != None: # Sobald ein 2ter Spieler im Spiel ist
                                                                (p2_direction, p2_koords,_) = p2_data
                                                                try:
                                                                        current_level.anderer_spieler.state = p2_direction[1]
                                                                        current_level.anderer_spieler.body.position.x = p2_koords[0]
                                                                        current_level.anderer_spieler.body.position.y = p2_koords[1]
                                                                        current_level.anderer_spieler.direction = p2_direction[0]
                                                                except: pass
                                else: current_level.spieler2 = None # Im Singleplayer braucht man keinen 2. Spieler
                                       # if frame_counter%10 == 0:
#
  #                                              frame_counter = 0
    #                                            stuff_data = send_data((-42,playing_Spieler,1,1))
                                
#################################################################
                                
                                if (frame_counter % 1 == 0): LEVELSURF.blit(hintergrund_blit(),(rect.left -10, rect.top -10))
                                w.update()
                                for i in kugeln: i.update()
                                for i in explosions: i.update()
                                space.step(1/35)
                                clock.tick(25)
                                DISPLAYSURF.blit(camera_blit(), (0,0))

                                ### Highscoreanzeige ###
                                if bonustime > 0: bonustime = 300 - int(time.time() - start_time - pause_time)
                                else: bonustime = 0
                                score_string = "Bonustime: " + str(bonustime) + "     Score: " + str(score)
                                thisPrint = pygame.font.Font('freesansbold.ttf', 20).render(score_string,True,(255,255,255))
                                thisRect = thisPrint.get_rect()
                                thisRect.center = ((150,40))
                                DISPLAYSURF.blit(thisPrint,thisRect)
                                if (frame_counter > 800 and frame_counter < 850):
                                        die_string = "Press F5 to instantly die painfully"
                                        diePrint = pygame.font.Font('freesansbold.ttf', 20).render(die_string,True,(255,255,255))
                                        dieRect = diePrint.get_rect()
                                        dieRect.center = ((470,40))
                                        DISPLAYSURF.blit(diePrint,dieRect)
                                if (frame_counter > 850 and frame_counter < 900):
                                        die_string = "Press 'Q' to give up and go home"
                                        diePrint = pygame.font.Font('freesansbold.ttf', 20).render(die_string,True,(255,255,255))
                                        dieRect = diePrint.get_rect()
                                        dieRect.center = ((470,40))
                                        DISPLAYSURF.blit(diePrint,dieRect)
                                if frame_counter > 5000000: frame_counter = 0


                                pygame.display.flip()
                                #print(game.index(current_level))
                                
                                if w.finish and __name__ != "__main__":
                                        #print(game.index(current_level))
                                        #print(game.index(current_level) + 1 < len(game))
                                        old_score = score
                                        score += bonustime
                                        if game.index(current_level) + 1 < len(game): return True, old_score,bonustime
                                        else: return False, old_score,bonustime
                                
                                
def set_everything(start_level):
        global current_level,game,score
        tut_w = Welt(tut_bild, tut_bl, tut_gegner,tut_powerups, tut_steine, tut_speichpt,tut_p,s,s2,textboxes = tut_texte)
        w1 = Welt(pygame.image.load("Gui/bg1.jpg").convert(),
          [bl0, bl1, bl2, bl3, bl4, bl5, bl6, bl7, bl8, bl9, bl9_2, bl10, bl11, bl12, bl13, bl14, bl15, bl16, bl17, bl18, bl19,bl20, bl21, bl22],
          [g0, g1, g2, g3, fg0, fg1, fg2, fg3, fg4], [hj1, hj2], [st], [sp1, sp2, sp3], p1, s, s2)
        w2 = Welt( pygame.image.load("Gui/bg2.jpg").convert(), [bla, blb, blc, bld, ble, blf], [], [], [], [], p2, s, s2) 
        w3 = Welt(w3_bild, w3_bl, w3_gegner,w3_powerups, [], w3_speichpt,p2,s,s2)
        wend = Welt(w3_bild, w3_bl, w3_gegner,w3_powerups, [], w3_speichpt,p2,s,s2)
        game = [tut_w,w1,w2,w3,wend]
        current_level = game[start_level]
        score = 0 
        for w in game:
                w.finish = False
                
def on_execute(multi_True = False,start_level = 1): # Multiplayer starten oder Singleplayer (bei False singleplayer)
        global multiplayer,survival_time,playing_Spieler
        multiplayer = multi_True     
        survival_time = time.time()#Für Highscore
        set_everything(start_level)
        if multiplayer:
                if __name__ == "__main__":
                        try:
                                print("Client connecting on \""+client_ip+"\", port "+str(port)+" . . .")
                                create_Client(42042,'localhost')#192.168.178.37')
                                print("Client connected!")
                                playing_Spieler = get_player_number()
                                #print(playing_Spieler)
                                for w in game:
                                        if playing_Spieler == 1:
                                                w.spieler = current_level.spieler1# Der Spieler den dieser PC steuert
                                                w.anderer_spieler = current_level.spieler2
                                        else:
                                                w.spieler = current_level.spieler2
                                                w.anderer_spieler = current_level.spieler1
                                main()
                                client.disconnect()
                                print("Client disconnected!")
                        except MastermindError:
                                print("No server found! Please start Server and try again!")
                                pygame.quit()
                                sys.exit()
                else: # Start aus dem Menü heraus
                        playing_Spieler = get_player_number()
                        for w in game:
                                if playing_Spieler == 1:
                                                w.spieler = current_level.spieler1# Der Spieler den dieser PC steuert
                                                w.anderer_spieler = current_level.spieler2
                                                if multiplayer_ghostmode:
                                                        w.anderer_spieler.shape.collision_type = 0
                                                awaiting_snd_player = True
                                                while awaiting_snd_player:
                                                        p2_data = send_data((playing_Spieler, # Spieler 1 oder 2
                                                                           (), #  Richtung in die er schaut und sprite_in_use
                                                                           (), # Positition des Spielers
                                                                           ()))
                                                        pygame.display.flip()
                                                        if p2_data != None:
                                                                awaiting_snd_player = False    
                                else:
                                                w.spieler = current_level.spieler2
                                                w.anderer_spieler = current_level.spieler1
                                                if multiplayer_ghostmode: w.anderer_spieler.shape.collision_type = 0
                        main()
        else:
                for w in game: w.spieler = w.spieler1
                if __name__ == "__main__": main()
                # Singelplayerstart aus dem Menü heraus
                else:  return main()




if __name__ == "__main__":      on_execute(multiplayer,test_startlvl)



