import pygame,time, sys, MASTER #Auskommentiert, da sonst direkt ins Spiel eingestiegen wird
from Startmenu_Images import *

from pygame.locals import *

WINDOWw = 800 #window width
WINDOWh = 600 #window height

buttonDistance = 50
buttonWidth = int(WINDOWh/4)
buttonHeight = int(buttonWidth / 2)

firstButtonXpos = WINDOWw/2 - buttonWidth - buttonDistance/2
firstButtonYpos = WINDOWh/3


gamename = "The Random Run"

playername = "Player"

#
'''
Highscores
'''
#

highscore_list = [] # Erster Platz ist die Nummer 0
#Max_size ist so 5?!

default_highscore = [("Mister Man",999),("Mister Man",500),("Mister Man",420),("Mister Man",42),("Mister Man",1)] #  Tupel mit Name und Punkten

highscore_list = default_highscore

def get_Highscore(name,points):
    global highscore_list
    
    list_number = 0
    while(points <= highscore_list[list_number][1]) & (len(highscore_list) >= (list_number-1)):
        list_number += 1
    if list_number < len(highscore_list):
        highscore_list.insert(list_number,(name,points))
        del(highscore_list[len(highscore_list)-1])
        

#
'''
Sounds
'''
#

button_sound = "Sounds/click.wav"

game_start_sound = "Sounds/GtaVocals/Respect.wav"
game_over_sound  = "Sounds/GtaVocals/GameOver.wav"


game_music = 'Sounds/tetris.mid'
menu_music = None

#
'''
Images:
'''
#
#
#
# Images in Startmenu_Images.py!
#
#
#




class Button(pygame.Surface):
    def __init__(self,width,height,xpos,ypos, menutitle):
        super().__init__((width,height))
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.goto_menutitle = menutitle
        
        
        (normal,cursor_on,clicked) = self.get_images()
        
        self.image_surf = normal#.convert() # Aktuelles Bild
        self.image_surf = pygame.transform.scale(self.image_surf,(self.width,self.height))

        self.normal_surf = normal#.convert()
        self.normal_surf = pygame.transform.scale(self.normal_surf,(self.width,self.height))
        
        self.cursor_on_surf = cursor_on#.convert()
        self.cursor_on_surf = pygame.transform.scale(self.cursor_on_surf,(self.width,self.height))
        
        self.clicked_surf = clicked#.convert()
        self.clicked_surf = pygame.transform.scale(self.clicked_surf,(self.width,self.height))
        
    
        self.sound = pygame.mixer.Sound(button_sound)

    def get_images(self):
        #First normal, then cursor over, then clicked
        if self.goto_menutitle == "Singleplayer_screen":# or self.goto_menutitle == "Game_start":
            return singleplayer_button,singleplayer_button_cursor_over,singleplayer_button_clicked
        
        elif self.goto_menutitle == "Multiplayer_screen":
            return multiplayer_button,multiplayer_button_cursor_over,multiplayer_button_clicked
        elif self.goto_menutitle == "Quit_screen":
            return quit_button,quit_button_cursor_over,quit_button_clicked
        elif self.goto_menutitle == "Game_start":
            return ng_button,ng_button_cursor_over,ng_button_clicked
        elif self.goto_menutitle == "Start_screen":
            return back_button,back_button_cursor_over,back_button_clicked
        
        else:
            return (buttonImage,buttonCursorOver,buttonClicked)
            
    
    def clicked(self): # Was tun wenn Button geclickt

        #Spielstart
        
        if(self.goto_menutitle == "Game_start"): # Singleplayer start simple (Beginning)
            pygame.mixer.Sound(game_start_sound).play()
            #game_start_sound.play()
            time.sleep(1)


            #In der Endversion soll das am besten in der Spiel-Datei stehen und nicht hier, zwecks Highscore anzeige
            pygame.mixer.music.load(game_music)
            pygame.mixer.music.play(-1, 0.0)

            survival_time = time.time()
            MASTER.game_run()
            survival_time = int(time.time() - survival_time)

            get_Highscore(playername,survival_time)
                

            pygame.mixer.music.stop()
            
            pygame.mixer.Sound(game_over_sound).play()
            time.sleep(1)
            
            return "Singleplayer_screen"
        
        elif(self.goto_menutitle == "End"):
            pygame.quit()
            sys.exit()
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
        self.image_surf = pygame.image.load(PFAD + background_image).convert()# (ehem. None)
        self.image_surf = pygame.transform.scale(self.image_surf,(WINDOWw,WINDOWh))
        self.menus = {"Start_screen": Menu(gamename),
                      "Singleplayer_screen": Menu("Singleplayer"),
                      "Multiplayer_screen":Menu("Multiplayer"),
                      #"Highscore_screen": Menu("Highscore"), Egal, da Highscore immer neu generiert werden muss
                      "Credits_screen": Menu("Credits"),
                      "NotDone": Menu("Under Construction"),
                      "Game_start": Menu("Singleplayer"),# Spiel starten, danach zurück zum singleplayer menu
                      "Quit_screen": Menu("Quit Confirm"), # Bestätigen des Spielverlassens
                      "End": Menu("End")} # Verlässt das Spiel
            

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
        for button in self.menu_in_use.buttons: # button des Menüs anzeigen                         
            self.display_surf.blit(button.image_surf,(button.xpos,button.ypos))
        for (myString,pos,size) in self.menu_in_use.texts: # Alle Texte anzeigen
            self.showText(myString,pos,size)
        self.showText(self.menu_in_use.menuname, textsize = int(WINDOWh/20)) # Menuname oben anzeigen

        pygame.display.flip()

    def on_loop(self):
        pass
            
    #Beende Spiel
    def endIt(self):
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()


    def mouseclick(self, clickX, clickY, is_clicked = False):
        #Alles was mit der maus abgeglichen werden muss, also Position und Bool über den Klick selbst

        
        for button in self.menu_in_use.buttons: # Test, Zeiger auf Button? Geklickt?
            if ((clickX > button.xpos) & (clickX < (button.xpos+button.width))) & ((clickY > button.ypos) & (clickY < button.ypos+button.height)):
                if is_clicked:
                    button.image_surf = button.clicked_surf#.convert()
                    button.image_surf = pygame.transform.scale(button.image_surf,(button.width,button.height)) # Geklickter Button
                    self.on_render()
                    
                    new_menu = button.clicked()
                    
                    button.image_surf = button.normal_surf#.convert()
                    if new_menu == "Highscore_screen":
                        self.menus 
                        self.menu_in_use = Menu("Highscore")
                    else:
                        self.menu_in_use = self.menus[new_menu]
                else:
                    self.set_back_button_image() # Behebt Bug des Aufgedecktbleibens
                    
                    button.image_surf = button.cursor_on_surf#.convert()
                    self.menu_in_use.curser_over_button = button

                button.image_surf = pygame.transform.scale(button.image_surf,(button.width,button.height))
                return
            else:
                self.set_back_button_image()

    def set_back_button_image(self): # Auslagerung auf Methode, da sonst 2mal der Code verwendet wird (oder auftreten eines Bugs)
        if  self.menu_in_use.curser_over_button != None:
            self.menu_in_use.curser_over_button.image_surf = self.menu_in_use.curser_over_button.normal_surf#.convert()
            self.menu_in_use.curser_over_button.image_surf = pygame.transform.scale(self.menu_in_use.curser_over_button.image_surf,
                                                                                    (self.menu_in_use.curser_over_button.width,self.menu_in_use.curser_over_button.height))
            self.menu_in_use.curser_over_button = None

    
    def showText(self,myString,textpos = (WINDOWw/2, 50), textsize = 26, waitingTime = 0):
        if myString == gamename or myString == "Quit Confirm":
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
        
        self.texts = []# Tripel mit String, Position und Größe 

        self.curser_over_button = None

        self.fill_buttons()

    def fill_buttons(self):
        if self.menuname == gamename:
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos, "Singleplayer_screen"))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance, firstButtonYpos, "Multiplayer_screen"))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos + buttonHeight + buttonDistance, "Highscore_screen"))
            self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance, firstButtonYpos + buttonHeight + buttonDistance, "Credits_screen"))
            
            self.buttons.append(Button(int(buttonWidth/2),buttonHeight,WINDOWw/2-(buttonWidth/2/2),WINDOWh-(int(WINDOWh/4)), "Quit_screen")) # Quit game screen
            
        elif self.menuname == "Quit Confirm":
                self.texts.append(("Are you sure? (Don't do it!)",(WINDOWw/2,WINDOWh/2-100),30))
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos+100, "End"))
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance, firstButtonYpos+100, "Start_screen"))
                                
        else:
            if self.menuname == "Singleplayer":
                self.buttons.append(Button(buttonWidth*2 + buttonDistance,buttonHeight,firstButtonXpos,firstButtonYpos,"Game_start")) # Spielstart
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos,firstButtonYpos+ buttonHeight + buttonDistance,"NotDone"))
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + buttonWidth + buttonDistance,firstButtonYpos+ buttonHeight + buttonDistance,"NotDone"))
            if self.menuname == "Highscore":
                #self.buttons.append(Button(int(buttonWidth/2),buttonHeight,firstButtonXpos,firstButtonYpos,"NotDone"))
                place = 1
                place_y_pos = WINDOWh/2-100
                for (name,points) in highscore_list:

                    if place == 1:
                        textsize = 40
                    else:
                        textsize = 30 - place
                    
                    self.texts.append((str(place) + ".    " + name + ":   " + str(points),(WINDOWw/2,place_y_pos),textsize))
                    place += 1
                    place_y_pos += 50
                

                if highscore_list[0][0] == "Mister Man":
                    self.texts.append(("GOAL: Beat Mister Man!",(WINDOWw/2,place_y_pos+30),30))
                
            elif self.menuname == "Multiplayer":
                self.buttons.append(Button(buttonWidth,buttonHeight*2,firstButtonXpos,firstButtonYpos,"NotDone"))
                self.buttons.append(Button(buttonWidth,buttonHeight*2,firstButtonXpos + buttonWidth + buttonDistance, firstButtonYpos, "Not Done"))

            elif self.menuname == "Credits":
                self.texts.append(("Graphical Design: The Phil",(WINDOWw/2,WINDOWh/2+50),20))
                self.texts.append(("Physiks and mechanics: Tom-Master",(WINDOWw/2,WINDOWh/2),20))
                self.texts.append(("Menu and Multiplayer: General Funky",(WINDOWw/2,WINDOWh/2-50),20))
                self.texts.append(("Supervision and advice: Clemens Schefel",(WINDOWw/2,WINDOWh/2+100),20))

            else:
                pass
                
            self.buttons.append(Button(buttonWidth,int(buttonHeight),firstButtonXpos,WINDOWh - 100,"Start_screen"))
    





    
        
start = Main()
start.on_execute()
