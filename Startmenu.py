import pygame,time, sys, MASTER, Gameclient,Gameserver,Texts, random#MASTERmulit,
import fileinput # Für Highscore
from Startmenu_Images import *
from pygame.locals import *

###############    Automatisches Erkennen der eigenen IP-Adresse   #############
# Wenn es fehlschlägt (Kein Internet etc.) kann nur am selben Computer gespielt werden #
import socket
try:ip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
except:
    ip = 'localhost'
    print = ('No Networt Connection')
            

server_ip = ip
client_ip = ip
port = 42042

gamename = "The Random Run"
playername = "Player"

WINDOWw = 800 #window width
WINDOWh = 600 #window height

buttonDistance = 50
buttonWidth = int(WINDOWh/4)
buttonHeight = int(buttonWidth / 2)

firstButtonXpos = WINDOWw/2 - buttonWidth - buttonDistance/2
firstButtonYpos = WINDOWh/3







#
'''
Highscores
'''
#



highscore_list = [] # Erster Platz ist die Nummer 0
#Max_size ist so 5?!


test = []
with open('Highscore.txt','r') as f:
    for line in f:
        if line[-1] == "\n"[-1]:
            line = line[:-1]
        test.append(line)
for i in range(0,len(test)):
    if i % 2 == 0:
        highscore_list.append((test[i],test[i+1]))
    
    

def get_Highscore(name,points):
    global highscore_list
    try:
        list_number = 0
        while (len(highscore_list) > list_number) & (points <= int(highscore_list[list_number][1])):
            list_number += 1
        if list_number < len(highscore_list):
            highscore_list.insert(list_number,(name,points))
            del(highscore_list[len(highscore_list)-1])
        with open('Highscore.txt','w') as file:
            for entry in highscore_list:
                file.write(entry[0] + "\n")
                file.write(str(entry[1]) + "\n")
    except: pass

def reset_Highscore():
    global highscore_list
    highscore_list = [("Mister Man",999),("Mister Man",500),("Mister Man",420),("Mister Man",42),("Mister Man",1)]#  Tupel mit Name und Punkten
    with open('Highscore.txt','w') as file:
        for entry in highscore_list:
            file.write(entry[0] + "\n")
            file.write(str(entry[1]) + "\n")
            
            
    
    

#
'''
Sounds
'''
#

button_sound = "Sounds/click.wav"

game_start_sound = None
star_wars_sound = "Sounds/Startwars_intro.ogg"


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
    '''##################################################################
    Klasse der Knöpfe im Startmenu
    - __init__(Breite, Höhe, X-Position, Y-Position, Key des Menüs, zu dem der Button führt)
            Erstellt einen Button mit gesetzter Breite und Höhe an der (X,Y)-Position der zum genannten Menü führt
    - get_images()
            Nimmt die drei Bilder eines Buttons und weist sie anhand des Menü-Keys zu
            (Normale Button, Button mit der Maus auf dem Button, Geklickter Button)
    ##################################################################'''
    def __init__(self,width,height,xpos,ypos, menutitle):
        super().__init__((width,height))
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.goto_menutitle = menutitle
        
        #### Initiazing Images ####
        (normal,cursor_on,clicked) = self.get_images()

        self.normal_surf = pygame.transform.scale(normal,(self.width,self.height))
        self.cursor_on_surf = pygame.transform.scale(cursor_on,(self.width,self.height))
        self.clicked_surf = pygame.transform.scale(clicked,(self.width,self.height))

        self.image_surf = self.normal_surf # Aktuelles Bild
        

    
        self.sound = pygame.mixer.Sound(button_sound)
        #self.gameover_sound = pygame.mixer.Sound("Sounds/GtaVocals/Respect.wav")

    def get_images(self):
        
    #####################
    #Startmenu Buttons
    #####################
            
        if self.goto_menutitle == "Singleplayer_screen":# or self.goto_menutitle == "Game_start":
            return singleplayer_button,singleplayer_button_cursor_over,singleplayer_button_clicked
        elif self.goto_menutitle == "Multiplayer_screen":
            return multiplayer_button,multiplayer_button_cursor_over,multiplayer_button_clicked
        elif self.goto_menutitle == "Quit_screen":
            return quit_button,quit_button_cursor_over,quit_button_clicked
        elif self.goto_menutitle == "Credits_screen":
            return credits_button,credits_button_cursor_over,credits_button_clicked
        elif self.goto_menutitle == "Highscore_screen":
            return highscore_button,highscore_button_cursor_over, highscore_button_clicked
        elif self.goto_menutitle == "Reset_highscore":
            return reset_button,reset_button_cursor_over,reset_button_clicked

    #####################
    #Singleplayer Menu
    #####################
            
        elif self.goto_menutitle == "Game_start":
            return ng_button,ng_button_cursor_over,ng_button_clicked
        elif self.goto_menutitle == "Choose_lvl_screen":
            return choose_lvl_button,choose_lvl_button_cursor_over,choose_lvl_button_clicked
        elif self.goto_menutitle == "NotDone": # TODO
            return load_button,load_button_cursor_over,load_button_clicked

    ######################
    #End Game Menu
    ######################
        
        elif self.goto_menutitle == "End":
            return yes_button,yes_button_cursor_over,yes_button_clicked

    ######################
    #Multiplayer Menu
    ######################
    
        elif self.goto_menutitle == "Link_In_screen":
            return link_in_button,link_in_button_cursor_over,link_in_button_clicked
        elif self.goto_menutitle == "Search":
            return search_button,search_button_cursor_over,search_button_clicked
        elif self.goto_menutitle == "Open_Multi_screen":
            return open_screen_button,open_screen_button_cursor_over,open_screen_button_clicked
        elif self.goto_menutitle == "Open_game": # Multiplayer normales Spiel
            return host_normal_button,host_normal_button_cursor_over,host_normal_button_clicked
        elif self.goto_menutitle == "Awaiting_Player_screen": # Multiplayer normales Spiel
            return host_minigame_button,host_minigame_button_cursor_over,host_minigame_button_clicked        

    ##############
    ##Other
    ##############
        
        if self.goto_menutitle == "Start_screen":# or self.goto_menutitle == "Game_start":
            return back_button,back_button_cursor_over,back_button_clicked
        else:
            return (buttonImage,buttonCursorOver,buttonClicked)
            
class Menu:
    '''##################################################################

    ##################################################################'''
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
                self.buttons.append(Button(buttonWidth*2,buttonHeight,firstButtonXpos + buttonDistance,firstButtonYpos - int(buttonDistance/2),"Game_start")) # Spielstart
                self.buttons.append(Button(buttonWidth*2,buttonHeight,firstButtonXpos + buttonDistance, firstButtonYpos +buttonHeight+ int(buttonDistance/2) - int(buttonDistance/2),"Choose_lvl_screen"))
                self.buttons.append(Button(buttonWidth*2,buttonHeight,firstButtonXpos + buttonDistance, firstButtonYpos +2*(buttonHeight+ int(buttonDistance/2)) - int(buttonDistance/2),"NotDone"))

            if self.menuname == "Choose Level":
                self.buttons.append(Button(buttonWidth,buttonHeight,firstButtonXpos + int((buttonWidth + buttonDistance)/2),firstButtonYpos+ buttonHeight*2,"Load_single_game"))
                self.surfaces.append( (   (buttonWidth*2 + buttonDistance,buttonHeight), (firstButtonXpos,firstButtonYpos)  ) )
                self.texts.append(("Enter Levelcode: ",(firstButtonXpos+ int(buttonWidth/2+15),firstButtonYpos + int(buttonHeight/2)),20))
                self.write_text_config = (( "",(firstButtonXpos+175,firstButtonYpos + 25),22,True))
                ######### TODO #############
            
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
                
                self.buttons.append(Button(int(buttonWidth/2),int(buttonHeight/2),WINDOWw -320,WINDOWh - 182,"Reset_highscore"))
                
                if highscore_list[0][0] == "Mister Man":
                    self.texts.append(("GOAL: Beat Mister Man!",(WINDOWw/2,place_y_pos+30),30))
                    
                
            elif self.menuname == "Multiplayer":
                self.buttons.append(Button(buttonWidth*2 + buttonDistance,buttonHeight,firstButtonXpos,firstButtonYpos,"Open_Multi_screen"))
                self.buttons.append(Button(buttonWidth*2 + buttonDistance,buttonHeight,firstButtonXpos, firstButtonYpos +buttonHeight+ int(buttonDistance/2), "Link_In_screen"))

            elif self.menuname == "Credits":
                self.texts.append(("Graphical Design: The Phil",(WINDOWw/2,WINDOWh/2+50),20))
                self.texts.append(("Physiks and mechanics: Tom-Master",(WINDOWw/2,WINDOWh/2),20))
                self.texts.append(("Menu and Multiplayer: General Funky",(WINDOWw/2,WINDOWh/2-50),20))
                self.texts.append(("Supervision and advice: Clemens Schefel",(WINDOWw/2,WINDOWh/2+100),20))

            elif self.menuname == "Open TCP-Server": 
                self.buttons.append(Button(buttonWidth*2 + buttonDistance,buttonHeight,firstButtonXpos,firstButtonYpos,"Open_game"))
                self.buttons.append(Button(buttonWidth*2 + buttonDistance,buttonHeight,firstButtonXpos, firstButtonYpos +buttonHeight+ int(buttonDistance/2),"Awaiting_Player_screen"))

            elif self.menuname == "Enter Multiplayergame":
                self.surfaces.append( (   (buttonWidth*2 + buttonDistance,buttonHeight), (firstButtonXpos,firstButtonYpos)  ) )
                self.texts.append(("IP-Address: ",(firstButtonXpos+ int(buttonWidth/2),firstButtonYpos + int(buttonHeight/2)),20))
                self.write_text_config = (( ip,(firstButtonXpos+140,firstButtonYpos + 25),22,True))
                self.writeable_text =  ip
                self.buttons.append(Button(buttonWidth*2 + buttonDistance,buttonHeight,firstButtonXpos,firstButtonYpos + buttonDistance*2,"Search"))

            elif self.menuname == "Awaiting second player":
                self.texts.append(("Let a friend join in to start the randomness!",(WINDOWw/2,WINDOWh/2-50),30))
                self.texts.append(("(If you have one...)",(WINDOWw/2,WINDOWh/2-25),10))

            else:
                pass
                
            self.buttons.append(Button(buttonWidth,int(buttonHeight),firstButtonXpos,WINDOWh - 100,"Start_screen"))
    
    
    
class Main:
    '''##################################################################

    ##################################################################'''
    def __init__(self):
        pygame.init()
        self.running = True
        self.display_surf = pygame.display.set_mode((WINDOWw,WINDOWh))#,RESIZABLE)
        self.image_surf = pygame.image.load(PFAD + background_image).convert()
        self.image_surf = pygame.transform.scale(self.image_surf,(WINDOWw,WINDOWh))

        self.menus = {"Start_screen": Menu(gamename,"Start_screen"),
                      "Singleplayer_screen": Menu("Singleplayer","Singleplayer_screen"),
                      "Choose_lvl_screen": Menu("Choose Level","Choose_lvl_screen"),
                      "Multiplayer_screen":Menu("Multiplayer", "Multiplayer_screen"),
                      #"Highscore_screen": Menu("Highscore"), Egal, da Highscore immer neu generiert werden muss
                      "Credits_screen": Menu("Credits", "Credits_screen"),
                      "NotDone": Menu("Under Construction","NotDone"),
                      "Game_start": Menu("Singleplayer","Game_start"),# Spiel starten, danach zurück zum singleplayer menu
                      "Quit_screen": Menu("Quit Confirm","Quit_screen"), # Bestätigen des Spielverlassens
                      "End": Menu("End","End"),# Verlässt das Spiel
                      "Open_Multi_screen": Menu ("Open TCP-Server","Open_Multi_screen"),
                      "Link_In_screen": Menu("Enter Multiplayergame","Link_In_screen"),
                      "Open_game":Menu("Open_game","Open_game"), # Öffnet Multiplayerspiel
                      "Awaiting_Player_screen": Menu("Awaiting second player","Awaiting_Player_screen")} 

        self.menu_in_use = self.menus["Start_screen"] # Startmenu in Benutzung


    def on_execute(self):
        
        #pygame.mixer.music.load("/media/8C48-C703/sandman1.wav")
        # pygame.mixer.music.play(-1, 0.0)
        # musik    
        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
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
                if (self.menu_in_use.writeable_text != "") & (self.menu_in_use == self.menus["Link_In_screen"]):
                    self.button_clicked(Button(1,1,1,1,"Search"))
            elif event.key == K_BACKSPACE:
                if len(self.menu_in_use.writeable_text) > 0:
                    self.menu_in_use.writeable_text = self.menu_in_use.writeable_text[:-1]
            else:
                if len(self.menu_in_use.writeable_text) < 18: # Maxlänge, damit es nicht aus der Box kommt
                    try: self.menu_in_use.writeable_text += str(event.unicode)
                    except: pass


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

        pygame.display.flip()
            
    #Beende Spiel
    def endIt(self):
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()

    def button_clicked(self,button): # Was tun wenn Button geclickt
        global server_IP

        #####################################################################################################################################################
        #Spielstart Singleplayer
        #####################################################################################################################################################
        
        if(button.goto_menutitle == "Game_start"): # Singleplayer start simple (Beginning)
          #  pygame.mixer.Sound(game_start_sound).play()
            #game_start_sound.play()
                time.sleep(1)
                
                self.interlevel_scene(0)
                score_info = MASTER.on_execute(False) # (Continue Bool, Punktzahl, bonustime)
                finished_level_number = 1
                continue_game = score_info[0]
                while continue_game:
                    self.level_finished(score_info,finished_level_number)
                    self.interlevel_scene(finished_level_number)
                    finished_level_number += 1
                    score_info = MASTER.main()
                    continue_game = score_info[0]

                    
                highscore = score_info[1] + score_info[2]
                get_Highscore(playername,highscore)

                self.display_surf.fill((0,0,0))
                self.blend_in_text("Congratulations!",(int(WINDOWw/2),int(WINDOWh/2)),30,(buttonWidth*2,buttonHeight*2))
                time.sleep(1)
                self.blend_in_text("You finished..",(int(WINDOWw/2),int(WINDOWh/2)),30,(buttonWidth*2,buttonHeight*2))
                time.sleep(1)
                self.blend_in_text("The Random Run!",(int(WINDOWw/2),int(WINDOWh/2)),30,(buttonWidth*2,buttonHeight*2))
                time.sleep(3)
                
                return "Credits_screen"            

        ###############################
        # Multiplayer Open Game
        ###############################

        elif(button.goto_menutitle == "Open_game"):
            #try:
                server = Gameserver.ServerGame()
                server.connect(server_ip,port)
                server.accepting_allow() ###############
                client_ip = server_ip
                Gameclient.create_Client(port,client_ip)

                self.blend_in_text("Awaiting 2nd Player",(int(WINDOWw/2),int(WINDOWh/2)),30,(buttonWidth*2,buttonHeight*2))

                time.sleep(2)
                
                MASTER.on_execute(True) #Start Game!
                finished_level_number = 1
                self.level_finished(score_info,finished_level_number)
                continue_game = score_info[0]
                while continue_game:
                    finished_level_number += 1
                    score_info = MASTER.main()
                    self.level_finished(score_info,finished_level_number)
                highscore = score_info[1]
                get_Highscore(playername,highscore)
             
                Gameclient.client.disconnect()
                server.disconnect_clients()
                server.disconnect()    
           #except:
             #   self.blend_in_text("Something went wrong...",(int(WINDOWw/2),int(WINDOWh/2)),20,(buttonWidth*2,buttonHeight*2))
#
  #              time.sleep(2)'''
    #            return "Open_Multi_screen"         
        
        ###############################
        #Mulitplayer Link in
        ###############################
        elif(button.goto_menutitle == "Search"):
            client_ip = self.menu_in_use.writeable_text

            connection_text = "Connecting"
            for dot in " ...":
                connection_text += dot
                self.blend_in_text(connection_text,(int(WINDOWw/2),int(WINDOWh/2)),30,(buttonWidth*2,buttonHeight*2))
                time.sleep(0.5)
                
            #####
            #Multiplayer client aufrufen
            #try:  
                Gameclient.create_Client(port,client_ip)

                self.blend_in_text("Starting Game",(int(WINDOWw/2),int(WINDOWh/2)),30,(buttonWidth*2,buttonHeight*2))

                time.sleep(2)
                
                MASTER.on_execute(True) #Start Game!
                finished_level_number = 1
                self.level_finished(score_info,finished_level_number)
                continue_game = score_info[0]
                while continue_game:
                    finished_level_number += 1
                    score_info = MASTER.main()
                    self.level_finished(score_info,finished_level_number)
                highscore = score_info[1]
                get_Highscore(playername,highscore)
             
                Gameclient.client.disconnect()
            #except:
              #  self.blend_in_text("Connection Failed",(int(WINDOWw/2),int(WINDOWh/2)),30,(buttonWidth*2,buttonHeight*2))
                #Gameclient.client.disconnect()
                #time.sleep(2)'''
                
                return self.menu_in_use.key_name


        #########################
        #Reset Highscore
        #########################

        elif(button.goto_menutitle == "Reset_highscore"):
            reset_Highscore()
            return "Highscore_screen"
        #########################
        #Ende Spiel
        #########################
        
        elif(button.goto_menutitle == "End"):
            pygame.quit()
            sys.exit()
            
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
                    button.image_surf = button.clicked_surf
                    button.image_surf = pygame.transform.scale(button.image_surf,(button.width,button.height)) # Geklickter Button
                    self.on_render()
                    
                    new_menu = self.button_clicked(button)
                    
                    button.image_surf = button.normal_surf
                    if new_menu == "Highscore_screen":
                        self.menu_in_use = Menu("Highscore","Highscore_screen")
                    else:
                        self.menu_in_use = self.menus[new_menu]
                else:
                    self.set_back_button_image() # Behebt Bug des Aufgedecktbleibens
                    
                    button.image_surf = button.cursor_on_surf
                    self.menu_in_use.curser_over_button = button

                button.image_surf = pygame.transform.scale(button.image_surf,(button.width,button.height))
                return
            else:
                self.set_back_button_image()

    def set_back_button_image(self): # Auslagerung auf Methode, da sonst 2mal der Code verwendet wird (oder auftreten eines Bugs)
        if  self.menu_in_use.curser_over_button != None:
            self.menu_in_use.curser_over_button.image_surf = self.menu_in_use.curser_over_button.normal_surf
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

    def interlevel_scene(self, level = 0):
        awesomeness = 0
        pygame.mixer.music.load(game_music)

        if level == 0:
            leveltext = random.choice(Texts.intro_texts)
        elif level == 1:
            leveltext = random.choice(Texts.level_1_texts)
        elif level == 2:
            leveltext = random.choice(Texts.level_2_texts)
        elif level == 3:
            leveltext = random.choice(Texts.level_3_texts)
        else:
            return False
        
        
        for line in leveltext:
            reached_max = False
            alpha_value = 250
            thisPrint = pygame.font.Font('freesansbold.ttf', 25).render(line[0],True,(255,255,255))
            thisRect = thisPrint.get_rect()
            thisRect.center = ((WINDOWw/2,WINDOWh/2-80))
            if line[1] != None:
                image_surf = pygame.image.load(line[1])
                image_surf = pygame.transform.scale(image_surf,(200,200))
                

            alphaSurface = pygame.Surface((WINDOWw,WINDOWh))
            alphaSurface.fill((0,0,0))
            alphaSurface.set_alpha(alpha_value)

            ###
            awesomeness +=1
            self.do_interlevel_effects(awesomeness,leveltext, 1,level)
            ###
        
            
            while alpha_value < 255:
                self.display_surf.fill((0,0,0))
                self.display_surf.blit(thisPrint,thisRect)
                if line[1] != None:
                    self.display_surf.blit(image_surf,(int(WINDOWw/2)-100,int(WINDOWh/2)))
                alphaSurface.set_alpha(alpha_value)
                self.display_surf.blit(alphaSurface,(0,0))
                if awesomeness == 1 and leveltext != Texts.starwars_intro:
                    self.showText("Press 'Space' to skip", textsize = 13)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                        self.endIt()
                    if event.type == KEYUP and event.key == K_SPACE:
                        return
                
                if alpha_value <= 0:
                    time.sleep(0.1)
                    reached_max = True
                    ###
                    self.do_interlevel_effects(awesomeness,leveltext, 2,level)
                    ###
                if reached_max:
                    alpha_value += 3
                else:
                    alpha_value -= 3

    def do_interlevel_effects(self,awesome,leveltext, playtime,level): # Playtime (1 oder 2) wann es gemacht werden soll
        if level == 0:
            if playtime == 1:
                if leveltext == Texts.normal_intro:
                    if awesome == 1:
                        pygame.mixer.music.play(-1, 0.0)
            else:
                if leveltext == Texts.starwars_intro:
                    if awesome == 1:
                        time.sleep(1)
                        pygame.mixer.Sound(star_wars_sound).play()
                    if awesome == 3:
                        pygame.mixer.music.play(-1, 0.0)
        if level == 1:
            pass
        if level == 2:
            pass

                    
    def blend_in_text(self,text,position = (int(WINDOWw/2),int(WINDOWh/2)), textsize = 25, feldgroeße = (buttonWidth*2,buttonHeight*2)): # Texteinblende mit Hintergrund
        # feldgröße ist Breite und Höhe Tupel
            text_surface = (feldgroeße,
                (position[0] - int(feldgroeße[0]/2),position[1] - int(feldgroeße[1]/2)))
        
            image = pygame.transform.scale(searchbar_image, text_surface[0])
            self.display_surf.blit(image,text_surface[1])
            self.showText(text,position,textsize)
            pygame.display.flip()

    def level_finished(self,score_info,finished_level_number):
                        level_end_string = "Congratulations! You've cleared Level " + str(finished_level_number) + "!"
                        self.display_surf.fill((0,0,0))
                        self.showText(level_end_string, (int(WINDOWw/2),int(WINDOWh/2)))
                        pygame.display.flip()
                        time.sleep(2)
                        
                        score_shown = score_info[1]
                        bonus_shown = score_info[2]
                        for i in range(0,int(score_info[2]/2)):
                            self.display_surf.fill((0,0,0))
                            score_shown += 2
                            bonus_shown -= 2
                            self.showText("Level  " + str(finished_level_number) + ":",(int(WINDOWw/2),int(WINDOWh/2) -200),60)
                            self.showText("Bonustime: " + str(bonus_shown),(int(WINDOWw/2),int(WINDOWh/2)-50),30)
                            self.showText("Score: " + str(score_shown),(int(WINDOWw/2),int(WINDOWh/2)),50)
                            pygame.display.flip()
                        if (score_info[2] % 2) == 1:
                            self.display_surf.fill((0,0,0))
                            score_shown += 1
                            bonus_shown -= 1
                            self.showText("Level  " + str(finished_level_number) + ":",(int(WINDOWw/2),int(WINDOWh/2) -200),60)
                            self.showText("Bonustime: " + str(bonus_shown),(int(WINDOWw/2),int(WINDOWh/2)-50),30)
                            self.showText("Score: " + str(score_shown),(int(WINDOWw/2),int(WINDOWh/2)),50)
                            pygame.display.flip()                            
                        time.sleep(2)






    
if __name__ == "__main__":        
    start = Main()
    start.on_execute()
