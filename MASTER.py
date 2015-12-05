import sys, pygame, pymunk, Boden, Hindernis
from pygame.locals import*

class Spieler(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)

                self.x = 200
                self.y = 100


                self.sprite_iterator = 0
                self.sprite_list = ([man1], listman, [man2], [], [], [], [])

                self.state = 0 # 0 = stand, 1 = move, 2 = jump, 3 = fall, 4 = duck, 5 = roll, 6 = schlittern

                self.jump_force = (0,0)

                self.double_jump_iterator = 0

                self.direction = 1 #1 = rechts, -1 = links

                self.mass = 200

                self.body = pymunk.Body(self.mass, pymunk.inf)
                self.body.position = (800, 500)
                self.shape = pymunk.Poly.create_box(self.body, (self.current_sprite().get_width(), self.current_sprite().get_height()))
                space.add(self.body, self.shape)
                self.shape.collision_type = 1

                self.is_Grounded = False

        def rect(self):
                x = pygame.Rect(self.x, self.y, self.current_sprite().get_width(), self.current_sprite().get_height())
                x.center = self.body.position
                return x

        def current_sprite(self):
                return self.sprite_list[self.state][self.sprite_iterator]
                

        def rev_sprite_list(self):
                for i in range(len(self.sprite_list)):
                        for j in range(len(self.sprite_list[i])):
                                self.sprite_list[i][j] = pygame.transform.flip(self.sprite_list[i][j], True, False)

        def state_update(self):
                keys = pygame.key.get_pressed()
                if self.direction == 1 and keys[K_LEFT] and not keys[K_RIGHT]:
                        self.direction = -1
                        self.rev_sprite_list()
                elif self.direction == -1 and keys[K_RIGHT] and not keys[K_LEFT]:
                        self.direction = 1
                        self.rev_sprite_list()
                if self.is_Grounded and not (keys[K_RIGHT] or keys[K_LEFT]):
                        self.state = 0
                elif self.is_Grounded and (keys[K_RIGHT] or keys[K_LEFT]):
                        self.state = 1     
                elif not self.is_Grounded:
                        self.state = 2

                        
        def jump(self):
                self.body.velocity.y -= 400
                #for i in w.boeden:
                   # i.body.velocity.y += 400

        def move(self):
            self.body.position.x += self.direction * 15

        def selfblit(self):
                if self.sprite_iterator >= len(self.sprite_list[self.state]):
                    self.sprite_iterator = 0
                LEVELSURF.blit(self.current_sprite(), self.rect())
                self.sprite_iterator += 1

        def update(self):
                self.state_update()
                self.selfblit()
                
               # print(self.rect().midbottom)
                #print(self.body.position)
              #  pygame.draw.polygon(DISPLAYSURF, ((0,70,0)), self.shape.get_vertices())
               # print(self.shape.bb)
                #print(self.state)
                



class Welt():
        def __init__(self, boeden, hindernisse, power_ups, spieler):
                self.boeden = boeden
                self.hindernisse = hindernisse
                self.power_ups = power_ups
                self.spieler = spieler
                self.moveSpeed = 0
                self.maxMoveSpeed = 16
                for i in self.boeden:
                                        space.add(i.shape)
                for i in self.hindernisse:
                        space.add(i.body, i.shape)

        def move(self):
            if self.moveSpeed < self.maxMoveSpeed:
                self.moveSpeed += 0.5
            for i in self.boeden:
                i.body.position.x -= self.moveSpeed * self.spieler.direction
               

        def update(self):
                self.spieler.state_update()
                for i in self.boeden:
                        i.update()
                        #i.shape.bb
                        #i.body.update_position(i.body, 1/50)
                        LEVELSURF.blit(i.surf, (i.center_rect()))
                        #pygame.draw.polygon(LEVELSURF, ((34,66,34)), i.shape.get_vertices())
                       # pygame.draw.circle(LEVELSURF, ((4,5,6)), (int(i.body.position.x), int(i.body.position.y)), 10)
                for i in self.hindernisse:
                        i.update()
                        LEVELSURF.blit(i.blit_surf(), i.center_rect())
                        #pygame.draw.circle(LEVELSURF, ((4,5,6)), (int(i.body.position.x), int(i.body.position.y)), 10)
                        #pygame.draw.polygon(LEVELSURF, ((34,66,34)), i.shape.get_vertices())
                        
                self.spieler.body.update_position(self.spieler.body, 1/50)
                self.spieler.shape.bb
                self.spieler.selfblit()
                #pygame.draw.polygon(LEVELSURF, ((76, 45, 98)), self.spieler.shape.get_vertices())
                #pygame.draw.circle(LEVELSURF, ((45,34,23)), (int(self.spieler.body.position.x), int(self.spieler.body.position.y)), 10)
                
                if self.moveSpeed > 0:
                        self.moveSpeed -= 0.25


class Kugel():
        def __init__(self, vec):
                self.vec = vec
                self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 10))
                self.body.position = (s.body.position.x +40 * s.direction, s.body.position.y - 40)
                self.shape = pymunk.Circle(self.body, 10)
                space.add(self.body, self.shape)
                self.body.apply_impulse(vec)
                kugeln.append(self)

        def update(self):
                pygame.draw.circle(LEVELSURF, ((0,0,0)), (int(self.body.position.x), int(self.body.position.y)), 10)
        

pygame.init()


man1 = pygame.image.load("man1.png")
man2 = pygame.image.load("man2.png")
man3 = pygame.image.load("man3.png")
man4 = pygame.image.load("man4.png")
listman = [man1, man2, man3, man4]
listman2 = [man1, man2, man3, man4]
listman3 = [man1, man2, man3, man4]
listman4 = [man1, man2, man3, man4]
listman5 = [man1, man2, man3, man4]
DISPLAYSURF = pygame.display.set_mode((1000,800))
LEVELSURF = pygame.Surface((4000, 8000))
space = pymunk.Space()
mars = pygame.image.load("ground.png")
bl = Boden.Block(pygame.Rect(0,400,600,50), mars)
bl2 = Boden.Block(pygame.Rect(800, 650, 300, 50), mars)
bl4 = Boden.Block(pygame.Rect(1400, 800, 300, 50), mars)
bl5 = Boden.Block(pygame.Rect(2000 ,900, 300, 50), mars)
bl3 = Boden.Block(pygame.Rect(2500, 700, 300, 50), mars)
g = Hindernis.Gegner(bl4, 15, listman2, 3)
g2 = Hindernis.Gegner(bl5, 15, listman3, 3)
g3= Hindernis.Gegner(bl3, 15, listman4, 3)
g4 = Hindernis.Gegner(bl, 15, listman5, 3)
s = Spieler()
kugeln = []
w = Welt([bl, bl2, bl3, bl4, bl5], [g,g2,g3,g4], [], s)

def touch(space, arbiter):
        s.is_Grounded = True
        #print(s.is_Grounded)
        return True;

def cänt_touch_dis(space, arbiter):
        s.is_Grounded = False
        #print(s.is_Grounded)
        return True

rect = pygame.Rect(0,0,1000,800)
def camera_blit():
        try:
                #rect.center = w.hindernisse[0].body.position
                rect.center = s.body.position
                surf = LEVELSURF.subsurface(rect)
                return surf         
        except:
                if s.body.position.x < 500:
                        rect.left = 0
                if s.body.position.y < 400:
                        rect.top = 0
                # zu erweitern    
                surf = LEVELSURF.subsurface(rect)
                return surf


space.add_collision_handler(1,2,post_solve=touch, separate=cänt_touch_dis)
space.gravity = (0, 1900)
clock = pygame.time.Clock()
fps = 25



while True:
        for event in pygame.event.get():
                mousepos = pygame.mouse.get_pos()
                print(mousepos)
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                elif event.type == KEYDOWN:
                        if event.key == K_SPACE:
                                s.jump()
                        if event.key == K_UP:
                                k = Kugel((1500 * s.direction, -100))
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] or keys[K_LEFT]:
                s.move()
       # if keys[K_SPACE]:
          #      s.jump()
        #print(space.collision_handler(1,2))
        LEVELSURF.fill((255, 255, 255))
        w.update()
        for i in kugeln:
                i.update()
        space.step(1/45)
        clock.tick(fps)
        DISPLAYSURF.blit(camera_blit(), (0,0))
        pygame.display.flip()
        #pygame.quit()
        #sys.exit()
