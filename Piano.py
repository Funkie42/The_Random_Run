import pygame, time

timer = 0

##############
##  Sounds ##
#############
key_sound = ['Sounds/c.ogg','Sounds/d.ogg','Sounds/e.ogg','Sounds/f.ogg','Sounds/g.ogg','Sounds/a.ogg','Sounds/h.ogg','Sounds/c2.ogg']

pygame.init()
pygame.mixer.init()





def play_key(key_sound):
    global timer
    
    #if timer == 0:
    pygame.mixer.Sound(key_sound).play()
    time.sleep(0.05)
    timer += 1
    #if timer == 5:
    #         timer = 0
    
    #pygame.mixer.Sound.stop()  


        
def majestro(x,y): 
    
                                                                                
                                            # Nur im Bonuslevel
            if y > 952.0:                 # Check von Spielerhöhe
                if x >= 110.0:            # Beginn des Keyboards
                    if x < 185.0:         # Ende 1. Taste
                        play_key(key_sound[0])
                        #time.sleep(0.1)                                    #C
                        #key_c.stop()
        
                if x >= 186.0:
                    if x < 260.0:
                        play_key(key_sound[1])
                        #time.sleep(0.1)                                     #D
                        #key_c.stop()
        
                if x >= 261.0:
                    if x < 335.0:
                        play_key(key_sound[2])
                        #time.sleep(0.1)                                     #E
                        #key_c.stop()
            
                if x >= 336.0:
                    if x < 410.0:
                        play_key(key_sound[3])
                        #time.sleep(0.1)                                     #F
                        #key_c.stop()
                    
                if x >= 411.0:
                    if x < 485.0:
                        play_key(key_sound[4])
                        #time.sleep(0.1)                                     #G
                        #key_c.stop()
            
                if x >= 486.0:
                    if x < 560.0:
                        play_key(key_sound[5])
                        #time.sleep(0.1)                                     #A
                        #key_c.stop()
                    
                if x >= 561.0:
                    if x < 635.0:
                        play_key(key_sound[6])
                        #time.sleep(0.1)                                     #H
                        #key_c.stop()
                    
                if x >= 636.0:
                    if x < 710.0:
                        play_key(key_sound[7])
                        #pygame.mixer.Sound(key_c2).play()
                        #time.sleep(0.1)                                    #C2
                        #key_c.stop()
                        
                        
