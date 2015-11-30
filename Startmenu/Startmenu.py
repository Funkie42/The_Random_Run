import pygame,time
import Spieler
from pygame.locals import *

WINDOWh = 800 #window height
WINDOWw = 800 #window width

buttonDistance = 50
buttonWidth = 200
buttonHeight = 100

buttonImage = pygame.image.load("/home/pi/Git/The_Random_Run/Gui/ground.png")
buttonClicked = pygame.image.load("/home/pi/Git/The_Random_Run/Gui/man2.png")
buttonCursorOver = pygame.image.load("/home/pi/Git/The_Random_Run/Gui/man1.png") #Testzweck

firstButtonXpos = WINDOWw/2 - buttonWidth - buttonDistance/2
firstButtonYpos = WINDOWh/3

game_start_sound = pygame.mixer.Sound('/home/pi/Desktop/The_Random_Run/GtaVocals/Respect.wav')
game_over_sound = pygame.mixer.Sound('/home/pi/Desktop/The_Random_Run/GtaVocals/GameOver.wav')

version = "Version 0.027"
gamename = "The Random Run"


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
    
        self.sound = pygame.mixer.Sound('/home/pi/Git/The_Random_Run/GtaVocals/Laugh7.wav')
        
    def clicked(self): # Was tun wenn Button geclickt

        if(self.number == -1): # Singleplayer start simple (Beginning)
            game_start_sound.play()
            time.sleep(1)
            Spieler.main()
            game_over_sound.play()
            time.sleep(1)
            return 1
        else:
            self.sound.play()
            # Evtl. kurz verzögern
            time.sleep(0.2)
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


    def on_execute(self):
        
        pygame.mixer.music.load('tetris.mid')
        pygame.mixer.music.play(-1, 0.0)
        
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
        elif event.type == MOUSEMOTION: # Mausposition
            (mousex,mousey) = event.pos
            self.mouseclick(mousex,mousey)
        elif event.type == MOUSEBUTTONUP: # Click-Ort
            (clickX,clickY) = event.pos
            self.mouseclick(clickX,clickY,True)

    #Rendern eben :)
    def on_render(self):
        self.display_surf.blit(self.image_surf,(0,0))
        for button in self.menu_in_use.buttons: # button des Menüs                                      
            self.display_surf.blit(button.image_surf,(button.xpos,button.ypos))

        self.showText(self.menu_in_use.menuname, textsize = 64) # Menuname oben anzeigen

        self.showText(version,(WINDOWw/2,WINDOWh-50),15) # versionnummer Text
        pygame.display.flip()

    def on_loop(self):
        pass
            
    #Beende Spiel
    def endIt(self):
        pygame.mixer.music.stop()
        pygame.quit()


    def mouseclick(self, clickX, clickY, is_clicked = False):
        for button in self.menu_in_use.buttons:
            if ((clickX > button.xpos) & (clickX < (button.xpos+button.width))) & ((clickY > button.ypos) & (clickY < button.ypos+button.height)):
                if is_clicked:
                    button.image_surf = buttonClicked.convert()
                    button.image_surf = pygame.transform.scale(button.image_surf,(button.width,button.height)) # Geklickter Button
                    self.on_render()
                    
                    new_menu = button.clicked()
                    
                    button.image_surf = buttonImage.convert()
                    self.menu_in_use = self.menus[new_menu]
                else:
                    self.set_back_button_image() # Behebt Bug des Aufgedecktbleibens
                    
                    button.image_surf = buttonCursorOver.convert()
                    self.menu_in_use.curser_over_button = button

                button.image_surf = pygame.transform.scale(button.image_surf,(button.width,button.height))
                return
            else:
                self.set_back_button_image()

    def set_back_button_image(self): # Auslagerung auf Methode, da sonst 2mal der Code verwendet wird (oder auftreten eines Bugs)
        if  self.menu_in_use.curser_over_button != None:
            self.menu_in_use.curser_over_button.image_surf = buttonImage.convert()
            self.menu_in_use.curser_over_button.image_surf = pygame.transform.scale(self.menu_in_use.curser_over_button.image_surf,
                                                                                    (self.menu_in_use.curser_over_button.width,self.menu_in_use.curser_over_button.height))
            self.menu_in_use.curser_over_button = None

    
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

        self.curser_over_button = None

        self.fill_buttons()

    def fill_buttons(self):
        if self.menuname == gamename:
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos, 1))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance, firstButtonYpos, 2))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos + buttonHeight + buttonDistance, 3))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance,
                                                                               firstButtonYpos + buttonHeight + buttonDistance, 4))
        else:
            if self.menuname == "Singleplayer":
                self.buttons.append(Button(buttonWidth*2 + buttonDistance,buttonHeight,firstButtonXpos,firstButtonYpos,-1)) # Spielstart
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos+ buttonHeight + buttonDistance,5))
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance,firstButtonYpos+ buttonHeight + buttonDistance,5))
            if self.menuname == "Highscore":
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos,5))
                
            elif self.menuname == "Multiplayer":
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos,5))

            elif self.menuname == "Credits":
                pass
            else:
                pass
                
            self.buttons.append(Button(buttonWidth,int(buttonHeight/2),firstButtonXpos,WINDOWh - 120,0))
    





    
        
start = Main()
start.on_execute()
