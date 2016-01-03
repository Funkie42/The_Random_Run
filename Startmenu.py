import pygame,time, sys, MASTER
from Startmenu_Images import *

from pygame.locals import *

import MASTERmulit,Gameclient,Gameserver


WINDOWw = 800 #window width
WINDOWh = 600 #window height

buttonDistance = 50
buttonWidth = int(WINDOWh/4)
buttonHeight = int(buttonWidth / 2)

firstButtonXpos = WINDOWw/2 - buttonWidth - buttonDistance/2
firstButtonYpos = WINDOWh/3


load_surf = ((buttonWidth*2,buttonHeight*2),
             (int(WINDOWw/2) - buttonWidth,int(WINDOWh/2) -  buttonHeight))
# Loading Surf while connecting in Multiplayer

gamename = "The Random Run"
playername = "Player"

# For Mulitplayer

server_ip = "localhost"
client_ip = "localhost"
port = 42042

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

game_start_sound = None



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
        #self.gameover_sound = pygame.mixer.Sound("Sounds/GtaVocals/Respect.wav")

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
            
    
    
class Main:
    def __init__(self):
        pygame.init()
        self.running = True
        self.display_surf = pygame.display.set_mode((WINDOWw,WINDOWh))#,RESIZABLE)    # ,pygame.FULLSCREEN  für fullscreen (ehem. None)
        self.image_surf = pygame.image.load(PFAD + background_image).convert()# (ehem. None)
        self.image_surf = pygame.transform.scale(self.image_surf,(WINDOWw,WINDOWh))
        self.menus = {"Start_screen": Menu(gamename,"Start_screen"),
                      "Singleplayer_screen": Menu("Singleplayer","Singleplayer_screen"),
                      "Multiplayer_screen":Menu("Multiplayer", "Multiplayer_screen"),
                      #"Highscore_screen": Menu("Highscore"), Egal, da Highscore immer neu generiert werden muss
                      "Credits_screen": Menu("Credits", "Credits_screen"),
                      "NotDone": Menu("Under Construction","NotDone"),
                      "Game_start": Menu("Singleplayer","Game_start"),# Spiel starten, danach zurück zum singleplayer menu
                      "Quit_screen": Menu("Quit Confirm","Quit_screen"), # Bestätigen des Spielverlassens
                      "End": Menu("End","End"),# Verlässt das Spiel
                      "Open_Multi_screen": Menu ("Open TCP-Server","Open_Multi_screen"),
                      "Link_In_screen": Menu("Enter Multiplayergame","Link_In_screen"),
                      "Open_game":Menu("Open_game","Open_game"),
                      "Awaiting_Player_screen": Menu("Awaiting second player","Awaiting_Player_screen")} 
            

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
        
        elif (self.menu_in_use.write_text_config != None) & (event.type == KEYDOWN):
            if event.key == K_RETURN:
                if self.menu_in_use.writeable_text != "":
                    pass # TODO
            elif event.key == K_BACKSPACE:
                if len(self.menu_in_use.writeable_text) > 0:
                    self.menu_in_use.writeable_text = self.menu_in_use.writeable_text[:-1]
            else:
                if len(self.menu_in_use.writeable_text) < 19: # Maxlänge, damit es nicht aus der Box kommt
                    try: self.menu_in_use.writeable_text += str(event.unicode)
                    except: pass

    #Rendern eben :)
    def on_render(self):
        self.display_surf.blit(self.image_surf,(0,0))
        
        for surface in self.menu_in_use.surfaces: # Alle anderen Oberflächen
            image = pygame.transform.scale(searchbar_image, surface[0])
            self.display_surf.blit(image,surface[1])
            
        for button in self.menu_in_use.buttons: # button des Menüs anzeigen                         
            self.display_surf.blit(button.image_surf,(button.xpos,button.ypos))
            
        for (myString,pos,size) in self.menu_in_use.texts: # Alle Texte anzeigen
            self.showText(myString,pos,size)
            
        self.showText(self.menu_in_use.menuname, textsize = int(WINDOWh/20)) # Menuname oben anzeigen
        
        if self.menu_in_use.write_text_config != None: # Für Texteingaben im Spiel
            text,pos,size,writey = self.menu_in_use.write_text_config
            text = self.menu_in_use.writeable_text
            self.showText(text,pos,size, writeable = True)

        #Flip it!    
        pygame.display.flip()
            
    #Beende Spiel
    def endIt(self):
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()

    def button_clicked(self,button): # Was tun wenn Button geclickt
        global server_IP

        #######################################
        #Spielstart Singleplayer
        #######################################
        
        if(button.goto_menutitle == "Game_start"): # Singleplayer start simple (Beginning)
          #  pygame.mixer.Sound(game_start_sound).play()
            #game_start_sound.play()
            time.sleep(1)


            #In der Endversion soll das am besten in der Spiel-Datei stehen und nicht hier, zwecks Highscore anzeige
            pygame.mixer.music.load(game_music)
            pygame.mixer.music.play(-1, 0.0)

            survival_time = time.time()
            try:MASTER.main()
            except: print("The Game crashed for some reason.... try again! :)")
            finally:
                survival_time = int(time.time() - survival_time)

                get_Highscore(playername,survival_time)
                    

                pygame.mixer.music.stop()
                
                #self.game_over_sound.play()
                time.sleep(1)
                
                return "Singleplayer_screen"
        #########################
        #Ende Spiel
        #########################
        
        elif(button.goto_menutitle == "End"):
            pygame.quit()
            sys.exit()

        ###############################
        # Multiplayer Open Game
        ###############################

        elif(button.goto_menutitle == "Open_game"):
            try:
                server = Gameserver.ServerGame()
                server.connect(server_ip,port)

                server.accepting_allow() ###############

                client_ip = server_ip

                Gameclient.create_Client(port,client_ip)

                image = pygame.transform.scale(searchbar_image, load_surf[0])
                self.display_surf.blit(image,load_surf[1])
                self.showText("Starting Game",(int(WINDOWw/2),int(WINDOWh/2)),30)
                pygame.display.flip()

                time.sleep(2)
                
                MASTERmulit.start_up() #Start Game!
             
                Gameclient.client.disconnect()
                server.disconnect_clients()
                server.disconnect()    
            except:
                image = pygame.transform.scale(searchbar_image, load_surf[0])
                self.display_surf.blit(image,load_surf[1])
                self.showText("Something went wrong...",(int(WINDOWw/2),int(WINDOWh/2)),30)
                pygame.display.flip()

                time.sleep(2)
            return "Open_Multi_screen"



            
        
        ###############################
        #Mulitplayer Link in
        ###############################
        elif(button.goto_menutitle == "Search"):
            client_ip = self.menu_in_use.writeable_text

            image = pygame.transform.scale(searchbar_image, load_surf[0])

            connection_text = "Connecting"
            for dot in " ...":
                connection_text += dot
                self.display_surf.blit(image,load_surf[1])
                self.showText(connection_text,(int(WINDOWw/2),int(WINDOWh/2)),30)
                pygame.display.flip()
                time.sleep(0.5)
            #####
            #Multiplayer client aufrufen
            try:  
                Gameclient.create_Client(port,client_ip)

                image = pygame.transform.scale(searchbar_image, load_surf[0])
                self.display_surf.blit(image,load_surf[1])
                self.showText("Starting Game",(int(WINDOWw/2),int(WINDOWh/2)),30)
                pygame.display.flip()

                time.sleep(2)
                
                MASTERmulit.start_up() #Start Game!
             
                Gameclient.client.disconnect()
            except:
                image = pygame.transform.scale(searchbar_image, load_surf[0])
                self.display_surf.blit(image,load_surf[1])
                self.showText("Connection Failed",(int(WINDOWw/2),int(WINDOWh/2)),30)
                pygame.display.flip()
                Gameclient.client.disconnect()
                time.sleep(2)
                
            return self.menu_in_use.key_name

        ####################
        #Anderes Menu
        ####################
            
        else:
            button.sound.play()
            time.sleep(0.2)
            return button.goto_menutitle # Nächster Menübildschirm
        



    def mouseclick(self, clickX, clickY, is_clicked = False):
        #Alles was mit der maus abgeglichen werden muss, also Position und Bool über den Klick selbst

        
        for button in self.menu_in_use.buttons: # Test, Zeiger auf Button? Geklickt?
            if ((clickX > button.xpos) & (clickX < (button.xpos+button.width))) & ((clickY > button.ypos) & (clickY < button.ypos+button.height)):
                if is_clicked:
                    button.image_surf = button.clicked_surf#.convert()
                    button.image_surf = pygame.transform.scale(button.image_surf,(button.width,button.height)) # Geklickter Button
                    self.on_render()
                    
                    new_menu = self.button_clicked(button)
                    
                    button.image_surf = button.normal_surf#.convert()
                    if new_menu == "Highscore_screen":
                        self.menu_in_use = Menu("Highscore","Highscore_screen")
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

    
    def showText(self,myString,textpos = (WINDOWw/2, 50), textsize = 26, waitingTime = 0, writeable = False):
        if myString == gamename or myString == "Quit Confirm":
            pass
        else:
            thisPrint = pygame.font.Font('freesansbold.ttf', textsize).render(myString,True,(255,255,255))
            thisRect = thisPrint.get_rect()
            if writeable:
                thisRect.x, thisRect.y = textpos
            else:
                thisRect.center = (textpos)
                
            self.display_surf.blit(thisPrint,thisRect)
                
            if(waitingTime != 0):
                pygame.display.update()
                pygame.time.wait(waitingTime)  
        

class Menu:

    def __init__(self,menuname, key_name):
        
        self.menuname = menuname
        self.key_name = key_name
        
        self.buttons = []
        self.surfaces = []  #2er Tupel von 2er Tupeln mit (Breite,Höhe) und (Xpos,Ypos)
        self.texts = []# Tripel mit String, Position und Größe
        self.write_text_config = None # 4er Tupel mit String, Position, Größe und Writeable auf True        
        self.writeable_text = ""

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
                self.buttons.append(Button(buttonWidth,buttonHeight*2,firstButtonXpos,firstButtonYpos,"Open_Multi_screen"))
                self.buttons.append(Button(buttonWidth,buttonHeight*2,firstButtonXpos + buttonWidth + buttonDistance, firstButtonYpos, "Link_In_screen"))

            elif self.menuname == "Credits":
                self.texts.append(("Graphical Design: The Phil",(WINDOWw/2,WINDOWh/2+50),20))
                self.texts.append(("Physiks and mechanics: Tom-Master",(WINDOWw/2,WINDOWh/2),20))
                self.texts.append(("Menu and Multiplayer: General Funky",(WINDOWw/2,WINDOWh/2-50),20))
                self.texts.append(("Supervision and advice: Clemens Schefel",(WINDOWw/2,WINDOWh/2+100),20))

            elif self.menuname == "Open TCP-Server": 
                self.buttons.append(Button(buttonWidth,buttonHeight*2,firstButtonXpos,firstButtonYpos,"Open_game"))
                self.buttons.append(Button(buttonWidth,buttonHeight*2,firstButtonXpos + buttonWidth + buttonDistance, firstButtonYpos,"Awaiting_Player_screen"))

            elif self.menuname == "Enter Multiplayergame":
                self.surfaces.append( (   (buttonWidth*2 + buttonDistance,buttonHeight), (firstButtonXpos,firstButtonYpos)  ) )
                self.texts.append(("IP-Address: ",(firstButtonXpos+ int(buttonWidth/2),firstButtonYpos + int(buttonHeight/2)),20))
                self.write_text_config = (( "192.168.178.",(firstButtonXpos+140,firstButtonYpos + 25),22,True))
                self.writeable_text =  "192.168.178."
                self.buttons.append(Button(buttonWidth*2 + buttonDistance,buttonHeight,firstButtonXpos,firstButtonYpos + buttonDistance*2,"Search"))

            elif self.menuname == "Awaiting second player":
                self.texts.append(("Let a friend join in to start the randomness!",(WINDOWw/2,WINDOWh/2-50),30))
                self.texts.append(("(If you have one...)",(WINDOWw/2,WINDOWh/2-25),10))
                

            else:
                pass
                
            self.buttons.append(Button(buttonWidth,int(buttonHeight),firstButtonXpos,WINDOWh - 100,"Start_screen"))
    





    
if __name__ == "__main__":        
    start = Main()
    start.on_execute()
