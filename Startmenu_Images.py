import pygame
from pygame.locals import *

PFAD = ""

background_image = "Gui/background.jpg"


#Generic Button
buttonImage = pygame.image.load(PFAD + "Gui/Buttons/bl_off.png")
buttonCursorOver = pygame.image.load(PFAD + "Gui/Buttons/bl_on.png")
buttonClicked = pygame.image.load(PFAD + "Gui/Buttons/bl_clicked.png")

#Back Button
back_button = pygame.image.load(PFAD + "Gui/Buttons/bl_back_off.png")
back_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/bl_back_on.png")
back_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/bl_back_clicked.png")



####################
#Main Menu#
####################

#Singleplayer Button
singleplayer_button = pygame.image.load(PFAD + "Gui/Buttons/red_sp_off.png")
singleplayer_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/red_sp_on.png")
singleplayer_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/red_sp_clicked.png")

#Multiplayer Button
multiplayer_button = pygame.image.load(PFAD + "Gui/Buttons/blue_mp_off.png")
multiplayer_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/blue_mp_on.png")
multiplayer_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/blue_mp_clicked.png")

#Quit Button
quit_button = pygame.image.load(PFAD + "Gui/Buttons/quit_button_off.png")
quit_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/quit_button_on.png")
quit_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/quit_button_clicked.png")

#Credits Button
credits_button = pygame.image.load(PFAD + "Gui/Buttons/bl_credits_off.png")
credits_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/bl_credits_on.png")
credits_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/bl_credits_clicked.png")

#Highscore Button
highscore_button = pygame.image.load(PFAD + "Gui/Buttons/bl_high_off.png")
highscore_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/bl_high_on.png")
highscore_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/bl_high_clicked.png")


#####################
#Singleplayer Menu
#####################

#Load Button
load_button = pygame.image.load(PFAD + "Gui/Buttons/tutorial_off.png")
load_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/tutorial_on.png")
load_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/tutorial_clicked.png")

#New Game Button
ng_button = pygame.image.load(PFAD + "Gui/Buttons/new_game_off.png")
ng_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/new_game_on.png")
ng_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/new_game_clicked.png")

#Choose Level Buttn

choose_lvl_button = pygame.image.load(PFAD + "Gui/Buttons/choose_lvl_off.png")
choose_lvl_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/choose_lvl_on.png")
choose_lvl_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/choose_lvl_clicked.png")

######################
#Multiplayer Menu
######################

# Link In Button
link_in_button = pygame.image.load(PFAD + "Gui/Buttons/link_in_off.png")
link_in_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/link_in_on.png")
link_in_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/link_in_clicked.png")

#Open Server Button
open_screen_button = pygame.image.load(PFAD + "Gui/Buttons/open_game_off.png")
open_screen_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/open_game_on.png")
open_screen_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/open_game_clicked.png")

#Try Connecting Button
search_button = pygame.image.load(PFAD + "Gui/Buttons/connect_off.png") 
search_button_cursor_over  = pygame.image.load(PFAD + "Gui/Buttons/connect_on.png")
search_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/connect_clicked.png")

#Open a normal game Button
host_normal_button = pygame.image.load(PFAD + "Gui/Buttons/blue_ghostmode_off.png") 
host_normal_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/blue_ghostmode_on.png")
host_normal_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/blue_ghostmode_clicked.png") 

#Open a minigame Button
host_minigame_button = pygame.image.load(PFAD + "Gui/Buttons/blue_duell_off.png")
host_minigame_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/blue_duell_on.png")
host_minigame_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/blue_duell_clicked.png") 

#####################
#Highscore Menu
#####################
#Rest Highscore Button
reset_button = pygame.image.load(PFAD + "Gui/Buttons/reset_off.png")
reset_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/reset_on.png")
reset_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/reset_clicked.png")

#Change Name Button
cn_button = pygame.image.load(PFAD + "Gui/Buttons/cn_off.png")
cn_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/cn_on.png")
cn_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/cn_clicked.png")

#Confirm Button
confirm_button = pygame.image.load(PFAD + "Gui/Buttons/confirm_off.png")
confirm_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/confirm_on.png")
confirm_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/confirm_clicked.png")

######################
#End Game Menu
######################

#Yes Button
yes_button = pygame.image.load(PFAD + "Gui/Buttons/bl_yes_off.png")
yes_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/bl_yes_on.png")
yes_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/bl_yes_clicked.png")

#Benutzen??
#No Button
no_button = pygame.image.load(PFAD + "Gui/Buttons/bl_no_off.png")
no_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/bl_no_on.png")
no_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/bl_no_clicked.png")






# Search Bar

searchbar_image = pygame.image.load(PFAD + "Gui/fenster.png")
