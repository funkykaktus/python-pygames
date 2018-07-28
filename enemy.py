# -*- coding: cp1252 -*-
# Sami Kaleem 881217
# windows 8     python 3.3      pygame_version 1.9.2pre

import pygame
from weapon import *

class Enemy(pygame.sprite.Sprite):
    global listaBild1
    global listaBild2
    global listaZombie1
    global listaZombie2
    global listan
    global listaEnemyBeam
    global listaBoss1
    global listaBoss2
    listaEnemyBeam=pygame.sprite.Group()
    listaBild1=("bad.png","bad2.png","bad3.png","bad4.png","bad5.png","bad6.png")
    listaBild2=("badl1.png","badl2.png","badl3.png","badl4.png","badl5.png","badl6.png")
    listaZombie1=("zombie1.png","zombie2.png","zombie3.png","zombie4.png")
    listaZombie2=("zombier1.png","zombier2.png","zombier3.png","zombier4.png")
    listaBoss2=("boss.png","boss2.png","boss3.png","boss4.png","boss5.png","boss6.png","boss7.png")
    listaBoss1=("bossl1.png","bossl2.png","bossl3.png","bossl4.png","bossl5.png","bossl6.png","bossl7.png")
    
    def __init__(self,name,numb,life,power):
       
        try:
            pygame.sprite.Sprite.__init__(self)
            if name=="wizard":
                self.name=name
                self.numb=numb
                self.life=life
                self.power=power
                self.ljud=False
                self.ljudStop=False
                self.ljudCome=0
                self.image = pygame.image.load("wiz.png").convert_alpha()
                self.rect = self.image.get_rect()
            elif name=="badguy":
                self.numb=numb
                self.name=name
                self.life=life
                self.power=power
                self.bild=0
                self.tid=15
                self.tid2=0
                self.walk=0
                self.wait=20
                self.wait2=0
                self.bo=True
                self.ljud=False
                self.ljudCome=0
                self.image = pygame.image.load("bad.png").convert_alpha()
                self.rect = self.image.get_rect()
            elif name=="zombie":
                self.numb=numb
                self.name=name
                self.life=life
                self.power=power
                self.bild=0
                self.tid=15
                self.tid2=0
                self.walk=0
                self.wait=20
                self.wait2=0
                self.bo=True
                self.ljud=False
                self.ljudCome=0
                self.image = pygame.image.load("zombie1.png").convert_alpha()
                self.rect = self.image.get_rect()
            elif name=="boss":
                self.numb=numb
                self.name=name
                self.life=life
                self.power=power
                self.bild=0
                self.tid=15
                self.tid2=0
                self.walk=0
                self.wait=20
                self.wait2=0
                self.bo=True
                self.ljud=False
                self.ljudCome=0
                self.image = pygame.image.load("boss.png").convert_alpha()
                self.rect = self.image.get_rect()
                
        except:
               print("något gick snett (class enemy konstruktor)")

    def speed(self,numb,boo):
        #Fiendens hastighet
        try:
            if(self.name=="badguy" or self.name=="zombie"):
                if(boo==True):
                    self.numb=-1
                else:
                    self.numb=1
            elif(self.name=="wizard" or self.name=="boss"):
                self.numb=numb
        except:
            print("något gick snett class enemy def speed")


    def freeze(self,spelarposx,spelarposy):
        try:
              if(self.name=="badguy"):
                  #Om spelaren är inom den här avståndet då siktar fienden vapnet mot spelaren
                  if(self.rect.x+350>spelarposx and self.rect.x<spelarposx and self.rect.y-30<spelarposy and self.rect.y+30>spelarposy):
                      self.image = pygame.image.load("badrs.png").convert_alpha()
                      self.numb=0
                      self.bo=True
                      self.wait2+=1
                      self.ljudCome+=1
                      if(self.rect.x+200>spelarposx and self.wait<self.wait2):
                          #om spelaren är inom den här avståndet då skjuter fienden
                          self.wait2=0
                          Enemy.shoot(self,3,49)
                          self.ljud=True
                          self.ljudStop=False
                      elif(self.rect.x-350<spelarposx and self.wait<self.wait2 and self.life<50 ):
                          
                          
                          #om spelaren är inom den här avståndet då skjuter fienden
                          self.wait2=0
                          Enemy.shoot(self,3,32)
                          self.ljud=True
                          self.ljudCome+=1
                  elif(self.rect.x-350<spelarposx and self.rect.x>spelarposx and self.rect.y-30<spelarposy and self.rect.y+30>spelarposy):
                       #Om spelaren är inom den här avståndet då siktar fienden vapnet mot spelaren
                       self.image = pygame.image.load("badls.png").convert_alpha()
                       self.numb=0
                       self.bo=True
                       self.wait2+=1
                       self.ljudCome+=1
                       if(self.rect.x-200<spelarposx and self.wait<self.wait2 ):
                           #om spelaren är inom den här avståndet då skjuter fienden
                           self.wait2=0
                           Enemy.shoot(self,-3,-32)
                           self.ljud=True
                           self.ljudCome+=1
                       elif(self.rect.x-350<spelarposx and self.wait<self.wait2 and self.life<50 ):
                           #om spelaren är inom den här avståndet då skjuter fienden
                           self.wait2=0
                           Enemy.shoot(self,-3,-32)
                           self.ljud=True
                           self.ljudCome+=1
                           
                  elif(self.bo==True):
                      self.bo=False
                      self.numb=1
                  else:
                      self.ljudCome=0
              elif(self.name=="zombie"):
                  #Om spelaren är inom den här avståndet 
                  if(self.rect.x+350>spelarposx and self.rect.x<spelarposx and self.rect.y-30<spelarposy and self.rect.y+30>spelarposy):
                      self.numb=1
                      self.bo=True
                      self.wait2+=1
                      #self.ljudCome+=1
                  elif(self.rect.x-350<spelarposx and self.rect.x>spelarposx and self.rect.y-30<spelarposy and self.rect.y+30>spelarposy):
                       #Om spelaren är inom den här avståndet då 
                       self.numb=-1
                       self.bo=True
                       self.wait2+=1
                       #self.ljudCome+=1
                  elif(self.bo==True):
                      self.bo=False
                      self.numb=1
              elif(self.name=="boss"):
                   if(self.rect.x+3500>spelarposx and self.rect.x<spelarposx and self.rect.y-20<spelarposy and self.rect.y+20>spelarposy):
                      self.image = pygame.image.load("bossfastr.png").convert_alpha()
                      self.rect.y-=1
                      self.numb=2
                      self.bo=True
                      self.wait2+=1
                      #self.ljudCome+=1
                   elif(self.rect.x-3500<spelarposx and self.rect.x>spelarposx and self.rect.y-20<spelarposy and self.rect.y+20>spelarposy):
                      #Om spelaren är inom den här avståndet då
                      self.image = pygame.image.load("bossfast.png").convert_alpha()
                      self.rect.y-=1
                      self.numb=-2
                      self.bo=True
                      self.wait2+=1
                      #self.ljudCome+=1
                   elif(self.rect.y<spelarposy-50):
                       self.numb=1
                       if(self.rect.x>810):
                           self.image = pygame.image.load("bosshoover2.png").convert_alpha()
                           self.numb=0
                   elif(self.rect.y>spelarposy):
                       self.numb=1
                       if(self.rect.x>810):
                           self.image = pygame.image.load("bosshoover2.png").convert_alpha()
                           self.numb=0
                           self.rect.y-=2
                       
                   elif(self.bo==True):
                      self.bo=False
                      self.numb=1
                  

               
                      
        except:
            print("något gick snett (class enemy def freeze)")
    

    

    def shoot(self,rikt,b):
        try:
            #Skjuter skott
            global listaEnemyBeam 
            beam=weapon(5,rikt)
            beamy=self.rect.y+22
            beamx=self.rect.x+b
            beam.rect.y=beamy
            beam.rect.x=beamx
            listaEnemyBeam.add(beam)
        except:
            print("något gick fel (class enemy def shoot)")

    def getLista():
        global listaEnemyBeam
        return listaEnemyBeam
             
        


    def move(self):
        try:
            #Vilken riktning fienden går
            if(self.name=="badguy"):
                #Går ett antal steg sen vänder
                Enemy.nastaBild(self)
                self.walk+=self.numb
                if(self.walk>300):
                    self.walk=0
                    self.numb=-1
                elif(self.walk<-300):
                    self.walk=0
                    self.numb=1
            elif(self.name=="zombie"):
                Enemy.nastaBild(self)
                self.walk+=self.numb
                if(self.walk>300):
                    self.walk=0
                    self.numb=-1
                elif(self.walk<-300):
                    self.walk=0
                    self.numb=1
            elif(self.name=="boss"):
                Enemy.nastaBild(self)
                self.walk+=self.numb
                if(self.walk>800):
                    self.walk=0
                    self.numb=-1
                elif(self.walk<-800):
                    self.walk=0
                    self.numb=1
            elif(self.name=="wizard"):
                pass
            self.rect.x+=self.numb
        except(ValueError):
            print("något gick fel (class enemy def move)")
                
    def nastaBild(self):
        try:
            
            #Det gör så att det blir en animation när den går
            self.tid2+=1
            if(self.name=="badguy"):
                if(self.tid<self.tid2):
                     self.tid2=0
                     if(self.numb==-1):#Ändrar bild när den går till vänster
                         self.image = pygame.image.load(listaBild2[self.bild]).convert_alpha()
                     elif(self.numb==1):#Ändrar bild när den går till höger
                         self.image = pygame.image.load(listaBild1[self.bild]).convert_alpha()
                     self.bild+=1
                     if(self.bild==6):
                         self.bild=0
            elif(self.name=="zombie"):
                if(self.tid<self.tid2):
                     self.tid2=0
                     if(self.numb==-1):#Ändrar bild när den går till vänster
                         self.image = pygame.image.load(listaZombie1[self.bild]).convert_alpha()
                     elif(self.numb==1):#Ändrar bild när den går till höger
                         self.image = pygame.image.load(listaZombie2[self.bild]).convert_alpha()
                     self.bild+=1
                     if(self.bild==3):
                         self.bild=0
            elif(self.name=="boss"):
                if(self.tid<self.tid2):
                     self.tid2=0
                     if(self.numb==-1):#Ändrar bild när den går till vänster
                         self.image = pygame.image.load(listaBoss1[self.bild]).convert_alpha()
                     elif(self.numb==1):#Ändrar bild när den går till höger
                         self.image = pygame.image.load(listaBoss2[self.bild]).convert_alpha()
                     self.bild+=1
                     if(self.bild==6):
                         self.bild=0
        except:
            print("något gick fel (class enemy def nastaBild)")


        
