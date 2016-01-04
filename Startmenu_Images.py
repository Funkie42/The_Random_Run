import pygame
from pygame.locals import *

PFAD = ""

background_image = "Gui/menu.png"


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
load_button = pygame.image.load(PFAD + "Gui/Buttons/red_load_off.png")
load_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/red_load_on.png")
load_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/red_load_clicked.png")

#New Game Button
ng_button = pygame.image.load(PFAD + "Gui/Buttons/red_ng_off.png")
ng_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/red_ng_on.png")
ng_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/red_ng_clicked.png")

#Choose Level Buttn

choose_lvl_button = pygame.image.load(PFAD + "Gui/Buttons/red_choose_off.png")
choose_lvl_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/red_choose_on.png")
choose_lvl_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/red_choose_clicked.png")

######################
#Multiplayer Menu
######################

# Link In Button
link_in_button = pygame.image.load(PFAD + "Gui/Buttons/blue_link_off.png")
link_in_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/blue_link_on.png")
link_in_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/blue_link_clicked.png")

#Open Server Button
open_screen_button = pygame.image.load(PFAD + "Gui/Buttons/red_open_off.png")
open_screen_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/red_open_on.png")
open_screen_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/red_open_clicked.png")

#Try Connecting Button
#search_button = pygame.image.load(PFAD + "Gui/Buttons/bl_search_off.png") 
#search_button_cursor_over  = pygame.image.load(PFAD + "Gui/Buttons/bl_search_on.png")
#search_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/bl_search_clicked.png")
search_button = pygame.image.load(PFAD + "Gui/Buttons/blue_connect_off.png") 
search_button_cursor_over  = pygame.image.load(PFAD + "Gui/Buttons/blue_connect_on.png")
search_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/blue_connect_clicked.png")

#Open a normal game Button
host_normal_button = pygame.image.load(PFAD + "Gui/Buttons/red_normalgame_off.png") 
host_normal_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/red_normalgame_on.png")
host_normal_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/red_normalgame_clicked.png") 

#Open a minigame Button
host_minigame_button = pygame.image.load(PFAD + "Gui/Buttons/red_mini_off.png")
host_minigame_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/red_mini_on.png")
host_minigame_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/red_mini_clicked.png") 

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

searchbar_image = pygame.image.load(PFAD + "Gui/ground.png")
