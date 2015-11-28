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
gamename = "The RanD0m RuN"


class Button(pygame.Surface):
    def __init__(self,width,height,xpos,ypos, number_in_menu):
        super().__init__((width,height))
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.number = number_in_menu

        #self.display_surf = None
        self.image_surf = buttonImage.convert()
        self.image_surf = pygame.transform.scale(self.image_surf,(self.width,self.height))

        self.sound = pygame.mixer.Sound('/home/pi/Git/The_Random_Run/GtaVocals/Laugh8.wav')
        
    def clicked(self): # Was tun wenn Button geclickt
        self.sound.play()
        # Evtl. kurz verzögern
        return self.number # Nächster Menübildschirm
        

class Main:
    def __init__(self):
        pygame.init()
        self.running = True
        self.display_surf = pygame.display.set_mode((WINDOWw,WINDOWh))    # ,pygame.FULLSCREEN  für fullscreen (ehem. None)
        self.image_surf = pygame.image.load("startmenu.jpg").convert()# (ehem. None)
        self.image_surf = pygame.transform.scale(self.image_surf,(WINDOWh,WINDOWw))
        
        self.menus = [Menu(gamename),Menu("Singleplayer"),Menu("Multiplayer"),
                          Menu("Highscore"),Menu("Credits"),Menu("Under Construction")] # Test
        self.menu_in_use = self.menus[0] # Startmenu in Benutzung

        #
        #
        #
        #

    def on_execute(self):

        
        pygame.mixer.music.load('tetris.mid')
        pygame.mixer.music.play(-1, 0.0)

        #buttonding
        
        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            #self.on_loop()

            self.on_render()
        self.endIt()

    #Alles, was man interaktiv machen kann
    def on_event(self, event):
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            self.running = False
        elif event.type == MOUSEBUTTONUP:
            (clickX,clickY) = event.pos
            self.mouseclick(clickX,clickY)

    #Rendern eben :)
    def on_render(self):
        self.display_surf.blit(self.image_surf,(0,0))
        for button in self.menu_in_use.buttons: # button des Menüs                                      
            self.display_surf.blit(button.image_surf,(button.xpos,button.ypos))

        title = self.menu_in_use.get_title()
        self.showText(title, textsize = 64)

        self.showText(version,(WINDOWw/2,WINDOWh-50),15) # versionnummer Text
        pygame.display.flip()

    def on_loop(self):
        pass
            
    #Beende Spiel
    def endIt(self):
        pygame.mixer.music.stop()
        pygame.quit()


    def mouseclick(self, clickX, clickY ):
        for button in self.menu_in_use.buttons:
            if ((clickX > button.xpos) & (clickX < (button.xpos+buttonWidth))) & ((clickY > button.ypos) & (clickY < button.ypos+buttonHeight)):
                new_menu = button.clicked()
                self.menu_in_use = self.menus[new_menu]
                return
                
    def showText(self,myString,textpos = (WINDOWw/2, 50), textsize = 32, waitingTime = 0):
        thisPrint = pygame.font.Font('freesansbold.ttf', textsize).render(myString,True,(255,255,255))
        thisRect = thisPrint.get_rect()
        thisRect.center = (textpos)
        self.display_surf.blit(thisPrint,thisRect)
        if(waitingTime != 0):
            pygame.display.update()
            pygame.time.wait(waitingTime)  
        

class Menu:

    def __init__(self,menuname):
        
        self.menuname = menuname
        self.buttons = []

        self.fill_buttons()

    def fill_buttons(self):
        if self.menuname == gamename:
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos, 1))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance, firstButtonYpos, 2))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos + buttonHeight + buttonDistance, 3))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance,
                                                                               firstButtonYpos + buttonHeight + buttonDistance, 4))
        else:
            if self.menuname == "Highscore":
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos,5))
                
            elif self.menuname == "Multiplayer":
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos,5))

            elif self.menuname == "Credits":
                pass
            else:
                pass
                
            self.buttons.append(Button(buttonWidth,int(buttonHeight/2),firstButtonXpos,WINDOWh - 120,0))
    




    #Nur Startmenu render:
    def get_title(self):
        return self.menuname 




    
        
start = Main()
start.on_execute()
