import SpriteSheet

#SPIELERSPRITES
character_sprite = SpriteSheet.SpriteSheet("Gui/character.png")
character2_sprite = SpriteSheet.SpriteSheet("Gui/character2.png")
alien_sprite = SpriteSheet.SpriteSheet("Gui/alien.png")
pacman_sprite = SpriteSheet.SpriteSheet("Gui/epm_spritesheet.png")


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
                 (2700,3250,400,100, 20,"You then can still use the doublejump"),
                 (3650,3200,200,50, 25,"Sometimes..."),
                 (4000,3300,400,100, 20,"You have to jump into the unknown"),
                 (3650,3950,250,100, 20,"..But not this time"),
                 (2850,2550,300,50, 20,"Well Done! I'm surprised"),
                 (2875,2250,250,50, 20,"You seem quite fit"),
                 (2500,2250,300,50,20,"Then let's turn it up a notch"),
                 (2500,1350,1050,50, 20,"You see.. you can shoot surreal-space-balls with the 'Up' Button! They sometimes shoot through walls!"),
                 (4100,1350,300,50, 20,"Ready for some fighting?"),
                 (4900,1350,500,50, 20,"Each Enemy gives you a number of extra points"),
                 (5400,1250,500,50, 20,"I think you should go down now"),
                 (5500,1300,400,50, 20,"Your shuttle is waiting"),
                 (4400,2300,400,50, 20,"You can control it with 'WASD'"),
                 (4200,2100,400,50, 20,"It may be a bit difficult at first..'"),
                 (3900,1900,500,50, 20,"The Portal home is in the upper left corner'"),
                 (3500,1900,300,50, 20,"Good luck!'"),
                 (200,450,350,50, 20,"You did it! Welcome home!'")]

#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
tut_boden_gegner = [(18,0,alien_sprite,5,50000),
                (19,10,alien_sprite,5,20)] # TODO

#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse, Waagrecht oder nicht (Bool, standart true))
tut_flug_gegner = [(4700,4900,1600,10,pacman_sprite,10,50,True),
               (5200,5250,2900,0,pacman_sprite,10,5000,True),
               (4800,4850,2700,0,pacman_sprite,10,5000,True)] # TODO



#LEVEL2
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
w2_blockkoordinaten = [(100,2200,700 ,50),
                    (1700,2000,1200,50),
                    (2900,1700,750, 50),
                    (3650,1700,50, 800),
                    (3650, 2400,1450, 50),
                    (4400,2000,100, 50)]

#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w2_boden_gegner = [] # TODO
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w2_flug_gegner = [] 

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
                    (2400,2050,50,100)]
#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse,Feuerrate)
w3_boden_gegner = [(1,2,alien_sprite,1,10),
                (6,8,alien_sprite,5,10),
                (7,5,alien_sprite,1,5)] # TODO
#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse,Feuerrate, Waagrecht oder nicht (Bool, standart true))
w3_flug_gegner = [(400,600,2250,3,pacman_sprite,5,1,True),
                (400,600,2500,3,pacman_sprite,5,10,True),
               (1000,1300,1800,4,pacman_sprite,10,1000,True),
               (1000,1300,2200,4,pacman_sprite,10,1000,True)] 
'''
#Level a
# Levelmach Vorlage zum schnellen erstellen
###########Blöcke###################
# Inhalt der Tupel:   ( left,   top,    width,  height)
blockkoordinaten = [(1,1,1,1),
                    (1,1,1,1)] # TODO
leveldesign_block = None # z.B. mars oder so
Bloecke_in_lvl = []
for blockkoord in blockkoordinaten:
    Bloecke_in_lvl.append(Boden.Block(pygame.Rect(blockkoord[0],blockkoord[1],
                                              blockkoord[2],blockkoord[3]), leveldesign_block))

###########Gegner###################
gegner_in_lvl = []
#Boden Gegner: (Block, Geschwindigkeit, Sprite, Masse)

boden_gegner = [(1,1,1,1),
                     (1,1,1,1)] # TODO

#Fliegender Gegner: (anfang, ende, topOrleft, Geschwindigkeit, Sprite, Masse, Waagrecht oder nicht (Bool, standart true))

flug_gegner = [(1,1,1,1),
                     (1,1,1,1)] # TODO

for gegner in boden_gegner:
    gegner_in_lvl.append(Hindernis.Gegner(gegner[0],gegner[1],gegner[2],gegner[3]))
for gegner in flug_gegner:
    gegner_in_lvl.append(Hindernis.FliegenderGegner(gegner[0],gegner[1],gegner[2],gegner[3],gegner[4],gegner[5],gegner[6]))

#############Power_Ups###############

powerups_in_lvl = []
#############Speicherpunkte############

speichpt_in_lvl = []
welt_a_bild = None
welt_a = Welt(welt_a_bild, Bloecke_in_lvl, gegner_in_lvl,powerups_in_lvl,speichpt_in_lvl,s,s2)
'''
