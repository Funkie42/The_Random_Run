import SpriteSheet, pygame

#SPIELERSPRITES
character_sprite = SpriteSheet.SpriteSheet("Gui/character.png")
character2_sprite = SpriteSheet.SpriteSheet("Gui/character2.png")
alien_sprite = SpriteSheet.SpriteSheet("Gui/alien.png")
pacman_sprite = SpriteSheet.SpriteSheet("Gui/epm_spritesheet.png")
zyklop_sprite = SpriteSheet.SpriteSheet("Gui/zyklop.png")
zyklop_sprite.sprite_sheet = pygame.transform.flip(zyklop_sprite.sprite_sheet,True,False)
endgegner_sprite = SpriteSheet.SpriteSheet("Gui/ufo_sprite_sheet.png")

#GELÄNDESPRITES
level_grounds = ["Gui/ground5.png","Gui/ground.png",
                 "Gui/ground2.png","Gui/ground3.png",
                 "Gui/ground4.png","Gui/ground5.png","Gui/ground5.png","Gui/keyboard.jpg"]

# Background Bilder
tut_bild = "Gui/bg_tut.jpg"
w1_bild = "Gui/bg1.jpg"
w2_bild = "Gui/bg2.jpg"
w3_bild = "Gui/bg3.jpg"
w4_bild = "Gui/bg4.jpg"
w5_bild = "Gui/bg5.jpg"
w6_bild = "Gui/bg_bonus.jpg"
bg_bilder = [tut_bild,w1_bild,w2_bild,w3_bild,w4_bild,w5_bild,w6_bild,w6_bild]

########################Tutorial#######################################################################
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
tut_blockkoordinaten = [(100,4000,900,500),
                    (1200,4000,800,500),
                    (1600,3800,200,50),
                    (1800,3800,200,50),
                    (1000,4100,200,400),
                    (2200,3800,200,50),#[5]
                    (2600,3800,200,50),
                    (2600,4000,500,500),
                    (3100,4000,50,500),
                    (3150,3500,800,1000),
                    (3350,3050,100,50), #[10]
                    (2800,2800,400,50),
                    (2500,2000,50,50),
                    (2550,1800,50,50),
                    (2700,1600,1000,100),
                    (3700,1300,50,400),
                    (3750,1300,100,50),
                    (3850,1300,50,400), # [17]
                    (3750,1600,100,100),
                    (3900,1600,600,100),
                    (4500,1600,200,100),
                    (4600,1700,400,100),
                    (4900,1600,600,100),
                    (5500,1500,100,200),
                    (5900,0,100,4000),# [24]
                    (5500,3000,400,1500),
                    (4900,2800,50,50),
                    (4500,2600,200,100),
                    (0,0,100,4500), #  [28]
                    (100,0,6000,100),
                    (300,300,150,100),
                    (3650,3190,200,10)
                        ]
# Inhalt der Tupel:   (left,   top,    width,  height,size,text)
tut_textboxes = [(200,3700,800,60,35,"Welcome to the tutorial of 'The Random Run'"),
                 (600,4100,350,40,25,"Press 'Space' to jump"),
                 (1250,4050,450,40, 25,"Press 'Space' twice to doublejump"),
                 (2050,4050,500,200, 25,"Don't jump down there though.."),
                 (2900,4050,500,100, 25,"To jump extra high, use the highjump!"),
                 (2700,3250,400,100, 20,"You can still use the doublejump"),
                 (3650,3200,200,50, 25,"Sometimes..."),
                 (4000,3300,400,100, 20,"You have to jump into the unknown"),
                 (3650,3950,250,100, 20,"..But not this time"),
                 (2850,2550,300,50, 20,"Well Done!"),
                 (2875,2250,250,50, 20,"You seem quite fit"),
                 (2500,2250,300,50,20,"Let's turn it up a notch"),
                 (2800,1350,750,50, 20,"You can shoot Hyper-Space-Balls with the Up-Key"),
                 (4100,1350,300,50, 20,"Ready for some fighting?"),
                 (4900,1350,500,50, 20,"Each Enemy gives you a number of bonus points"),
                 (5400,1250,500,50, 20,"Maybe you should go down"),
                 (5500,1300,400,50, 20,"Your shuttle is waiting"),
                 (4450,2200,400,50, 20,"You can control it with 'WASD'"),
                 (3900,2500,400,50, 20,"It may be a bit difficult at first.."),
                 (4200,2140,500,50, 20,"The Portal is in the upper left corner"),
                 (3800,2450,300,50, 20,"Good luck!"),
                 (200,450,350,50, 20,"You did it!"),
                 (200,4050,200,50,20,"Use ← or → to move")]

#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
tut_boden_gegner = [(18,0,alien_sprite,5,50000),
                (19,10,zyklop_sprite,5,20)] # TODO


#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse, Waagrecht oder nicht (Bool, standart true))
tut_flug_gegner = [(4700,4900,1600,10,pacman_sprite,10,50,True),
               (5200,5250,2900,0,pacman_sprite,10,5000,True),
               (4800,4850,2700,0,pacman_sprite,10,5000,True)] # TODO

tut_speicherpunkte = [3,9,11,14,25] #Block nummer
tut_powerups = [("highjump",8)]
tut_portal = 30 #Block nummer
tut_steine = [27]

#LEVEL1
# Inhalt der Tupel:   ( left,   top,    width,  height)
w1_blockkoordinaten = [(50, 3000, 500, 50),
                    (550, 3000, 300, 50),
                    (950, 2850, 300, 50),
                     (1250, 2850, 50, 450),
                       (1550, 2400, 50, 650),
                       (1300, 3250, 800, 50), #5
                       (1600, 3000, 350, 50),
                       (2100, 2600, 50, 700),
                       (1750, 2550, 300, 50),
                       (2350, 2550, 150, 50),
                       (2500, 2550, 150, 50), #10
                       (2650, 2100, 50, 1100),
                       (2450, 2750, 200, 50),
                       (2550, 2950, 100, 50),
                       (2600, 3150, 50, 50),
                       (2500, 3350, 50, 50),
                       (2400, 3550, 50, 50),
                       (2500, 3750, 50, 50),
                       (2200, 3950, 250, 50), #18
                       (1500, 3950, 50, 50),
                       (600, 3950, 250, 50),
                       (400, 4200, 1, 1),
                       (2700, 2950, 100, 50),
                       (2700, 2950, 150, 50),
                       (2700, 2700, 100, 50),
                       (3000, 2250, 150, 50),
                       (3300, 2000, 50, 50), # 26
                       (3500, 2000, 50, 50), # 27
                       (3700, 2000, 50, 50),
                       (3200,2250,50,1500),
                       (3900, 2000, 150, 50),
                       (3850, 1950, 50, 100), # 31
                       (4050, 1600, 50, 250),  # Auskommentiert!?
                       (4300, 2100, 50, 50),
                       #(0,2500,50,550)
                       ]

#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w1_boden_gegner = ((2, 3, zyklop_sprite, 50, 100),
                   (5, 3, alien_sprite, 100, 100),
                   (8, 3, alien_sprite, 1, 100),
                   (12, 3, alien_sprite, 10, 100),
                   (30, 10, alien_sprite, 10, 10))
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w1_flug_gegner = [(1600, 2100, 3850, 4, pacman_sprite, 10, 100,True),
                  (900, 1450, 3850, 6, pacman_sprite, 10, 100,True),
                  (4100, 4500, 1000, 6, pacman_sprite, 10, 100, False),
                  (4100, 4500, 1500, 6, pacman_sprite, 10, 100, False),
                  (4100, 4500, 200, 6, pacman_sprite, 10, 100, False),
                  (3300, 3750, 1800, 15, pacman_sprite, 10, 25,True),
                  (3300, 3750, 2200, 15, pacman_sprite, 10, 25,True)]
w1_powerups = [("highjump",6),("highjump",24)]
w1_speichpunkte = [10,20,22]
w1_steine= [21]
w1_portal = 33

#LEVEL2
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
w2_blockkoordinaten = [(100, 5000, 100, 50),  (200, 4900, 100, 50), (300, 4700, 100, 50), (400, 4400, 100, 50), (500, 4100, 200, 50), (600, 3600, 100, 50),
                       (1000, 3600, 100, 50), (1450, 3600, 200, 50), (2000, 3600, 700, 50), (2700, 3100, 100, 50), (1900, 3600, 100, 50)#10
                       ,(3900, 4000, 100, 50)]

#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w2_boden_gegner = [] 
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w2_flug_gegner = [(2850, 3150, 3100, 5, pacman_sprite, 10, 125, True),(3200, 3550, 3100, 5, pacman_sprite, 10, 125, True),(3600, 3900, 3100, 5, pacman_sprite, 10, 125, True),
                  (3100, 3500, 4000, 5, pacman_sprite, 10, 125, False), (3600, 4000, 4000, 5, pacman_sprite, 10, 125, False)]
w2_powerups = [("highjump", 4), ("dash", 6), ("highjump", 8)]
w2_speichpunkte = [9]
w2_steine= []
w2_portal = 11


#LEVEL3
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
w3_blockkoordinaten = [(150,2000,300,80),
                    (500,3000,100,100),
                    (50,1500,100,580),
                    (50,1400,850,100),
                    (200,1250,70,50), #[4]
                    (300,750,200,50),
                    (850,650,400,50),
                    (800,3000,500,100), #[7]
                    (900,2700,400,100),
                    (800,1640,100,1160),
                    (1300,2950,100,150),
                    (1400,2500,100,1000),
                    (900,1900,1100,100), #[12]
                    (1600,2000,200,1000),
                    (1700,3200,250,500), # [14]
                    (1200,3700,400,100),
                    (1800,2700,50,50),
                    (2000,2500,50,50),
                    (2200,2400,50,50),
                    (2400,2300,50,50),
                    (2800,2200,200,1750),#[20]
                    (3000,2100,100,1850),
                    (2400,2050,50,100),
                       (1400,700,300,50),
                       (1750,700,250,50),
                       (1850,600,50,150),
                       (2000,700,400,50),#[26]
                       (2350,600,50,300),
                       (4500,2000,1500,400),
                       (5000,1950,150,50),
                       (4600,2500,400,3600),
                       (1500,100,6300,200),
                       (2400,800,300,100), #32
                       (2720,800,300,100),
                       (3040,800,300,100),
                       (3360,800,300,100),
                       (3680,800,300,100),
                       (4000,800,300,100),
                       (4350,800,950,100),
                       (4600,600,150,50), #39
                       (4600,550,20,100),
                       (4800,700,150,50),
                       (4800,650,20,100),
                       (5100,300,200,200),#43
                       (5100,600,200,200),
                       (5300,800,375,400),
                       (4940,650,10,100),
                       (4740,550,10,100),
                       (5800,300,200,1000), #48
                       (5150,1300,800,100),
                       (5000,1000,150,400),
                       (3000,1000,2000,100),
                       (2800,900,100,600), #52
                       (2900,1400,300,100),
                      # (3400,1600,60,30),
                      # (3700,1800,60,30),
                      # (4200,1800,60,30),
                       (1000,3430,50,50),
                       (800,3200,50,50),
                       (100,3000,200,100)]
w3_textboxes = [(1300,3725,200,50,20,"Wrong way..")]
#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w3_boden_gegner = [(1,2,alien_sprite,1,10),
                (6,8,alien_sprite,5,10),
                (7,5,alien_sprite,1,5),
                   (23,3,alien_sprite,100,200),
                   (32,100,alien_sprite,100,10000),
                   (33,100,alien_sprite,100,10000),
                   (34,50,alien_sprite,100,10000),
                   (35,100,alien_sprite,100,10000),
                   (36,100,alien_sprite,100,10000),
                   (37,50,alien_sprite,100,10000),
                   (39,2,alien_sprite,5,6),
                   (41,4,alien_sprite,5,6),
                   (49,0,alien_sprite,1,1)] # TODO
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w3_flug_gegner = [(400,600,2250,3,pacman_sprite,5,10,True),
                (400,600,2500,3,pacman_sprite,5,10,True),
               (1000,1300,1800,4,pacman_sprite,10,1000,True),
               (1000,1300,2200,4,pacman_sprite,10,1000,True),
                (2500,3000,350,10,pacman_sprite,10,10,True),
                  (3000,3500,350,10,pacman_sprite,10,10,True),
                  (3500,4000,350,10,pacman_sprite,10,10,True),
                  (300,680,4400,55,pacman_sprite,10,2,False),
                  (1300,1600,3550,5,pacman_sprite,10,20000,False),
                  (1500,1800,3850,5,pacman_sprite,10,20000,False)]
w3_powerups = [("highjump",4),("highjump",14)]
w3_speichpunkte = [12,8,20,24,45]
w3_steine = [26]
w3_portal = 29

#LEVEL4
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
schräge = []
x = 2000
#while x < 3600:
#    y = 8070 - x
#    schräge.append((x,y,1,20))
#    x += 3
w4_blockkoordinaten = [(200,7750,400,250),
                       (700,7750,300,250),
                       (50,6700,100,1300),
                       (150,7750,50,250), #3
                       (150,100,100,100),
                       (1200,7750,50,50),
                       (1200,7500,50,50),
                       (1500,7750,50,50),
                       (1500,7500,50,50),
                        (1800,7750,50,50),
                       (1800,7500,50,50),#10
                       (2100,7500,200,100),
                       (2300,7250,100,350),
                       (2100,7000,50,50),
                       (1400,6900,400,50),
                       (1200,6800,50,30),
                       (1400,6550,50,20),
                       (1750,6550,50,10),
                       (2200,6550,200,100),
                       (2300,6650,200,100),
                       (2400,6750,200,100),#20
                       (2600,6850,400,100),
                       (2500,6850,100,100),
                       (3000,6850,100,100),
                       (3000,6750,200,100),
                       (3100,6650,200,100),
                       (3200,6550,200,100),
                       (3000,6950,100,1050), #27
                       (3300,7750,400,250),
                       (3950,7750,20,50),
                       (4200,7750,20,50),
                       (4480,7750,20,50),
                       (4730,7750,20,50),
                       (4980,7750,20,50),
                       (5250,7750,20,50),
                       (5500,7600,40,400),
                       (5500,7700,150,300), #36
                       (5650,7400,40,600),
                       (5650,7500,150,300),
                       (5800,7200,40,600),
                       (5800,7300,150,300), #40
                       (5950,6000,50,1600),
                       (5900,6800,50,30),
                       (5600,6600,100,50),
                       (5200,6600,100,50),
                       (5125,6450,50,50),
                       (5000,6200,100,50), #46
                       (4740,5950,250,100),
                       (4500,5800,200,100),
                       (4000,5700,600,100),
                       (3900,4450,100,1350),
                       (4000,5450,50,50),
                       (4000,5200,50,50),
                       (4000,4950,50,50), #53
                       (4000,4700,50,50),
                       (3600,4450,300,150),
                       (3600,4600,100,200),
                       (3400,4700,200,100),
                       (3400,4750,100,250),
                       (3200,4900,200,100),
                       (3200,4950,100,250),#60
                       (3000,5100,200,100),
                       (3000,5150,100,250),
                       (2800,5300,200,100),
                       (2800,5350,100,250),
                       (2600,5500,200,100),
                       (2600,5550,100,250),
                       (2400,5700,200,100),
                       (2400,5750,100,250),
                       (2200,5900,200,100),
                       (2200,5950,100,250),#70
                       (2000,6100,200,100), #Ende schräge
                       (1400,6100,600,100),
                       (1200,6100,200,100),
                       (700,6000,150,50),
                       (400,5900,50,50),
                       (420,5600,50,50),
                       (440,5300,50,50),
                       (460,5000,50,50),
                       (400,4800,50,50),
                       (600,4750,100,50), #80
                       (900,4700,100,50),
                       (1200,4650,100,50),
                       (1500,4600,40,1300),
                       (1500,4700,150,100), #84
                       (1650,4500,40,300),
                       (1650,4600,150,200),
                       (1800,4400,40,400),
                       (1800,4500,150,300),
                       (1950,4300,200,500),
                       (2150,4700,400,100),#90
                       (2550,4450,250,100),
                       (2800,4200,300,100),
                       (2900,3900,1,1),
                       (2800,3600,300,100),
                       (3100,3600,50,700),
                       (2550,4550,50,700),
                       (2800,4300,50,250),
                       ] + schräge
w4_textboxes = []
#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w4_boden_gegner = [(14,25,alien_sprite,20,25),
                   (21,30,alien_sprite,20,1000),
                   (38,10,alien_sprite,20,7),
                   (36,10,alien_sprite,20,7),
                   (40,10,alien_sprite,20,7),
                   (47,30,alien_sprite,20,10000),
                   (49,30,alien_sprite,20,10),
                   (72,40,alien_sprite,20,10000),
                   (84,10,alien_sprite,20,6),
                   (86,10,alien_sprite,20,5),
                   (88,10,alien_sprite,20,4),
                   (71,10,alien_sprite,20,19),
                   (69,10,alien_sprite,20,12),
                   (67,10,alien_sprite,20,25),
                   (65,10,alien_sprite,20,10),
                   (63,10,alien_sprite,20,17),
                   (61,10,alien_sprite,20,14),
                   (59,10,alien_sprite,20,10),
                   (57,10,alien_sprite,20,18)] 
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w4_flug_gegner = [(7500,7800,1375, 12, pacman_sprite,10,10,False),
                  (7350,7650,1675, 12, pacman_sprite,10,10,False),
                  (6200,6450,2800,10,pacman_sprite,10,8,False),
                  (6500,6550,2800,5,pacman_sprite,10,8,False),
                  (4300,4700,4600,15,pacman_sprite,20,8,True),
                  (4300,4700,5000,15,pacman_sprite,10,8,True),
                  (5000,6000,600,60,pacman_sprite,10,6,False),
                  (4000,4500,2325,42,pacman_sprite,10,8,False)]
w4_powerups = [("highjump",40)]
w4_speichpunkte = [11,28,73]
w4_steine = []
w4_portal = 93

#LEVEL5
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
w5_blockkoordinaten = [(200,4000,800,300),
                        (0,3300,100,700),
                       (0,4000,200,300),
                       (100,3300,1400,300),
                       (1000,4000,500,300),
                       (1500,3800,2000,300),
                       (1500,3300,2000,400),#6
                       (1500,4000,400,300),
                       (100,100,100,100),
                       (3500,3800,400,1000),
                       (3860,3000,30,1600),
                       (3500,3400,400,300),
                       (3800,3800,1,1), #12
                       (3900,4500,1000,300),
                       (4900,3200,400,1600),
                       (3500,2900,1800,300),
                       (3500,3200,400,200),
                       (4100,4250,50,50),
                       (4100,4000,50,50),
                       (4100,750,0,0),
                       (4100,500,0,0),#20
                       (4700,4250,50,50),
                       (4700,4000,50,50),
                       (4700,3750,50,50),
                       (4700,500,0,0),
                       (4420,3875,50,50),
                       (4420,4125,50,50),
                       (4420,3625,50,50),
                       (4380,3350,1,0), #28
                       ]
w5_textboxes = [(400,3700,800,60,20,"You feel it, it's the final stretch"),
                (1600,3600,400,60,20,"As you walk down the corridor"),
                 (1600,3850,400,60,16,"You sense that there's just one enemy left"),
                (2100,3600,400,60,20,"Excited to finally see what he looks like"),
                (2100,3850,400,60,20,"You keep walking.."),
                 (2600,3600,400,60,20,"Nothing left to do, just you and him"),
                  (3200,3600,200,60,20,"It's showtime!"),
                (3400,3850,200,60,20,"Let's dash")]
#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w5_boden_gegner = [] # TODO
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w5_flug_gegner = []
w5_powerups = [("dash",12)]
w5_speichpunkte = []
w5_steine = []
w5_portal = 8

#6 Level
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
w6_blockkoordinaten = [(300,7700,500,300),
                       (0,6000,300,2000),
                       (2300,6000,300,2000),
                       (300,6000,2000,300),
                       (2200,7700,100,300), #4
                       (100,100,1,1),
                       (700,7500,200,50),
                       (1700,7500,200,50),
                       (1000,7250,50,50),
                       (1300,7250,50,50),
                       (1600,7250,50,50), # 10
                       (700,7250,50,50),
                       (1850,7250,50,50),
                       (800,7000,50,50),
                       (1750,7000,50,50),
                       (900,6800,750,50), #15
                       (950,6600,25,200),
                       (1600,6600,25,200),
                       (950,6300,25,200),
                       (1600,6300,25,200),
                       (300,6700,200,50), #20
                       (2150,6700,200,50),
                       (1800,7700,400,300)]
w6_textboxes = []
#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w6_boden_gegner = [] # TODO
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w6_flug_gegner = []
w6_powerups = []
w6_speichpunkte = []
w6_steine = []
w6_portal = 5

# Bonus Level
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
bonus_blockkoordinaten =   [(0,1000,800 ,300),
                            (800,0,500,8000)]
                    
                           
bonus_boden_gegner = []
bonus_flug_gegner = []
bonus_powerups = []
bonus_speicherpunkte = []
bonus_steine = []
bonus_portal = 1

blockkoords = [tut_blockkoordinaten,w1_blockkoordinaten,w2_blockkoordinaten,w3_blockkoordinaten,w4_blockkoordinaten,w5_blockkoordinaten,w6_blockkoordinaten,bonus_blockkoordinaten]
textboxes = [tut_textboxes,[],[],w3_textboxes,w4_textboxes,w5_textboxes,w6_textboxes,[]]
bodengegner = [tut_boden_gegner,w1_boden_gegner,w2_boden_gegner,w3_boden_gegner,w4_boden_gegner,w5_boden_gegner,w6_boden_gegner,bonus_boden_gegner]
fluggegner = [tut_flug_gegner,w1_flug_gegner,w2_flug_gegner,w3_flug_gegner,w4_flug_gegner,w5_flug_gegner,w6_flug_gegner,bonus_flug_gegner]
speicherpunkte = [tut_speicherpunkte,w1_speichpunkte,w2_speichpunkte,w3_speichpunkte,w4_speichpunkte,w5_speichpunkte,w6_speichpunkte,bonus_speicherpunkte]
powerups = [tut_powerups,w1_powerups,w2_powerups,w3_powerups,w4_powerups,w5_powerups,w6_powerups,bonus_powerups]
steine = [tut_steine,w1_steine,w2_steine,w3_steine,w4_steine,w5_steine,w6_steine,bonus_steine]
portale = [tut_portal,w1_portal,w2_portal,w3_portal,w4_portal,w5_portal,w6_portal,bonus_portal]


