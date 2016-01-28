import SpriteSheet

#SPIELERSPRITES
character_sprite = SpriteSheet.SpriteSheet("Gui/character.png")
character2_sprite = SpriteSheet.SpriteSheet("Gui/character2.png")
alien_sprite = SpriteSheet.SpriteSheet("Gui/alien.png")
pacman_sprite = SpriteSheet.SpriteSheet("Gui/epm_spritesheet.png")
zyklop_sprite = SpriteSheet.SpriteSheet("Gui/zyklop.png")

#GELÄNDESPRITES
level_grounds = ["Gui/ground5.png","Gui/ground1.png",
                 "Gui/ground2.png","Gui/ground3.png",
                 "Gui/ground4.png","Gui/ground5.png"]

# Background Bilder
tut_bild = "Gui/bg_tut.jpg"
w1_bild = "Gui/bg1.jpg"
w2_bild = "Gui/bg2.jpg"
w3_bild = "Gui/bg3.jpg"
w4_bild = "Gui/bg4.jpg"
w5_bild = "Gui/bg5.jpg"
bg_bilder = [tut_bild,w1_bild,w2_bild,w3_bild,w4_bild,w5_bild]

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
                    (300,300,150,100)]
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
                 (2500,1350,1050,50, 20,"You can shoot Hyper-Space-Balls with the Up-Key"),
                 (4100,1350,300,50, 20,"Ready for some fighting?"),
                 (4900,1350,500,50, 20,"Each Enemy gives you a number of bonus points"),
                 (5400,1250,500,50, 20,"Maybe you should go down"),
                 (5500,1300,400,50, 20,"Your shuttle is waiting"),
                 (4400,2300,400,50, 20,"You can control it with 'WASD'"),
                 (4200,2100,400,50, 20,"It may be a bit difficult at first.."),
                 (3900,1900,500,50, 20,"The Portal is in the upper left corner"),
                 (3500,1900,300,50, 20,"Good luck!"),
                 (200,450,350,50, 20,"You did it!")]

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
                    (200,1250,50,50), #[4]
                    (300,650,200,50),
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
                    (2800,2200,200,50),#[20]
                    (3000,2100,50,150),
                    (2400,2050,50,100),
                       (1500,700,300,50),
                       (1800,700,200,50),
                       (2000,600,50,150),
                       (2050,700,400,50),#[26]
                       (2350,600,50,150),
                       (4500,2000,1500,400),
                       (5000,1950,150,50),
                       (4600,2500,400,3600)]
#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w3_boden_gegner = [(1,2,alien_sprite,1,10),
                (6,8,alien_sprite,5,10),
                (7,5,alien_sprite,1,5),
                   (23,3,alien_sprite,100,200)] # TODO
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w3_flug_gegner = [(400,600,2250,3,pacman_sprite,5,1,True),
                (400,600,2500,3,pacman_sprite,5,10,True),
               (1000,1300,1800,4,pacman_sprite,10,1000,True),
               (1000,1300,2200,4,pacman_sprite,10,1000,True)]
w3_powerups = [("highjump",4),("highjump",14)]
w3_speichpunkte = [12,8,20,24]
w3_steine = [26]
w3_portal = 29

blockkoords = [tut_blockkoordinaten,[],w2_blockkoordinaten,w3_blockkoordinaten]
textboxes = [tut_textboxes,[],[],[],[],[]]
bodengegner = [tut_boden_gegner,[],w2_boden_gegner,w3_boden_gegner]
fluggegner = [tut_flug_gegner,[],w2_flug_gegner,w3_flug_gegner]
speicherpunkte = [tut_speicherpunkte,[],w2_speichpunkte,w3_speichpunkte]
powerups = [tut_powerups,[],w2_powerups,w3_powerups]
steine = [tut_steine,[],w2_steine,w3_steine]
portale = [tut_portal,None,w2_portal,w3_portal]

