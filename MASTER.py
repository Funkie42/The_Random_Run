import sys, pygame, pymunk, time, random, copy
import Boden, Hindernis, Power_Ups, SpriteSheet, Speicherpunkt, Level,cProfile, copy
from pygame.locals import*
from copy import deepcopy
from Gameclient import *

playing_Spieler = 0 # Zu setzen auf 1 bzw. 2
multiplayer = False
multiplayer_ghostmode = True
survival_time = 0
score = 0
test_startlvl = 4# Für Testen
hitpoints = 5
death_counter = 0
dead_show = 0

TOMFAKTOR = False # Weil tom keinen Text anzeigen kann

jump_sound = "Sounds/jump.wav"
explosion_sound = "Sounds/dead.wav"
die_sound = "Sounds/aah.wav"
kugel_sound  = "Sounds/phaser.wav"
portal_sound = "Sounds/swoop.wav"
waypoint_sound = "Sounds/wp.wav"
rocket_sound = "Sounds/rocket_sound.wav"



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
                self.hitpoints = hitpoints
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
                        x = self.sprite.get_image(25 + self.spalte * self.sprite.sprite_sheet.get_width()/17 , 5, self.sprite.sprite_sheet.get_width()/17 -55, self.sprite.sprite_sheet.get_height() - 5)
                        #x = pygame.transform.scale(x, (90, 130))
                        return x
                else:
                        x = pygame.transform.flip(self.sprite.get_image(25 + self.spalte * self.sprite.sprite_sheet.get_width()/17 , 5, self.sprite.sprite_sheet.get_width()/17 -55, self.sprite.sprite_sheet.get_height() - 5), True, False)
                        #x = pygame.transform.scale(x, (90, 130))
                        return x


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
                pygame.mixer.Sound(jump_sound).play()
                if current_level.spieler.body.velocity.y > 0:
                        self.body.velocity.y = -self.jumpPower
                else:
                        self.body.velocity.y = -self.jumpPower

        def move(self):
            self.body.position.x += self.direction * self.moveSpeed
            hintergrund_rect.left += 4 * self.direction

        def dash(self):
                if self.dash_counter > 0:
                        pass
                        self.body.position.x += 60 * self.direction
                        ###################################self.dash_counter -= 1

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
                for i in self.textboxes:
                        space.remove(i.shape)
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
                        if (i.body.position.y > LEVELSURF.get_height() - self.sterbehoehe or i.hitpoints < 0 )and i in self.hindernisse: #evtl zu updaten
                                ex = Explotion(i.body)
                                self.hindernisse.remove(i)
                                space.remove(i.body, i.shape)
                        if rect.colliderect(i.center_rect()):
                                LEVELSURF.blit(i.current_sprite(), i.center_rect())
                                random_int = random.randint(0,800)
                                if random_int == 100:
                                        i.engage(self.spieler.body.position.x)
                                if i.kugel_counter == i.feuerrate:
                                        k = Kugel((1200 * i.direction, -50),((245,12,188)), i.body.position.x + (15 * i.direction), i.body.position.y - 10, False)
                                        k.shape.collision_type = 3
                                        k.shape.sprite_group = 2
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
                        if multiplayer:  self.anderer_spieler.sprite = character2_sprite
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
        def __init__(self, vec,farbe, x_pos = 0, y_pos = 0, spielerdir = 0): ###################XPOS YPOS geändert für Multiplayer
                object.__init__(self)                   #Spielerdir = 0 heißt eigener Player direction
                pygame.mixer.Sound(kugel_sound).play()
                self.vec = vec
                self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 7, 7))
                self.farbe = farbe
                ###########################
                if x_pos == 0:
                        x_pos = current_level.spieler.body.position.x
                if y_pos == 0:
                        y_pos = current_level.spieler.body.position.y
                if spielerdir == 0:
                        spielerdir = current_level.spieler.direction
                self.body.position = (x_pos +60 * spielerdir,
                                      y_pos - 35)
                ##############################
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
                current_level.spieler.hitpoints -= 1
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
                current_level.spieler.hitpoints -= 1
                current_level.spieler.body.velocity.x = -450 * current_level.spieler.direction
                current_level.spieler.body.velocity.y = -750
                #current_level.spieler.moveSpeed = 0
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
        random_int = random.randint(0,100)
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
        
        #current_level.removeFromSpace()
        current_level.removeFromSpace()
        pygame.mixer.Sound(portal_sound).play()
        current_level.finish = True
        if game.index(current_level) + 1 < len(game):
                current_level = game[game.index(current_level) + 1]
                #current_speicherpunkt = current_level.speicherpunkte[0]
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
                #rint(arbiter.shapes[1].body.velocity_func)
                pass
               
        return True

def player_leaves_stein(space, arbiter):
        current_level.spieler.onStein = False

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
turbine_sprite = SpriteSheet.SpriteSheet("Gui/turbine_sprite.png")
explosion_sprite = SpriteSheet.SpriteSheet("Gui/explotion.png")

lebensanzeige = pygame.image.load("Gui/powerups/heart.png")#.convert()
lebensanzeige = pygame.transform.scale(lebensanzeige,(25,25))

#SPIELER
s = Spieler()
s2 = Spieler()


#SPIEL
game = []
current_level = None
backup_hintergrund_rect = copy.deepcopy(hintergrund_rect)
kugeln = []
explosions = []


def main():
        global score,dead_show
        start_time = time.time()
        pause_time = 0
        bonustime = 300
        frame_counter = 0       
        for w in game:
                        global death_counter
                        death_counter = 0
                        while not w.finish and w == current_level:
                                old_death_counter = death_counter
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
                                                        w.finish = True
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
                                        k = Kugel((1200 * current_level.spieler.direction, -100),(218,165,32))        

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
                                if w.spieler.hitpoints <= 0: w.spieler.is_alive = False
                                if (frame_counter % 1 == 0): LEVELSURF.blit(hintergrund_blit(),(rect.left -10, rect.top -10))
                                w.update()
                                for i in kugeln: i.update()
                                for i in explosions: i.update()
                                pygame.draw.rect(LEVELSURF,(155,0,0),pygame.Rect(0,LEVELSURF.get_height() - w.sterbehoehe,LEVELSURF.get_width(),3))
                                space.step(1/35)
                                clock.tick(25)
                                DISPLAYSURF.blit(camera_blit(), (0,0))

                                ### Highscoreanzeige ###
                                if bonustime > 0: bonustime = 300 - int(time.time() - start_time - pause_time)
                                else: bonustime = 0
                                thisRect = None
                                if not TOMFAKTOR:
                                        score_string = "Bonustime: " + str(bonustime) + "     Score: " + str(score)
                                        thisPrint = pygame.font.Font('freesansbold.ttf', 20).render(score_string,True,(255,255,255))
                                        thisRect = thisPrint.get_rect()
                                        thisRect.center = ((150,40))
                                        DISPLAYSURF.blit(thisPrint,thisRect)
                                        if (frame_counter > 1800 and frame_counter < 1850):
                                                die_string = "Press F5 to instantly die painfully"
                                                diePrint = pygame.font.Font('freesansbold.ttf', 20).render(die_string,True,(255,255,255))
                                                dieRect = diePrint.get_rect()
                                                dieRect.center = ((470,40))
                                                DISPLAYSURF.blit(diePrint,dieRect)
                                        if (frame_counter > 1850 and frame_counter < 1900):
                                                die_string = "Press 'Q' to give up and go home"
                                                diePrint = pygame.font.Font('freesansbold.ttf', 20).render(die_string,True,(255,255,255))
                                                dieRect = diePrint.get_rect()
                                                dieRect.center = ((470,40))
                                                DISPLAYSURF.blit(diePrint,dieRect)
                                        if frame_counter > 500000000: frame_counter = 0
                                        if old_death_counter < death_counter or dead_show > 0:
                                                dead_show -= 1
                                                dead_string = "-" + str(death_counter*10)
                                                deadPrint = pygame.font.Font('freesansbold.ttf', 35).render(dead_string,True,(155,0,0))
                                                deadRect = thisPrint.get_rect()
                                                deadRect.center = ((380,70))
                                                DISPLAYSURF.blit(deadPrint,deadRect)       

                                        
                                lebenscounter = 0
                                for life in range(0,w.spieler.hitpoints):
                                        if not TOMFAKTOR: distance = thisRect.x
                                        else: distance = 20
                                        DISPLAYSURF.blit(lebensanzeige,(distance+ lebenscounter * 30,60))
                                        lebenscounter += 1
                                        


                                pygame.display.flip()
                                
                                if w.finish and __name__ != "__main__":
                                        #print(game.index(current_level))
                                        #print(game.index(current_level) + 1 < len(game))
                                        old_score = score
                                        score += bonustime
                                        if game.index(current_level) + 1 < len(game): return True, old_score,bonustime
                                        else: return False, old_score,bonustime
                                
def construct_level(level):
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
            enemys.append(Hindernis.Gegner(blocks[gegner[0]],gegner[1],gegner[2],gegner[3],gegner[4]))
        for gegner in Level.fluggegner[level]:
            enemys.append(Hindernis.FliegenderGegner(gegner[0],gegner[1],gegner[2],gegner[3],gegner[4],gegner[5],gegner[6],gegner[7]))
        waypoints = []
        for speicherpunkt in Level.speicherpunkte[level]:
                waypoints.append(Speicherpunkt.Speicherpunkt(blocks[speicherpunkt], [waypoint_sprite]))
        powerups = []
        for powerup in Level.powerups[level]:
                if powerup[0] == "highjump":
                        powerups.append(Power_Ups.High_Jump(blocks[powerup[1]], [highjump_sprite]))
        spaceshuttles = []
        for stein in Level.steine[level]:
                        spaceshuttles.append(Boden.Stein(blocks[stein], turbine_sprite))
        p = Speicherpunkt.Portal(blocks[Level.portale[level]], [portal2_sprite])
        bild = pygame.image.load(Level.bg_bilder[level]).convert() 
        return Welt(bild,blocks,enemys,powerups,spaceshuttles,waypoints,p,s,s2,texts)

        
def set_everything(start_level):
        global current_level,game,score
        tut_w = construct_level(0)
        w1 = construct_level(1)
        w2 = construct_level(2)
        w3 = construct_level(3)
        w3.sterbehoehe = 4000
        w4 = construct_level(4)
        wend = construct_level(0)
        game = [tut_w,w1,w2,w3,w4,wend] 
        current_level = game[start_level]
        score = 0 
        #for w in game:
        #        w.finish = False
                
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



