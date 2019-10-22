import sys, pygame, pymunk, time, random, copy
import Boden, Hindernis, Power_Ups, SpriteSheet, Speicherpunkt, Level,cProfile, Piano
from pygame.locals import*
from copy import deepcopy
from Gameclient import *

playing_Spieler = 0 # Zu setzen auf 1 bzw. 2
multiplayer = False
multiplayer_ghostmode = True
survival_time = 0
score = 0
opponentscore = 0
test_startlvl = 1# Für Testen
hitpoints = 5
death_counter = 0
dead_show = 0
kill_counter = 0
scorechange_size = 35
frame_counter = 0
final_boss = None
startlevel = 1

TOMFAKTOR = False # Weil tom keinen Text anzeigen kann

jump_sound = "Sounds/jump.wav"
explosion_sound = "Sounds/dead.wav"
die_sound = "Sounds/aah.wav"
kugel_sound  = "Sounds/phaser.wav"
portal_sound = "Sounds/swoop.wav"
waypoint_sound = "Sounds/wp.wav"
rocket_sound = "Sounds/rocket_sound.wav"
jumppad_sound = "Sounds/jump_pad.ogg"
dash_sound = "Sounds/swuuuuush.ogg"


class Spieler(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.sprite_iterator = 0

                self.spalte = 0
                
                self.state = 0 # 0 = stand, 1 = move, 2 = jump, 3 = fall, 4 = duck, 5 = roll, 6 = schlittern

                self.jump_force = (0,0)

                self.sprite = character_sprite
                
                self.double_jump_iterator = 0

                self.direction = 1 #1 = rechts, -1 = links
                self.sprites1 = []
                self.sprites2 = []
                self.make_sprites()
                self.hitpoints = hitpoints
                self.mass = 10
                self.moveSpeed = 1
                self.jumpPower = 650

                self.body = pymunk.Body(self.mass, pymunk.inf)
                self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
                space.add(self.body, self.shape)
                self.shape.collision_type = 1 

                self.dash_counter = 0
                self.double_jump_counter = 1

                self.is_Grounded = False
                self.onStein = False
                self.is_alive = True

        def make_sprites(self):
                for i in range(0,17):
                    x = self.sprite.get_image(25 + i * self.sprite.sprite_sheet.get_width()/17 , 5, self.sprite.sprite_sheet.get_width()/17 -55, self.sprite.sprite_sheet.get_height() - 5).convert()
                    self.sprites1.append(x)
                    self.sprites2.append(pygame.transform.flip(x,True,False))        

        def rect(self):
                x = pygame.Rect(0,0, self.current_sprite().get_width(), self.current_sprite().get_height())
                x.center = self.body.position
                return x

        def current_sprite(self):
                if self.direction == 1:
                        return self.sprites1[self.spalte]
                else:
                        return self.sprites2[self.spalte]


        def state_update(self):
                keys = pygame.key.get_pressed()
                if self.direction == 1 and keys[K_LEFT] and not keys[K_RIGHT] and self.moveSpeed != 0:
                        self.direction = -1
                elif self.direction == -1 and keys[K_RIGHT] and not keys[K_LEFT] and self.moveSpeed != 0:
                        self.direction = 1
                if self.is_Grounded and not (keys[K_RIGHT] or keys[K_LEFT]):
                        self.state = 0
                elif self.is_Grounded and (keys[K_RIGHT] or keys[K_LEFT]):
                        self.state = 1     
                elif not self.is_Grounded:
                        self.state = 2

                        
        def jump(self):
                if startlevel != 7: pygame.mixer.Sound(jump_sound).play()
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
                        self.dash_counter -= 1

        def selfblit(self):
                #if self.sprite_iterator >= len(self.sprite_list[self.state]):
                if self.state == 0:
                        self.spalte = 0
                elif self.state == 1:
                        if self.sprite_iterator >= 0:
                                if self.spalte <= 15:
                                        self.spalte += 1
                                else:
                                        self.spalte = 5 
                                self.sprite_iterator = 0
                        else:
                                self.sprite_iterator += 1
                elif self.state == 2:
                        self.spalte = 2  
                LEVELSURF.blit(self.current_sprite(), self.rect())
              


#WELT/LEVELKLASSE
class Welt():
        def __init__(self, BACKGROUNDSURF, boeden, hindernisse, power_ups, steine, speicherpunkte, portal, spieler1, spieler2, textboxes = []):
                global current_speicherpunkt, hintergrund_rect
                self.BACKGROUNDSURF = BACKGROUNDSURF
                self.BACKGROUNDSURF = pygame.transform.scale(self.BACKGROUNDSURF, (int(LEVELSURF.get_width() * 2/3), DISPLAYSURF.get_height() + 25))
                self.sterbehoehe = 200
                self.boeden = boeden
                self.hindernisse = hindernisse
                self.steine = steine
                self.power_ups = power_ups
                self.speicherpunkte = speicherpunkte
                self.portal = portal
                self.textboxes = textboxes
                if multiplayer_ghostmode:
                        self.speicherpunkte.insert(0, Speicherpunkt.Speicherpunkt(self.boeden[0], [waypoint_sprite]))
                        current_speicherpunkt = self.speicherpunkte[0]
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
                for i in self.textboxes:
                        space.remove(i.shape)
                for i in self.boeden:
                        space.remove(i.shape)
                for i in self.steine:
                        space.remove(i.body, i.shape)
                for i in self.hindernisse:
                        if not i.dead:
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
                
                for i in self.boeden:
                        if rect.colliderect(i.center_rect()) and i.center_rect().top < LEVELSURF.get_height() - self.sterbehoehe:
                                i.update(rect)
                                LEVELSURF.blit(i.surf, (i.center_rect()))
                for i in self.textboxes:
                        i.update(rect)
                        LEVELSURF.blit(i.surf, (i.center_rect()))
                for i in self.steine:
                        if i.body.position.y > LEVELSURF.get_height() - self.sterbehoehe and i in self.steine: 
                                i.respawn()
                        if rect.colliderect(i.center_rect()):
                                if self.spieler.onStein: 
                                        i.update()
                                else:
                                        i.reihe = 0
                                LEVELSURF.blit(i.current_sprite(),i.center_rect())
                               
                for i in self.hindernisse:
                        if not i.dead:
                                if (i.body.position.y > LEVELSURF.get_height() - self.sterbehoehe or i.hitpoints < 0 )and i in self.hindernisse: #evtl zu updaten
                                        ex = Explotion(i.body)
                                        i.dead = True
                                        space.remove(i.body, i.shape)
                                        global kill_counter
                                        kill_counter += 15
  
                                        
                                if rect.colliderect(i.center_rect()):
                                        LEVELSURF.blit(i.current_sprite(), i.center_rect())
                                        random_int = random.randint(0,800)
                                        if random_int == 100:
                                                i.engage(self.spieler.body.position.x)
                                        if i.kugel_counter == i.feuerrate:
                                                k = Kugel((1200 * i.direction, -50),((245,12,188)), i.body.position.x + (15 * i.direction), i.body.position.y - 10, False)
                                                k.shape.collision_type = 3
                                                k.shape.sprite_group = 2
                                                if i.endgegner:
                                                        k1 = Kugel((-1000, 500),((245,12,188)), i.body.position.x - 20, i.body.position.y +30, False)
                                                        k2 = Kugel((0, 500),((245,12,188)), i.body.position.x, i.body.position.y +30, False)
                                                        k3 = Kugel((1000, 500),((245,12,188)), i.body.position.x + 20, i.body.position.y +30, False)
                                                        k1.shape.collision_type = 3
                                                        k1.shape.sprite_group = 2
                                                        k2.shape.collision_type = 3
                                                        k2.shape.sprite_group = 2
                                                        k3.shape.collision_type = 3
                                                        k3.shape.sprite_group = 2
                                                        ######################################%%%%%%%%%%%%%%%%%%%%%%%    
                                i.update()
                                
                for i in self.power_ups:
                        if i.body.position.y > LEVELSURF.get_height() - self.sterbehoehe and i in self.power_ups: #evtl zu updaten
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
                                 pygame.mixer.Sound(waypoint_sound).play()
                                 try: space.remove(i.shape)
                                 except: pass

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
                        if multiplayer:
                                self.anderer_spieler.sprite = character2_sprite
                                self.anderer_spieler.sprites1 =[]
                                self.anderer_spieler.sprites2 =[]
                                self.anderer_spieler.make_sprites()
                        if playing_Spieler == 2:
                                self.spieler.body.position.x += 100
                        
                for spieler in alle_spieler:
                        if spieler == self.spieler: # Nur für den eigenen Spieler state-Update!
                                spieler.state_update()
                                if spieler.body.position.y > LEVELSURF.get_height() - self.sterbehoehe:
                                        spieler.is_alive = False
                                if spieler.is_alive == False: # So lassen, sonst geht F5 nichtmehr
                                        pygame.mixer.Sound(die_sound).play()
                                        global score,death_counter,dead_show
                                        if death_counter < 10: death_counter += 1
                                        score -= death_counter*10
                                        dead_show = 20
                                        spieler.hitpoints = hitpoints
                                        for j in self.steine:
                                                j.respawn()
                                        for j in self.hindernisse:
                                                if j.dead:
                                                        j.dead = False
                                                        if j.baseHitpoints == 4:
                                                                j.shape.collision_type = 6
                                                        j.init(space)
                                                        j.body.position = j.start
                                                        j.hitpoints = j.baseHitpoints
                                                        j.body.velocity.y = 0
                                                        j.body.velocity.x = 0
                                                        j.moveSpeed = j.baseMoveSpeed
                                                else:
                                                        j.body.position = j.start
                                                        j.hitpoints = j.baseHitpoints
                                        spieler.body.velocity.x = 0
                                        spieler.body.velocity.y = -50
                                        spieler.body.position = (current_speicherpunkt.rect.left + 50, current_speicherpunkt.rect.top - 200)
                                        spieler.is_alive = True
                                spieler.dash()
                                spieler.body.reset_forces()
                        spieler.selfblit()

class Explotion(object):
        def __init__(self, body):
                pygame.mixer.Sound(explosion_sound).play()
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
                if self.sprite_iterator >= 0:
                        self.sprite_iterator = 0
                        if self.spalte < 9:     self.spalte += 1
                        else:
                                self.spalte = 0
                                if self.reihe < 2:
                                        self.reihe += 1
                                else:   explosions.remove(self)
                else:   self.sprite_iterator += 1 


class Kugel(object):
        def __init__(self, vec,farbe, x_pos = 0, y_pos = 0, spielerdir = 0):
                object.__init__(self)                   #Spielerdir = 0 heißt eigener Player direction
                pygame.mixer.Sound(kugel_sound).play()
                self.vec = vec
                self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 7, 7))
                self.farbe = farbe
                if x_pos == 0:
                        x_pos = current_level.spieler.body.position.x
                if y_pos == 0:
                        y_pos = current_level.spieler.body.position.y
                if spielerdir == 0:
                        spielerdir = current_level.spieler.direction
                self.body.position = (x_pos +60 * spielerdir,
                                      y_pos - 35)
                self.shape = pymunk.Circle(self.body,  7)
                space.add(self.body, self.shape)
                self.body.velocity.x = vec[0]
                self.body.velocity.y = vec[1]
                kugeln.append(self)
                self.shape.collision_type = 4
                self.shape.elasticy = 1
                self.lebenszeit = 25
                self.shape.group = 1
        
        def update(self):
                pygame.draw.circle(LEVELSURF, self.farbe, (int(self.body.position.x), int(self.body.position.y)), 7)
                if self.body.position.y > 7800 and self in kugeln or self.lebenszeit == 0:
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
                if i.endgegner: ####################################MAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRIIIIIIIIIIIIIIIUUUUUUUUUUUUUUUUSSSSSSSSSSSSSSSSSs
                        j = pymunk.Body()
                        j.position = i.body.position
                        j.position.y -= 40
                        ex = Explotion(j)
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
                for i in current_level.hindernisse:
                        if i.body == arbiter.shapes[1].body:
                                if current_level.spieler.body.position.y < arbiter.shapes[1].body.position.y:
                                        current_level.spieler.body.velocity.y = -650
                                        current_level.spieler.double_jump_counter = 1
                                        i.hitpoints -= 2
                                else:
                                        current_level.spieler.hitpoints -= 1
                                        i.body.velocity.y = -400
        else:
                current_level.spieler.hitpoints -= 1
                current_level.spieler.body.velocity.x = -300 * current_level.spieler.direction
                current_level.spieler.body.velocity.y = -450
        return True

def player_jumps_fliegender_gegner(space, arbiter):
        if arbiter.contacts[0].normal.int_tuple[0] == 0:
                current_level.spieler.body.velocity.y = -650
                current_level.spieler.double_jump_counter = 1
                space.add(arbiter.shapes[1].body)
                arbiter.shapes[1].collision_type = 3
        else:
                current_level.spieler.hitpoints -= 1
                current_level.spieler.body.velocity.x = -300 * current_level.spieler.direction
                current_level.spieler.body.velocity.y = -450
        return True


def player_jumps_highjump(space, arbiter):
        if arbiter.contacts[0].normal.int_tuple[0] == 0:
                pygame.mixer.Sound(jumppad_sound).play()
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
        random_int = random.randint(0,25)
        if random_int == 1 and not TOMFAKTOR:
                score_string = "You randomly passed away of a heart attack" 
                thisPrint = pygame.font.Font('freesansbold.ttf', 35).render(score_string,True,(255,255,255))
                thisRect = thisPrint.get_rect()
                thisRect.center = ((400,300))
                DISPLAYSURF.blit(thisPrint,thisRect)
                pygame.display.flip()
                time.sleep(2)
                current_level.spieler.is_alive = False
                return True
        
        current_level.removeFromSpace()
        pygame.mixer.Sound(portal_sound).play()
        current_level.finish = True
        if game.index(current_level) + 1 < len(game):
                current_level = game[game.index(current_level) + 1]
        return True

def player_hits_dash(space,arbiter):
        if current_level.spieler.dash_counter == 0: pygame.mixer.Sound(dash_sound).play()
        current_level.spieler.dash_counter += 5
        current_level.spieler.double_jump_counter = 1
        return True

def player_stands_stein(space, arbiter):
        pygame.mixer.Sound(rocket_sound).play()
        current_level.spieler.is_Grounded = True
        current_level.spieler.body.velocity.x = 0
        current_level.spieler.onStein = True
        keys = pygame.key.get_pressed()
       
        if keys[K_w]:
                arbiter.shapes[1].body.velocity.y -= 10
        elif keys[K_d]:
                arbiter.shapes[1].body.velocity.x += 2
        elif keys[K_a]:
                arbiter.shapes[1].body.velocity.x -= 2
        elif keys[K_s]:
                arbiter.shapes[1].body.velocity.y += 2
        else:
                pymunk.Body.update_velocity(arbiter.shapes[1].body, ((0, -2000)), 0.9, 1/35)
                pass
               
        return True

def player_leaves_stein(space, arbiter):
        current_level.spieler.onStein = False
        cänt_touch_dis(space,arbiter)

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
#15 = Dash_powerup
#16 = Boss

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
space.add_collision_handler(1,15, post_solve=player_hits_dash)
#space.add_collision_handler(1,16, begin=player_jumps_boss)
space.gravity = (0, 1500)
clock = pygame.time.Clock()
fps = 30

#KAMERARECTS
rect = pygame.Rect(0,0,DISPLAYSURF.get_width(),DISPLAYSURF.get_height())
hintergrund_rect =pygame.Rect(0, 0, DISPLAYSURF.get_width() + 25, DISPLAYSURF.get_height() + 25)

#SPIELERSPRITES
character_sprite = Level.character_sprite
character2_sprite = Level.character2_sprite
alien_sprite = Level.alien_sprite
alien_sprite.sprite_sheet = pygame.transform.flip(alien_sprite.sprite_sheet, True , False)
pacman_sprite = Level.pacman_sprite

#POWERUPSPRITES

highjump_sprite = pygame.image.load("Gui/pad.png")
highjump_sprite = pygame.transform.scale(highjump_sprite,(70,30))
waypoint_sprite = pygame.image.load("Gui/wp.png")
waypoint_sprite = pygame.transform.scale(waypoint_sprite,(130,130))
portal1_sprite =pygame.image.load("Gui/portal1.png")
portal1_sprite = pygame.transform.scale(portal1_sprite,(130,130))
portal2_sprite = pygame.image.load("Gui/portal2.png")
portal2_sprite = pygame.transform.scale(portal2_sprite,(130,130))
dashPW_sprite = pygame.image.load("Gui/powerups/shoe.png")
dashPW_sprite = pygame.transform.scale(dashPW_sprite,(40,40))
turbine_sprite = SpriteSheet.SpriteSheet("Gui/turbine_sprite.png")
explosion_sprite = SpriteSheet.SpriteSheet("Gui/explotion.png")

lebensanzeige = pygame.image.load("Gui/powerups/heart.png")#.convert()
lebensanzeige = pygame.transform.scale(lebensanzeige,(25,25))
lebensanzeige2 = pygame.image.load("Gui/powerups/flash.png")#.convert()
lebensanzeige2 = pygame.transform.scale(lebensanzeige2,(25,25))


#SPIEL
game = []
current_level = None
backup_hintergrund_rect = copy.deepcopy(hintergrund_rect)
kugeln = []
explosions = []


def main():
        global score,dead_show,death_counter, kill_counter, current_level, opponentscore,frame_counter, final_boss
        start_time = time.time()
        pause_time = 0
        bonustime = 300
        kill_counter = 0
        death_counter = 0
        for w in game:
                        while not w.finish and w == current_level:
                                old_death_counter = death_counter
                                new_kugel = False
#################################
                                #Event Getter
################################# 
                                for event in pygame.event.get():
                                        if event.type == QUIT or  (event.type == KEYUP and event.key == K_ESCAPE):
                                                if multiplayer: send_data("gg")
                                                pygame.quit()
                                                sys.exit()
                                                
                                        elif event.type == KEYDOWN:
                                                if event.key == K_F12: # Für Beenden und zurück zum startmenü
                                                        if multiplayer: send_data("gg")
                                                        w.removeFromSpace()
                                                        w.finish = True
                                                        if not multiplayer_ghostmode: return False,1,1,"duell","defaultlose"
                                                        return (False,score,-1)
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
                                                if event.key == K_k:
                                                        pass
                                                        w.spieler.dash_counter += 5
                                                if event.key == K_F5:
                                                        w.spieler.is_alive = False
                                frame_counter += 1
                                keys = pygame.key.get_pressed()
                                if keys[K_RIGHT] or keys[K_LEFT]:
                                        w.spieler.move()
                                if new_kugel:
                                        k = Kugel((1200 * current_level.spieler.direction, -100),(218,165,32))        
                                if startlevel == 7:
                                    Piano.majestro(current_level.spieler.body.position.x,current_level.spieler.body.position.y)
                                
#################################################################
                                #Mulitplayer Datenaustausch#
#################################################################
                                if multiplayer and frame_counter > 2:
                                        if frame_counter % 1 == 0:  
                                                if not multiplayer_ghostmode: # Metzelmode
                                                        p2_data = send_data((playing_Spieler, # Spieler 1 oder 2
                                                                           (current_level.spieler.direction,current_level.spieler.state), #  Richtung in die er schaut und sprite_in_use
                                                                           (current_level.spieler.body.position.x,current_level.spieler.body.position.y), # Positition des Spielers
                                                                           ((current_level.spieler.direction,new_kugel)),# "Neue Kugel" (De facto alles um eine zu erstellen)
                                                                             (current_level.spieler.hitpoints,death_counter))) 
                                                        if p2_data == "gg":
                                                                w.removeFromSpace()
                                                                w.finish = True
                                                                if not multiplayer_ghostmode: return False,1,1,"duell","defaultwin"
                                                                return (False,score,-1,"")

                                                        elif p2_data != None: # Sobald ein 2ter Spieler im Spiel ist
                                                                (p2_direction, p2_koords, p2_kugel,p2_hits) = p2_data
                                                                try:#Anderen Spieler Daten setzten für Anzeige
                                                                        
                                                                        if p2_kugel[1]:
                                                                                k = Kugel((900 * p2_direction[0], -75),(155,0,0), p2_koords[0],p2_koords[1],p2_direction[0])
                                                                                k.shape.collision_type = 3
                                                                        current_level.anderer_spieler.state = p2_direction[1]
                                                                        current_level.anderer_spieler.body.position.x = p2_koords[0]
                                                                        current_level.anderer_spieler.body.position.y = p2_koords[1]
                                                                        current_level.anderer_spieler.direction = p2_direction[0]
                                                                        current_level.anderer_spieler.hitpoints = p2_hits[0]
                                                                        opponentscore = p2_hits[1]
                                                                except: pass
                                                              
                                                else: # Ghostmode
                                                        p2_data = send_data((playing_Spieler, # Spieler 1 oder 2
                                                                           (current_level.spieler.direction,current_level.spieler.state), #  Richtung in die er schaut und sprite_in_use
                                                                           (current_level.spieler.body.position.x,current_level.spieler.body.position.y),
                                                                             (score),())) # Positition des Spielers
                                                        if p2_data == "gg":
                                                                w.removeFromSpace()
                                                                w.finish = True
                                                                return (False,score,-1,"")
                                                        elif p2_data[0] == "level finished":
                                                                #print(game.index(current_level))
                                                                w.removeFromSpace()
                                                                w.finish = True
                                                                if game.index(current_level) + 1 < len(game):
                                                                        current_level = game[game.index(current_level) + 1]
                                                                return(True,score,0,"lost")
                                                        elif p2_data != None: # Sobald ein 2ter Spieler im Spiel ist
                                                                (p2_direction, p2_koords,p2_score,_) = p2_data
                                                                try:
                                                                        current_level.anderer_spieler.state = p2_direction[1]
                                                                        current_level.anderer_spieler.body.position.x = p2_koords[0]
                                                                        current_level.anderer_spieler.body.position.y = p2_koords[1]
                                                                        current_level.anderer_spieler.direction = p2_direction[0]
                                                                        opponentscore = p2_score
                                                                except: pass
                                else: current_level.spieler2 = None # Im Singleplayer braucht man keinen 2. Spieler

#################################################################
                                if w.spieler.hitpoints <= 0: w.spieler.is_alive = False
                                if (frame_counter % 1 == 0): LEVELSURF.blit(hintergrund_blit(),(rect.left -10, rect.top -10))
                                w.update()
                                for i in kugeln: i.update()
                                for i in explosions: i.update()
                                pygame.draw.rect(LEVELSURF,(155,0,0),pygame.Rect(0,LEVELSURF.get_height() - w.sterbehoehe,LEVELSURF.get_width(),3))
                                if final_boss != None: # Endgegner Tot - Level done!
                                        if final_boss.dead:
                                                final_boss = None
                                                w.portal = Speicherpunkt.Portal(w.boeden[28], [portal1_sprite])
                                                space.add(w.portal.shape)
                                                #if game.index(current_level) + 1 < len(game):
                                                #current_level = game[game.index(current_level) + 1]
                                if not w.finish: space.step(1/35)
                                clock.tick(25)
                                DISPLAYSURF.blit(camera_blit(), (0,0))

                                ### Highscoreanzeige ###
                                if bonustime > 0: bonustime = 300 - int(time.time() - start_time - pause_time)
                                else: bonustime = 0
                                if not TOMFAKTOR and multiplayer_ghostmode:
                                        bonustime_string = "Bonustime: " + str(bonustime)
                                        show_text(bonustime_string,20,(255,255,255),(20,20))
                                        score_string =  "Score: " + str(score)
                                        if multiplayer: score_string =  "P1 Score: " + str(score)
                                        show_text(score_string,20,(255,255,255),(200,20))
                                        if multiplayer: show_text("P2 Score: "+ str(opponentscore),20,(55,55,55),(200,50))
                                        
                                        if (frame_counter > 1800 and frame_counter < 1850):
                                                die_string = "Press F5 to restart form the last Checkpoint"
                                                show_text(die_string,20,(255,255,255),(333,20))
                                        if (frame_counter > 1850 and frame_counter < 1900):
                                                die_string = "Press 'F12' to exit"
                                                show_text(die_string,20,(255,255,255),(333,20))
                                        if multiplayer:
                                                if (frame_counter > 100 and frame_counter < 200):
                                                        show_text("Welcome to the Ghost-Multiplayer",20,(255,255,255),(333,20))
                                                if (frame_counter > 200 and frame_counter < 300):
                                                        show_text("You can only influence your opponent directly",20,(255,255,255),(333,20))
                                                if (frame_counter > 300 and frame_counter < 400):
                                                        show_text("If one person finishes a level",20,(255,255,255),(333,20))
                                                if (frame_counter > 400 and frame_counter < 500):
                                                        show_text("He gets the Bonusscore and the level ends",20,(255,255,255),(333,20))
                                                if (frame_counter > 500 and frame_counter < 600):
                                                        show_text("May the fastest win",20,(255,255,255),(333,20))
                                        if frame_counter > 500000000: frame_counter = 0
                                        if not multiplayer:
                                                if old_death_counter < death_counter or dead_show > 0:
                                                        dead_show -= 1
                                                        dead_string = "-" + str(death_counter*10)
                                                        show_text(dead_string,scorechange_size,(155,0,0),(250,42))
                                                if kill_counter > 0:
                                                        kill_counter -= 1
                                                        kill_string = "+10"
                                                        show_text(kill_string,scorechange_size,(0,155,0),(250,42))
                                                        
                                if not multiplayer_ghostmode and not TOMFAKTOR:
                                                show_text("P1 Kills: " + str(opponentscore),20,(255,255,255),(200,20))
                                                show_text("P2 Kills: "+ str(death_counter),20,(55,55,55),(200,50))
                                                if (frame_counter > 100 and frame_counter < 200):
                                                        show_text("Welcome to the Duell-Mode",20,(255,255,255),(333,20))
                                                if (frame_counter > 200 and frame_counter < 300):
                                                        show_text("2 Players, unlimited ammo, 10 Lives",20,(255,255,255),(333,20))
                                                if (frame_counter > 300 and frame_counter < 400):
                                                        show_text("Let's dance!",20,(255,255,255),(333,20))
                                                if (frame_counter > 400 and frame_counter < 500):
                                                        show_text("But remember, not every hit kills",20,(255,255,255),(333,20))
                                        
                                lebenscounter = 0
                                for life in range(0,w.spieler.hitpoints):
                                        distance = 20
                                        if multiplayer_ghostmode: lifeheight = 50
                                        else: lifeheight = 20
                                        DISPLAYSURF.blit(lebensanzeige,(distance+ lebenscounter * 30,lifeheight))
                                        lebenscounter += 1
                                if not multiplayer_ghostmode:
                                        lebenscounter = 0
                                        for life in range(0,w.anderer_spieler.hitpoints):
                                                distance = 20
                                                lifeheight = 50
                                                DISPLAYSURF.blit(lebensanzeige2,(distance+ lebenscounter * 30,lifeheight))
                                                lebenscounter += 1                                        
                                        
                                        


                                pygame.display.flip()
                                if not multiplayer_ghostmode:
                                        if death_counter >= 10:
                                                send_data((playing_Spieler, # Spieler 1 oder 2
                                                                           (current_level.spieler.direction,current_level.spieler.state), #  Richtung in die er schaut und sprite_in_use
                                                                           (current_level.spieler.body.position.x,current_level.spieler.body.position.y), # Positition des Spielers
                                                                           ((current_level.spieler.direction,new_kugel)),# "Neue Kugel" (De facto alles um eine zu erstellen)
                                                                             (current_level.spieler.hitpoints,death_counter)))

                                                return False,1,1,"duell","lost"
                                        elif opponentscore >= 10: return False,1,1,"duell","won"                                        
                                if w.finish and __name__ != "__main__":
                                        old_score = score
                                        score += bonustime
                                        if multiplayer: send_data(("level finished",game.index(current_level)))
                                        if game.index(current_level) + 1 < len(game): return True, old_score,bonustime, "won"
                                        else: return False, old_score,bonustime, "won"

def show_text(text,size,color,position):
        thisPrint = pygame.font.Font('freesansbold.ttf', size).render(text,True,color)
        thisRect = thisPrint.get_rect()
        thisRect.x = position[0]
        thisRect.y = position[1]
        DISPLAYSURF.blit(thisPrint,thisRect)
def construct_level(level,players):
        global final_boss
        blocks = []
        leveldesign_block = pygame.image.load(Level.level_grounds[level]).convert() # z.B. level1_ground oder so
        for blockkoord in Level.blockkoords[level]:
            blocks.append(Boden.Block(pygame.Rect(blockkoord[0],blockkoord[1],
                                                      blockkoord[2],blockkoord[3]), leveldesign_block))
        texts = []
        if not TOMFAKTOR:
                for textbox in Level.textboxes[level]:
                        texts.append(Boden.Textbox(pygame.Rect(textbox[0],textbox[1],textbox[2],textbox[3],),pygame.font.Font('freesansbold.ttf', textbox[4]).render(textbox[5],True,(255,255,255))))
        enemys = []
        for gegner in Level.bodengegner[level]:
                if gegner[2] == Level.zyklop_sprite: enemys.append(Hindernis.Gegner(blocks[gegner[0]],gegner[1],gegner[2],gegner[3],gegner[4],1))
                else:enemys.append(Hindernis.Gegner(blocks[gegner[0]],gegner[1],gegner[2],gegner[3],gegner[4]))
        for gegner in Level.fluggegner[level]:
            enemys.append(Hindernis.FliegenderGegner(gegner[0],gegner[1],gegner[2],gegner[3],gegner[4],gegner[5],gegner[6],gegner[7]))
        if level == 5:
                final_boss = Hindernis.Endgegner(4100,4700,3400,15,Level.endgegner_sprite,10,20)
                enemys.append(final_boss)
                
        waypoints = []
        for speicherpunkt in Level.speicherpunkte[level]:
                waypoints.append(Speicherpunkt.Speicherpunkt(blocks[speicherpunkt], [waypoint_sprite]))
        powerups = []
        for powerup in Level.powerups[level]:
                if powerup[0] == "highjump":
                        powerups.append(Power_Ups.High_Jump(blocks[powerup[1]], [highjump_sprite]))
                if powerup[0] == "dash":
                        powerups.append(Power_Ups.DashPW(blocks[powerup[1]], [dashPW_sprite]))
        spaceshuttles = []
        for stein in Level.steine[level]:
                        spaceshuttles.append(Boden.Stein(blocks[stein], turbine_sprite))
        p = Speicherpunkt.Portal(blocks[Level.portale[level]], [portal2_sprite])
        bild = pygame.image.load(Level.bg_bilder[level]).convert()
        w = Welt(bild,blocks,enemys,powerups,spaceshuttles,waypoints,p,players[0],players[1],texts)
        return w

def load_screen(level):
        loadstring = "Loading: "
        loadpos = (611,30)
        if level == 0:
                loadstring += "Tutorial"
        elif level == 6:
                loadstring += "Battleground"
                loadpos = (555,30)
        else:
                loadstring += "Level " + str(level)
        DISPLAYSURF.fill((0,0,0))
        show_text(loadstring,20,(155,155,155),loadpos)
        pygame.display.flip() 

def set_everything(start_level):
        #SPIELER
        s = Spieler()
        s2 = Spieler()
        global current_level,game,score
        game = []
        load_screen(start_level)
        if start_level == 0:
                game.append(construct_level(0,(s,s2)))
        elif start_level == 6:
                game.append(construct_level(6,(s,s2)))
        elif start_level == 7:
                game.append(construct_level(7,(s,s2))) 
        else:
                for w in range(start_level,7):
                        if w < 6: load_screen(w)
                        x = construct_level(w,(s,s2))
                        game.append(x)
                        if w == 3: x.sterbehoehe = 4000
                        if w == 4: x.sterbehoehe = 100
        current_level = game[0]#start_level
        score = 0 
def change_world_parameters_multi(w):
        if playing_Spieler == 1:
                w.spieler = current_level.spieler1# Der Spieler den dieser PC steuert
                w.anderer_spieler = current_level.spieler2
                if multiplayer_ghostmode:
                        w.anderer_spieler.shape.collision_type = 0
                else:
                        w.speicherpunkte.insert(0, Speicherpunkt.Speicherpunkt(w.boeden[0], [waypoint_sprite]))
                        current_speicherpunkt = w.speicherpunkte[0]
                        w.anderer_spieler.shape.collision_type = 3
                awaiting_snd_player = True
                while awaiting_snd_player:
                        p2_data = send_data((playing_Spieler,(),(),(),()))# Spieler 1 oder 2
                        for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                                        send_data("gg")
                                        pygame.quit()
                                        sys.exit()
                                elif event.type == KEYDOWN:
                                        if event.key == K_F12: # Für Beenden und zurück zum startmenü
                                                send_data("gg")
                                                return (False,score,-1)
                        pygame.display.flip()
                        if p2_data != None:     awaiting_snd_player = False    
        else:
                w.spieler = current_level.spieler2
                w.anderer_spieler = current_level.spieler1
                if multiplayer_ghostmode: w.anderer_spieler.shape.collision_type = 0
                else:
                        w.speicherpunkte = []
                        w.speicherpunkte.insert(0, Speicherpunkt.Speicherpunkt(w.boeden[4], [waypoint_sprite]))
                        current_speicherpunkt = w.speicherpunkte[0]
                        w.anderer_spieler.shape.collision_type = 3            
          
def on_execute(multi_True = False,start_level = 1, ghostmode = True): # Multiplayer starten oder Singleplayer (bei False singleplayer)
        global multiplayer,survival_time,playing_Spieler,multiplayer_ghostmode, current_level, current_speicherpunkt, startlevel
        startlevel = start_level       
        multiplayer = multi_True
        multiplayer_ghostmode = ghostmode
        survival_time = time.time()#Für Highscore
        
        if multiplayer: # Start nur aus dem Menü heraus
                        playing_Spieler,p2_ghostmode = get_player_number(multiplayer_ghostmode)
                        if playing_Spieler == 2 and not p2_ghostmode:
                                multiplayer_ghostmode = p2_ghostmode
                                set_everything(6)
                        elif not ghostmode: set_everything(6)
                        else: set_everything(1)
                        for w in game:
                                change_world_parameters_multi(w)      
        else:   #Singleplayer
                set_everything(start_level)
                for w in game: w.spieler = w.spieler1
        if __name__ == "__main__": main()
        else:  return main() # start aus dem Menü heraus




if __name__ == "__main__":      on_execute(multiplayer,test_startlvl)
