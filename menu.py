# -*- coding: cp1252 -*-
# windows 8     python 3.3      pygame_version 1.9.2pre


import pygame,sys
from pygame.locals import *
from spel import *

class Menu():

 
    def update(valen,nasta):
        #updaterar sk�rmen
        global lista#vilken lista som skrivs ut p� mennu sk�rmen
        global banor
        global bac
        global tillbaka
        global val
        global highScoreLista
        try:
            #H�r om man trycker p� enter
            if(lista[valen]=="Bana 1"and nasta==True):
                #spelet startas
                main.spel()
            elif(lista[valen]=="Start Game" and nasta==True):
                lista=banor
                val=0
                valen=0
            elif(lista[valen]=="Highscore" and nasta==True):
                lista=highScoreLista
                val=0
                valen=0
            elif(lista[valen]=="Instructions" and nasta==True):
                lista=tillbaka
                val=0
                valen=0
            elif(lista[valen]=="tillbaka"and nasta==True):
                lista=menu
                val=0
                valen=0
            elif(lista==highScoreLista and nasta==True):
                lista=menu
                val=0
                valen=0
                
            elif(lista[valen]=="Quit"and nasta==True):
                pygame.quit()
                sys.exit()
        except:
            print("N�got gick snett(class menu def update)")
        try:
            #h�r om man trycket up eller ner knapparna, d� �ndras f�rgen
            font = pygame.font.Font(None, 55)
            if lista!=tillbaka and lista!=highScoreLista:
                screen.blit(background,(0,0))
                height=140
                for i in lista:
                     if(lista.index(i)==valen):
                         text=font.render(i,True,red)  
                         screen.blit(text,[200,height])
                         height+=50
                     else:
                         text=font.render(i,True,black)  
                         screen.blit(text,[200,height])
                         height+=50
            elif lista==tillbaka:
                screen.blit(bac,(0,0))
                for i in lista:
                    text1=font.render(i,True,red)
                    screen.blit(text1,[150,340])
            elif lista==highScoreLista:
                #skriver ut highscore och sorterar den efter po�ng
                screen.blit(background,(0,0))
                highScoreLista.sort(key=lambda highScoreLista: int(highScoreLista[1]),reverse=True)
                screen.blit(background,(0,0))
                t1=font.render("Name",True,black)
                screen.blit(t1,[145,100])
                t2=font.render("Score",True,black)
                screen.blit(t2,[295,100])
                t3=font.render("Time",True,black)
                screen.blit(t3,[480,100])
                height=140
                t4=font.render("tillbaka",True,red)
                screen.blit(t4,[130,380])
                del highScoreLista[10:]
                for i in lista:
                    font = pygame.font.Font(None, 30)
                    text1=font.render(i[0],True,black)
                    screen.blit(text1,[150,height])
                    text2=font.render(i[1],True,black)
                    screen.blit(text2,[320,height])
                    text3=font.render(i[2],True,black)
                    screen.blit(text3,[490,height])
                    height+=19
        except:
               print("n�got gick snett class menu def update 2")


    def highScore():
        #laddar in highscore i en lista
        global highScoreLista
        
        try:
            textFile=open("highscore.txt","r")
            lines=textFile.readlines()
            for i in lines:
                if(len(i)==1):
                    pass
                else:
                    b=i.split()
                    highScoreLista.append(b)
            textFile.close()
            
        except(IOError):
               print("Det gick inte att �ppna textfilen (class menu def highscore)" )
        
            
        

    def men():
        try:
            #laddar in grafik och annat
            global screen
            global menu
            global background
            global black
            global red
            global banor
            global sida
            global lista
            global bac
            global tillbaka
            global val
            global highScoreLista
            highScoreLista=[]
            sida=""
            black=(0,0,0)
            red=(250,0,0)
            pygame.init()
            screen=pygame.display.set_mode((640,480),0,32)
            background=pygame.image.load("ba.jpg").convert()
            bac=pygame.image.load("bab.jpg").convert()
            screen.blit(background,(0,0))
            font = pygame.font.Font(None, 55)
            menu=("Start Game","Highscore","Instructions","Quit")
            banor=("Bana 1","tillbaka")
            tillbaka=("tillbaka","tillbaka")
            val=0
            height=140
            lista=menu
            Menu.update(val,False)
            Menu.highScore()
                     

            while True:#menu loopen
                #knappar
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYDOWN:
                        if event.key==K_DOWN:
                            if val>=len(lista)-1:
                                val=len(lista)-1
                            else:
                                val+=1
                                Menu.update(val,False)
                        elif event.key==K_UP:
                            if val<=0:
                                val=0
                            else:
                                val-=1
                                Menu.update(val,False)
                        elif event.key==K_RETURN:
                            Menu.update(val,True)
                        elif event.type==K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                pygame.display.flip()
        except(ValueError):
            print("n�got gick snett(class menu def men)")

Menu.men()
