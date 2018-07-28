# -*- coding: cp1252 -*-
# windows 8     python 3.3      pygame_version 1.9.2pre

import pygame
from player import *
from enemy import *

level1=["bana1.txt","bana2.txt","bana3.txt","bana4.txt","bana5.txt","bana6.txt","bana7.txt","bana8.txt"]

class Tile(pygame.sprite.Sprite):
    #I den h�r classen skapas banan
    
    listaTile = pygame.sprite.Group()
    def __init__(self,tile):
        pygame.sprite.Sprite.__init__(self)
        if tile=="mark":
            self.image = pygame.image.load("tile.png").convert()
            self.rect = self.image.get_rect()
            self.time=50
            self.name=tile
        elif tile=="coin":
            self.image = pygame.image.load("coin.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.name=tile
            

    
    def skapabana(bana):
        #L�ser in infot fr�n text filen och l�gger det in i en lista
        try:
            ok=True
            lista=[]
            f=open(level1[bana],"r")
            tom="borjan"
            #L�sar en rad i tagen
            while tom!="":
                b=f.readline()
                tom=b
                x=0
                #H�r l�ser den radens karakt�rer och l�gger in det i en lista
                while x<len(b):
                    if b[x]=="#":
                        lista.append("#")
                        x+=1
                    elif b[x]=="\n":
                        x+=1
                        lista.append("\n")
                    elif b[x]=="p":
                        x+=1
                        lista.append("p")
                    elif b[x]=="f":
                        x+=1
                        lista.append("f")
                    elif b[x]=="e":
                        x+=1
                        lista.append("e")
                    elif b[x]=="@":
                        x+=1
                        lista.append("@")
                    elif b[x]=="c":
                        x+=1
                        lista.append("c")
                    elif b[x]=="d":
                        x+=1
                        lista.append("d")
                    elif b[x]=="z":
                        x+=1
                        lista.append("z")
                    elif b[x]=="b":
                        x+=1
                        lista.append("b")
                    else:
                        x+=1
                        lista.append(" ")
                        
            f.close()
            return lista
        except(ValueError):
            print("Blev n�got fel (class tile def skapabana)")

    
    def ritautbana(bana):
        #L�sar listan och skapar kordinaterna
        try:

            
            x=-30
            y=0
            spelforx=30
            spelfory=30
            listaTile = pygame.sprite.Group()
            listaSpelare = pygame.sprite.Group()
            listaEnemys = pygame.sprite.Group()
            listagolv=pygame.sprite.Group()
            listaCoin=pygame.sprite.Group()
            for i in Tile.skapabana(bana):
                 if i=="#":
                    #L�d tilen
                    ny=Tile("mark")
                    x+=30
                    ny.rect.x=x
                    ny.rect.y=y
                    listaTile.add(ny)
                   
                 elif i=="f":
                     #Spelarens kordinat n�r spelaren g�r till f�rreg�ende rum  
                     x+=30
                     spelforx=x
                     spelfory=y
                 elif i=="\n":
                    y+=30
                    x=-30
                 elif i==" ":
                    x+=30
                 
                 elif i=="p":
                     #Spelarens kordinat n�r spelaren kommer till n�sta rum   
                     x+=30
                     spelarex=x
                     spelarey=y
                 elif i=="@":
                    x+=30
                    golv=Tile("mark")
                    golv.rect.x=x
                    golv.rect.y=y
                    listagolv.add(golv)
                 elif i=="e":
                     #Fiende wizard
                     x+30
                     ny=Enemy("wizard",1,10,1)
                     ny.rect.x=x
                     ny.rect.y=y
                     listaEnemys.add(ny)
                 elif i=="d":
                     #Fiende badguy
                     x+30
                     ny=Enemy("badguy",1,50,1)
                     ny.rect.x=x
                     ny.rect.y=y
                     listaEnemys.add(ny)
                 elif i=="z":
                     #Fiende zombie
                     x+30
                     ny=Enemy("zombie",1,80,1)
                     ny.rect.x=x
                     ny.rect.y=y
                     listaEnemys.add(ny)
                 elif i=="b":
                     #Boss
                     x+30
                     ny=Enemy("boss",1,500,1)
                     ny.rect.x=x
                     ny.rect.y=y
                     listaEnemys.add(ny)
                 elif i=="c":
                     #pengar
                     x+30
                     ny=Tile("coin")
                     ny.rect.x=x
                     ny.rect.y=y
                     listaCoin.add(ny)
                    
                     
            yield listaTile
            yield spelarex
            yield spelarey
            yield spelforx
            yield spelfory
            yield listaEnemys
            yield listagolv
            yield listaCoin
        except(ValueError):
            print("n�got gick fel (class tile def ritautbana)")
                    
                





            
