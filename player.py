# -*- coding: cp1252 -*-
# windows 8     python 3.3      pygame_version 1.9.2pre

import pygame

class Player(pygame.sprite.Sprite):
    #I dne h�r classen skapas spelaren
    try:
        global bilder1
        global bilder2
        global senaste
        senaste=0
        bilder1=["gl1.png","gl2.png","gl3.png","gl4.png","gl5.png","gl6.png","gl7.png","gl8.png"]
        bilder2=["g1.png","g2.png","g3.png","g4.png","g5.png","g6.png","g7.png","g8.png"]
    except:
        print("N�got gick snett class player b�rjan")
    def __init__(self,life):
        try:
            
            self.life=life
            self.bild=0
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("ga.png").convert_alpha()
            self.rect = self.image.get_rect()
        except:
            print("n�got gick snett(class player kunstruktor)")

    def move(self,b):
        #spelarens riktning n�r den g�r
        try:
            global bilder1
            global bilder2
            global tid
            tid=pygame.time.get_ticks()
            
            if(b==0):
                self.rect.x+=b
            elif(b==-2):
                self.rect.x+=b
                Player.nastaBild(self,bilder1)
            elif(b==2):
                self.rect.x+=b
                Player.nastaBild(self,bilder2)
        except:
            print("n�got gick snett class player def move")

    def nastaBild(self,bild):
        #Skapas ny bild n�r den g�r f�r att f� en fin animation
        try:
            global bilder1
            global bilder2
            global senaste
            global tid
            
            if(tid>senaste):
                senaste=tid+70
                self.image = pygame.image.load(bild[self.bild]).convert_alpha()
                self.bild+=1
                if(self.bild==8):
                    self.bild=0
        except:
            print("n�got gick snett class player def nasta")


        
            

    


        


   
            
       
            
            
   
        
        
        
       
            
       
        
        


  
            
