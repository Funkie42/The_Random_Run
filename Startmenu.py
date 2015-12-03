import pygame,time
import Spieler
from pygame.locals import *

WINDOWh = 600 #window height
WINDOWw = 600 #window width

buttonDistance = 50
buttonWidth = 200
buttonHeight = 100

#Generic Button
buttonImage = pygame.image.load("Gui/Buttons/load_button.png")
buttonCursorOver = pygame.image.load("Gui/Buttons/load_button.png")
buttonClicked = pygame.image.load("Gui/Buttons/load_button.png")

#Singleplayer Button
singleplayer_button = pygame.image.load("Gui/Buttons/red_off.png")
singleplayer_button_cursor_over = pygame.image.load("Gui/Buttons/red_on.png")
singleplayer_button_clicked = pygame.image.load("Gui/Buttons/red_clicked.png")

#Multiplayer Button
multiplayer_button = pygame.image.load("Gui/Buttons/blue_off.png")
multiplayer_button_cursor_over = pygame.image.load("Gui/Buttons/blue_on.png")
multiplayer_button_clicked = pygame.image.load("Gui/Buttons/blue_clicked.png")


firstButtonXpos = WINDOWw/2 - buttonWidth - buttonDistance/2
firstButtonYpos = WINDOWh/3

game_start_sound = pygame.mixer.Sound('GtaVocals/Respect.wav')
game_over_sound = pygame.mixer.Sound('GtaVocals/GameOver.wav')

version = "Version 0.042"
gamename = "The Random Run"


class Button(pygame.Surface):
    def __init__(self,width,height,xpos,ypos, menutitle):
        super().__init__((width,height))
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.goto_menutitle = menutitle
        
        
        #self.display_surf = None

        (normal,cursor_on,clicked) = self.get_images()
        
        self.image_surf = normal.convert()
        self.image_surf = pygame.transform.scale(self.image_surf,(self.width,self.height))

        self.normal_surf = normal.convert()
        self.normal_surf = pygame.transform.scale(self.normal_surf,(self.width,self.height))
        
        self.cursor_on_surf = cursor_on.convert()
        self.cursor_on_surf = pygame.transform.scale(self.cursor_on_surf,(self.width,self.height))
        
        self.clicked_surf = clicked.convert()
        self.clicked_surf = pygame.transform.scale(self.clicked_surf,(self.width,self.height))
        
    
        self.sound = pygame.mixer.Sound('GtaVocals/Laugh7.wav')

    def get_images(self):
        #First normal, then cursor over, then clicked
        if self.goto_menutitle == "Singleplayer_screen" or self.goto_menutitle == "Game_start":
            return singleplayer_button,singleplayer_button_cursor_over,singleplayer_button_clicked
        
        elif self.goto_menutitle == "Multiplayer_screen":
            return multiplayer_button,multiplayer_button_cursor_over,multiplayer_button_clicked
        
        else:
            return (buttonImage,buttonCursorOver,buttonClicked)
            
    
    def clicked(self): # Was tun wenn Button geclickt

        #Spielstart
        
        if(self.goto_menutitle == "Game_start"): # Singleplayer start simple (Beginning)
            game_start_sound.play()
            time.sleep(1)

            pygame.mixer.music.load('tetris.mid')
            pygame.mixer.music.play(-1, 0.0)
            
            Spieler.main()

            pygame.mixer.music.stop()
            
            game_over_sound.play()
            time.sleep(1)
            return "Singleplayer_screen"
        else:
            self.sound.play()
            # Evtl. kurz verzögern
            time.sleep(0.2)
            return self.goto_menutitle # Nächster Menübildschirm
        

class Main:
    def __init__(self):
        pygame.init()
        self.running = True
        self.display_surf = pygame.display.set_mode((WINDOWw,WINDOWh))    # ,pygame.FULLSCREEN  für fullscreen (ehem. None)
        self.image_surf = pygame.image.load("Gui/background.png").convert()# (ehem. None)
        self.image_surf = pygame.transform.scale(self.image_surf,(WINDOWw,WINDOWh))
        self.menus = {"Start_screen": Menu(gamename),
                      "Singleplayer_screen": Menu("Singleplayer"),
                      "Multiplayer_screen":Menu("Multiplayer"),
                      "Highscore_screen": Menu("Highscore"),
                      "Credits_screen": Menu("Credits"),
                      "NotDone": Menu("Under Construction"),
                      "Game_start": Menu("Singleplayer")} # Spiel starten, danach zurück zum singleplayer menu
        #self.menus = [Menu(gamename),Menu("Singleplayer"),Menu("Multiplayer"),
        #                  Menu("Highscore"),Menu("Credits"),Menu("Under Construction")] # Test
        self.menu_in_use = self.menus["Start_screen"] # Startmenu in Benutzung


    def on_execute(self):
        
        #pygame.mixer.music.load("/media/8C48-C703/sandman1.wav")
        # pygame.mixer.music.play(-1, 0.0)
        # musik

        
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

        self.showText(self.menu_in_use.menuname, textsize = 56) # Menuname oben anzeigen

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
                    button.image_surf = button.clicked_surf.convert()
                    button.image_surf = pygame.transform.scale(button.image_surf,(button.width,button.height)) # Geklickter Button
                    self.on_render()
                    
                    new_menu = button.clicked()
                    
                    button.image_surf = button.normal_surf.convert()
                    self.menu_in_use = self.menus[new_menu]
                else:
                    self.set_back_button_image() # Behebt Bug des Aufgedecktbleibens
                    
                    button.image_surf = button.cursor_on_surf.convert()
                    self.menu_in_use.curser_over_button = button

                button.image_surf = pygame.transform.scale(button.image_surf,(button.width,button.height))
                return
            else:
                self.set_back_button_image()

    def set_back_button_image(self): # Auslagerung auf Methode, da sonst 2mal der Code verwendet wird (oder auftreten eines Bugs)
        if  self.menu_in_use.curser_over_button != None:
            self.menu_in_use.curser_over_button.image_surf = self.menu_in_use.curser_over_button.normal_surf.convert()
            self.menu_in_use.curser_over_button.image_surf = pygame.transform.scale(self.menu_in_use.curser_over_button.image_surf,
                                                                                    (self.menu_in_use.curser_over_button.width,self.menu_in_use.curser_over_button.height))
            self.menu_in_use.curser_over_button = None

    
    def showText(self,myString,textpos = (WINDOWw/2, 50), textsize = 26, waitingTime = 0):
        if myString == gamename:
            pass
        else:
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
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos, "Singleplayer_screen"))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance, firstButtonYpos, "Multiplayer_screen"))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos + buttonHeight + buttonDistance, "Highscore_screen"))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance,
                                                                               firstButtonYpos + buttonHeight + buttonDistance, "Credits_screen"))
        else:
            if self.menuname == "Singleplayer":
                self.buttons.append(Button(buttonWidth*2 + buttonDistance,buttonHeight,firstButtonXpos,firstButtonYpos,"Game_start")) # Spielstart
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos+ buttonHeight + buttonDistance,"NotDone"))
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance,firstButtonYpos+ buttonHeight + buttonDistance,"NotDone"))
            if self.menuname == "Highscore":
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos,"NotDone"))
                
            elif self.menuname == "Multiplayer":
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos,"NotDone"))

            elif self.menuname == "Credits":
                pass
            else:
                pass
                
            self.buttons.append(Button(buttonWidth,int(buttonHeight/2),firstButtonXpos,WINDOWh - 120,"Start_screen"))
    





    
        
start = Main()
start.on_execute()
