import pygame
from pygame.locals import *

class Button(pygame.Surface):
    def __init__(self,width,height,xpos,ypos):
        super().__init__((width,height))
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos

        self.display_surf = None
        self.image_surf = pygame.image.load("startmenu.jpg").convert()
        self.image_surf = pygame.transform.scale(self.image_surf,(self.width,self.height))

        
        
         


class Startmenu:
    WINDOWh = 800 #window height
    WINDOWw = 800 #window width

    def __init__(self):
        self.running = True
        self.display_surf = None
        self.image_surf = None

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        pygame.mixer.music.load('tetris.mid')
        pygame.mixer.music.play(-1, 0.0)

        singleButton = Button(100,100,300,300)
        
        

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()

            self.on_render()
            singleButton.blit(singleButton.image_surf,
        self.on_cleanup()

    def on_init(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode((self.WINDOWw,self.WINDOWh))    # ,pygame.FULLSCREEN  für fullscreen
        self.running = True
        self.image_surf = pygame.image.load("startmenu.jpg").convert()
        self.image_surf = pygame.transform.scale(self.image_surf,(self.WINDOWh,self.WINDOWw))

    def on_event(self, event):
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            self.running = False

    def on_loop(self):
        pass

    def on_render(self):
        self.display_surf.blit(self.image_surf,(0,0))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.mixer.music.stop()
        pygame.quit()
    
        
start = Startmenu()
start.on_execute()
