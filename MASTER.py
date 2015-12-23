import sys, pygame, pymunk, Boden, Hindernis, Power_Ups, SpriteSheet, Speicherpunkt
from pygame.locals import*
from copy import deepcopy

class Spieler(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.sprite_iterator = 0
                self.sprite_list = ([man1], listman, [man2], [], [], [], [])

                self.reihe = 0
                self.spalte = 0
                
                self.state = 0 # 0 = stand, 1 = move, 2 = jump, 3 = fall, 4 = duck, 5 = roll, 6 = schlittern

                self.jump_force = (0,0)

                self.sprite = woman
                
                self.double_jump_iterator = 0

                self.direction = 1 #1 = rechts, -1 = links

                self.mass = 100

                self.body = pymunk.Body(self.mass, pymunk.inf)
                self.body.position = (800, 1500)
                self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
                space.add(self.body, self.shape)
                self.shape.collision_type = 1

                self.dash_counter = 0
                self.double_jump_counter = 1

                self.is_Grounded = False
                self.is_Alive = True

        def rect(self):
                x = pygame.Rect(0,0, self.current_sprite().get_width(), self.current_sprite().get_height())
                x.center = self.body.position
                return x

        def current_sprite(self):
                #return self.sprite_list[self.state][self.sprite_iterator]
                if self.direction == 1:
                        return self.sprite.get_image(self.spalte * self.sprite.sprite_sheet.get_width()/7 , self.reihe * self.sprite.sprite_sheet.get_height()/3, self.sprite.sprite_sheet.get_width()/7, self.sprite.sprite_sheet.get_height()/3)
                else:
                         return pygame.transform.flip(self.sprite.get_image(self.spalte * self.sprite.sprite_sheet.get_width()/7 , self.reihe * self.sprite.sprite_sheet.get_height()/3, self.sprite.sprite_sheet.get_width()/7, self.sprite.sprite_sheet.get_height()/3), True, False)


        def state_update(self):
                keys = pygame.key.get_pressed()
                if self.direction == 1 and keys[K_LEFT] and not keys[K_RIGHT]:
                        self.direction = -1
                        #self.rev_sprite_list()
                elif self.direction == -1 and keys[K_RIGHT] and not keys[K_LEFT]:
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
                        self.body.velocity.y = -650
                else:
                        self.body.velocity.y = -650

        def move(self):
            self.body.position.x += self.direction * 15
            hintergrund_rect.left += 2 * self.direction

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
                                        

                        
                LEVELSURF.blit(self.current_sprite(), self.rect())
                #self.sprite_iterator += 1
              


#WELT/LEVELKLASSE
class Welt():
        def __init__(self, BACKGROUNDSURF, boeden, hindernisse, power_ups, speicherpunkte, spieler):
                self.BACKGROUNDSURF = BACKGROUNDSURF
                self.BACKGROUNDSURF = pygame.transform.scale(self.BACKGROUNDSURF, (LEVELSURF.get_width(), LEVELSURF.get_height()))
                self.boeden = boeden
                self.hindernisse = hindernisse
                self.power_ups = power_ups
                self.speicherpunkte = speicherpunkte
                self.speicherpunkte.insert(0, Speicherpunkt.Speicherpunkt(self.boeden[0], [man1]))
                global current_speicherpunkt
                current_speicherpunkt = self.speicherpunkte[0]
                self.spieler = spieler
                self.finish = False
                self.init = False
                for i in self.boeden:
                        space.add(i.shape)
                for i in self.hindernisse:
                        i.init(space)
                for i in self.power_ups:
                        space.add(i.body, i.shape)
                for i in self.speicherpunkte:
                        space.add(i.shape)
               

        def update(self):
                global current_speicherpunkt
                if not self.init:
                        self.spieler.body.position.x = current_speicherpunkt.rect.left + 50
                        self.spieler.body.position.y = current_speicherpunkt.rect.top - 200
                        self.init = True
                        
                self.spieler.state_update()
                
                for i in self.boeden:
                        if rect.colliderect(i.center_rect()) and i.center_rect().top < LEVELSURF.get_height() - 200:
                                i.update()
                                LEVELSURF.blit(i.surf, (i.center_rect()))
                                #pygame.draw.polygon(LEVELSURF, ((34,66,34)), i.shape.get_vertices())
                               # pygame.draw.circle(LEVELSURF, ((4,5,6)), (int(i.body.position.x), int(i.body.position.y)), 10)
                               
                for i in self.hindernisse:
                        if i.body.position.y > LEVELSURF.get_height() - 200 and i in self.hindernisse: #evtl zu updaten
                                self.hindernisse.remove(i)
                                space.remove(i.body, i.shape)
                        if rect.colliderect(i.center_rect()):
                                i.update()
                                LEVELSURF.blit(i.current_sprite(), i.center_rect())
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

                for i in self.speicherpunkte:
                         if rect.colliderect(i.rect):
                                LEVELSURF.blit(i.sprite_list[i.sprite_iterator], i.rect)
                         if self.spieler.rect().colliderect(i.rect):
                                 global current_speicherpunkt
                                 current_speicherpunkt = i
                                 self.speicherpunkte.remove(i)
                                 space.remove(i.shape)
                                 
                                 
                                 
                        
                if self.spieler.body.position.y > LEVELSURF.get_height() - 200:
                        self.spieler.body.velocity.y = -50
                        self.spieler.body.position = (current_speicherpunkt.rect.left + 50, current_speicherpunkt.rect.top - 200)
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
                surf = current_levelBACKGROUNDSURF.subsurface(hintergrund_rect)
                return surf         
        except:
                hintergrund_rect.left = 0
                surf = current_level.BACKGROUNDSURF.subsurface(hintergrund_rect)
                return surf

#COLLISIONHANDLER

def touch(space, arbiter):
        s.is_Grounded = True
        s.double_jump_counter = 1
        s.body.velocity.x = 0
        return True

def cänt_touch_dis(space, arbiter):
        s.is_Grounded = False
        #print(s.is_Grounded)
        return True

def kugel_hits_gegner(space, arbiter):
        arbiter.shapes[0].body.velocity.y -= 400
        arbiter.shapes[0].body.velocity.x += 150 * s.direction
        return True

def kugel_hits_fliegender_gegner(space, arbiter):
        try:
                space.add(arbiter.shapes[0].body)
                return True
        except:
                return False
        

def player_hits_kugel(space, arbiter):
        arbiter.shapes[1].body.velocity.y -= 1000
        arbiter.shapes[1].body.velocity.x += 1 * s.direction
        #print("DEPP")
        return True

def player_jumps_gegner(space, arbiter):
        if arbiter.contacts[0].normal.int_tuple[0] == 0:
                s.body.velocity.y = -650
                s.double_jump_counter = 1
                #print("HURA")
        else:
                s.body.position.y -= 30
                s.body.velocity.y = -500
                s.body.velocity.x = - 500 * s.direction
        return True

def player_jumps_fliegender_gegner(space, arbiter):
        if arbiter.contacts[0].normal.int_tuple[0] == 0:
                s.body.velocity.y = -650
                s.double_jump_counter = 1
                space.add(arbiter.shapes[1].body)
                arbiter.shapes[1].collision_type = 3
        else:
                s.body.position.y -= 30
                s.body.velocity.y = -500
                s.body.velocity.x = - 500 * s.direction
        return True

def player_jumps_highjump(space, arbiter):
        if arbiter.contacts[0].normal.int_tuple[0] == 0:
                s.body.velocity.y = -1000
                print("DEPP")
        else:
                arbiter.shapes[1].body.position.x += 5 * s.direction
        return True

def kugel_hits_highjump(space, arbiter):
        arbiter.shapes[1].body.position.x += 20 * s.direction
        arbiter.shapes[0].group = 2
        return True
        

# UNIVERSELLE OPTIONEN
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 800))
LEVELSURF = pygame.Surface((6000, 8000))
space = pymunk.Space()
space.add_collision_handler(1,2,post_solve=touch, separate=cänt_touch_dis)
space.add_collision_handler(3,4, begin=kugel_hits_gegner)
#space.add_collision_handler(6,4, begin=kugel_hits_fliegender_gegner)
space.add_collision_handler(1,4, begin=player_hits_kugel)
space.add_collision_handler(1,3, begin=player_jumps_gegner)
space.add_collision_handler(1,6, begin=player_jumps_fliegender_gegner)
space.add_collision_handler(1,5, post_solve=player_jumps_highjump)
space.add_collision_handler(4,5, begin=kugel_hits_highjump)
space.gravity = (0, 1500)
clock = pygame.time.Clock()
fps = 25

#KAMERARECTS
rect = pygame.Rect(0,0,DISPLAYSURF.get_width(),DISPLAYSURF.get_height())
hintergrund_rect =pygame.Rect(0,300,DISPLAYSURF.get_width()+ 50,DISPLAYSURF.get_height()+50)

#SPIELERSPRITES
man1 = pygame.image.load("Gui/man1.png")
man1 = pygame.transform.scale(man1,(80,100))
man2 = pygame.image.load("Gui/man2.png")
man2 = pygame.transform.scale(man2,(80,100))
man3 = pygame.image.load("Gui/man3.png")
man3 = pygame.transform.scale(man3,(80,100))
man4 = pygame.image.load("Gui/man4.png")
man4 = pygame.transform.scale(man4,(80,100))
listman = [man1, man2, man3, man4]
woman = SpriteSheet.SpriteSheet("Gui/player.png")

#GELÄNDESPRITES
mars = pygame.image.load("Gui/ground.png")

#SPIELER
s = Spieler()

#LEVEL1
bl = Boden.Block(pygame.Rect(0,2000,1200,50), mars)
bl1 = Boden.Block(pygame.Rect(700,2400,600,50), mars)
bl2 = Boden.Block(pygame.Rect(1400,1900,600,50), mars)
bl3 = Boden.Block(pygame.Rect(1800,1500,600,50), mars)
bl4 = Boden.Block(pygame.Rect(2000,2000,600,50), mars)
bl5 = Boden.Block(pygame.Rect(2500,1800,600,50), mars)
bl6 = Boden.Block(pygame.Rect(3000,2000,600,50), mars)
bl7 = Boden.Block(pygame.Rect(3600,2400,600,50), mars)
bl8 = Boden.Block(pygame.Rect(4200,2400,50,200), mars)
bl9 = Boden.Block(pygame.Rect(4500,2200,600,50), mars)
bl10 = Boden.Block(pygame.Rect(4900,2100,600,50), mars)
bl11 = Boden.Block(pygame.Rect(5200,2000,600,50), mars)

g = Hindernis.Gegner(bl, 15,woman, 3)
g2 = Hindernis.FliegenderGegner(400, 900, 1800, 15, woman, 3)

p = Power_Ups.High_Jump(bl3,  [man1])

sp = Speicherpunkt.Speicherpunkt(bl4, [man1])

current_speicherpunkt = False
w1 = Welt(pygame.image.load("Gui/wald.jpg"), [bl,bl1,bl2,bl3,bl4,bl5,bl6,bl7,bl8,bl9,bl10,bl11,], [g, g2], [p], [sp], s)

#LEVEL2
#w2 = Welt( pygame.image.load("Gui/wald.jpg"), [], [], [], [], s, 500, 1500)

#SPIELER
game = [w1]
current_level = w1
kugeln = []


while True:
        for w in game:
                current_level = w
                while not w.finish:
                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                elif event.type == KEYDOWN:
                                        if event.key == K_SPACE:
                                                if s.is_Grounded:
                                                        s.jump()
                                                else:
                                                        if s.double_jump_counter > 0:
                                                                s.jump()
                                                                s.double_jump_counter -= 1
                                        if event.key == K_UP:
                                                k = Kugel((900 * s.direction, -75))
                                        if event.key == K_d:
                                                if not s.is_Grounded:
                                                        s.dash_counter += 5
                                                        
                        keys = pygame.key.get_pressed()
                        if keys[K_RIGHT] or keys[K_LEFT]:
                                s.move()
                                
                        LEVELSURF.fill((65, 165, 200, 0.5))
                        #LEVELSURF.blit(hintergrund_blit(), (rect.left -25, rect.top -25))
                        #LEVELSURF.blit(current_level.BACKGROUNDSURF, (0,0))
                        w.update()
                        
                        for i in kugeln:
                                i.update()
                                
                        space.step(1/35)
                        clock.tick(fps)
                        #print(len(space.bodies))
                        print(current_speicherpunkt)
                        DISPLAYSURF.blit(camera_blit(), (0,0))
                        pygame.display.flip()
                        #pygame.quit()
                        #sys.exit()
