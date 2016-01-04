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
