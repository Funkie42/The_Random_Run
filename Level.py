import SpriteSheet

#SPIELERSPRITES
character_sprite = SpriteSheet.SpriteSheet("Gui/character.png")
character2_sprite = SpriteSheet.SpriteSheet("Gui/character2.png")
alien_sprite = SpriteSheet.SpriteSheet("Gui/alien.png")
pacman_sprite = SpriteSheet.SpriteSheet("Gui/epm_spritesheet.png")
zyklop_sprite = SpriteSheet.SpriteSheet("Gui/zyklop.png")

#GELÄNDESPRITES
level_grounds = ["Gui/ground5.png","Gui/ground.png",
                 "Gui/ground2.png","Gui/ground3.png",
                 "Gui/ground4.png","Gui/ground5.png","Gui/ground5.png"]

# Background Bilder
tut_bild = "Gui/bg_tut.jpg"
w1_bild = "Gui/bg1.jpg"
w2_bild = "Gui/bg2.jpg"
w3_bild = "Gui/bg3.jpg"
w4_bild = "Gui/bg4.jpg"
w5_bild = "Gui/bg5.jpg"
w6_bild = w4_bild
bg_bilder = [tut_bild,w1_bild,w2_bild,w3_bild,w4_bild,w5_bild,w6_bild]

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
                    (3650,3190,200,10)]
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
w1_blockkoordinaten = [(50, 3000, 300, 50),
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
                       (4300, 2100, 50, 50)]

#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w1_boden_gegner = [(2, 3, alien_sprite, 50, 100),
                   (5, 3, alien_sprite, 100, 100),
                   (8, 3, alien_sprite, 1, 100),
                   (12, 3, alien_sprite, 10, 100),
                   (30, 10, alien_sprite, 10, 10)]
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
w2_blockkoordinaten = [(100,2200,700 ,300),
                    (1700,2000,1000,100),
                    (2900,1700,750, 100),
                    (3651,1700,100, 800),
                    (3750, 2400,1450, 100),
                    (4400,2000,100, 100), # 5
                       (1100,2100,300,100),
                       (0,0,100,2500)]

#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w2_boden_gegner = [(2,10,alien_sprite,1,22),
                   (2,10,alien_sprite,1,22)] 
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w2_flug_gegner = []
w2_powerups = []
w2_speichpunkte = []
w2_steine= []
w2_portal = 4


#LEVEL3
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
w3_blockkoordinaten = [(50,2000,350,80),
                    (500,3000,100,100),
                    (0,1500,50,580),
                    (0,1400,900,100),
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
                       (1500,700,300,50),
                       (1800,700,200,50),
                       (2000,600,50,150),
                       (2050,700,350,50),#[26]
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
w4_blockkoordinaten = [(150,7600,400,200),
                       (700,7650,300,150),
                       (0,6700,100,1100),
                       (100,7600,50,200),
                       (100,100,100,100)]
w4_textboxes = []
#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w4_boden_gegner = [] # TODO
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w4_flug_gegner = []
w4_powerups = []
w4_speichpunkte = []
w4_steine = []
w4_portal = 4

#LEVEL5
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
w5_blockkoordinaten = [(100,100,100,100),
                       (100,100,100,100),
                       (100,100,100,100),
                       (100,100,100,100),
                       (100,100,100,100)]
w5_textboxes = []
#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w5_boden_gegner = [] # TODO
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w5_flug_gegner = []
w5_powerups = []
w5_speichpunkte = []
w5_steine = []
w5_portal = 0

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

blockkoords = [tut_blockkoordinaten,w1_blockkoordinaten,w2_blockkoordinaten,w3_blockkoordinaten,w4_blockkoordinaten,w5_blockkoordinaten,w6_blockkoordinaten]
textboxes = [tut_textboxes,[],[],w3_textboxes,w4_textboxes,w5_textboxes,w6_textboxes]
bodengegner = [tut_boden_gegner,w1_boden_gegner,w2_boden_gegner,w3_boden_gegner,w4_boden_gegner,w5_boden_gegner,w6_boden_gegner]
fluggegner = [tut_flug_gegner,w1_flug_gegner,w2_flug_gegner,w3_flug_gegner,w4_flug_gegner,w5_flug_gegner,w6_flug_gegner]
speicherpunkte = [tut_speicherpunkte,w1_speichpunkte,w2_speichpunkte,w3_speichpunkte,w4_speichpunkte,w5_speichpunkte,w6_speichpunkte]
powerups = [tut_powerups,w1_powerups,w2_powerups,w3_powerups,w4_powerups,w5_powerups,w6_powerups]
steine = [tut_steine,w1_steine,w2_steine,w3_steine,w4_steine,w5_steine,w6_steine]
portale = [tut_portal,w1_portal,w2_portal,w3_portal,w4_portal,w5_portal,w6_portal]

