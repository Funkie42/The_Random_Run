import pygame
from pygame.locals import *

PFAD = ""

background_image = "Gui/menu.png"


#Generic Button
buttonImage = pygame.image.load(PFAD + "Gui/Buttons/bl_off.png")
buttonCursorOver = pygame.image.load(PFAD + "Gui/Buttons/bl_on.png")
buttonClicked = pygame.image.load(PFAD + "Gui/Buttons/bl_clicked.png")

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

#Back Button
back_button = pygame.image.load(PFAD + "Gui/Buttons/bl_back_off.png")
back_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/bl_back_on.png")
back_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/bl_back_clicked.png")

#Load Button
load_button = pygame.image.load(PFAD + "Gui/Buttons/red_load_off.png")
load_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/red_load_on.png")
load_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/red_load_clicked.png")

#New Game Button
ng_button = pygame.image.load(PFAD + "Gui/Buttons/red_ng_off.png")
ng_button_cursor_over = pygame.image.load(PFAD + "Gui/Buttons/red_ng_on.png")
ng_button_clicked = pygame.image.load(PFAD + "Gui/Buttons/red_ng_clicked.png")


#Credits Button
buttonImage = pygame.image.load(PFAD + "Gui/Buttons/bl_credits_off.png")
buttonCursorOver = pygame.image.load(PFAD + "Gui/Buttons/bl_credits_on.png")
buttonClicked = pygame.image.load(PFAD + "Gui/Buttons/bl_credits_clicked.png")

#Highscore Button
buttonImage = pygame.image.load(PFAD + "Gui/Buttons/bl_high_off.png")
buttonCursorOver = pygame.image.load(PFAD + "Gui/Buttons/bl_high_on.png")
buttonClicked = pygame.image.load(PFAD + "Gui/Buttons/bl_high_clicked.png")

#Yes Button
buttonImage = pygame.image.load(PFAD + "Gui/Buttons/bl_yes_off.png")
buttonCursorOver = pygame.image.load(PFAD + "Gui/Buttons/bl_yes_on.png")
buttonClicked = pygame.image.load(PFAD + "Gui/Buttons/bl_yes_clicked.png")

#No Button
buttonImage = pygame.image.load(PFAD + "Gui/Buttons/bl_no_off.png")
buttonCursorOver = pygame.image.load(PFAD + "Gui/Buttons/bl_no_on.png")
buttonClicked = pygame.image.load(PFAD + "Gui/Buttons/bl_no_clicked.png")



# Search Bar

searchbar_image = pygame.image.load(PFAD + "Gui/ground.png")
