import pygame
from pygame.locals import *

WINDOWh = 800 #window height
WINDOWw = 800 #window width

buttonDistance = 50
buttonWidth = 200
buttonHeight = 100

buttonImage = pygame.image.load("/home/pi/Git/The_Random_Run/Gui/ground.png")
firstButtonXpos = WINDOWw/2 - buttonWidth - buttonDistance/2
firstButtonYpos = WINDOWh/3

version = "Version 0.01"


class Button(pygame.Surface):
    def __init__(self,width,height,xpos,ypos):
        super().__init__((width,height))
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos

        self.display_surf = None
        self.image_surf = buttonImage.convert()
        self.image_surf = pygame.transform.scale(self.image_surf,(self.width,self.height))

        self.sound = pygame.mixer.Sound('/home/pi/Git/The_Random_Run/GtaVocals/GameOver.wav')
        
    def clicked(self): # Was tun wenn Button geclickt
        self.sound.play()

    

        

class Startmenu:
    WINDOWh = WINDOWh
    WINDOWw = WINDOWw

    def __init__(self):
        self.running = True
        self.display_surf = None
        self.image_surf = None
        self.buttons = []

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        pygame.mixer.music.load('tetris.mid')
        pygame.mixer.music.play(-1, 0.0)

        self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos))
        self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance, firstButtonYpos))
        self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos + buttonHeight + buttonDistance))
        self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance,
                                                                           firstButtonYpos + buttonHeight + buttonDistance))
        

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            #self.on_loop()

            self.on_render()
            #singleButton
        self.endIt()

    def on_init(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode((self.WINDOWw,self.WINDOWh))    # ,pygame.FULLSCREEN  für fullscreen
        self.running = True
        self.image_surf = pygame.image.load("startmenu.jpg").convert()
        self.image_surf = pygame.transform.scale(self.image_surf,(self.WINDOWh,self.WINDOWw))

    def on_event(self, event):
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            self.running = False
        elif event.type == MOUSEBUTTONUP:
            (clickX,clickY) = event.pos
            self.mouseclick(clickX,clickY)

    def on_loop(self):
        pass

    def on_render(self):
        self.display_surf.blit(self.image_surf,(0,0))
        for button in self.buttons:
            self.display_surf.blit(button.image_surf,(button.xpos,button.ypos))
        self.showText(version,(WINDOWw/2,WINDOWh-50),15)
        pygame.display.flip()

    def endIt(self):
        pygame.mixer.music.stop()
        pygame.quit()

    def mouseclick(self, clickX, clickY ):
        for button in self.buttons:
            if ((clickX > button.xpos) & clickX < (button.xpos+buttonWidth)) & ((clickY > button.ypos) & (clickY < button.ypos+buttonHeight)):
                button.clicked()
                
    def showText(self,myString,textpos = (50, 50), textsize = 32, waitingTime = 0):
        thisPrint = pygame.font.Font('freesansbold.ttf', textsize).render(myString,True,(255,255,255))
        thisRect = thisPrint.get_rect()
        thisRect.center = (textpos)
        self.display_surf.blit(thisPrint,thisRect)
        if(waitingTime != 0):
            pygame.display.update()
            pygame.time.wait(waitingTime)  
    
        
start = Startmenu()
start.on_execute()
