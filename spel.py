# -*- coding: cp1252 -*-
# windows 8     python 3.3      pygame_version 1.9.2pre


import pygame,sys
from player import *
from Tile import *
from textinput import *
from pygame.locals import *
from weapon import *
pygame.mixer.init(44100, -16, 2, 1024)


class main():
   

    def updategame():
        #Updaterar spelet
        try:
            global oldx
            global oldy
            global highScore
            global countDown
            global nr2
            global tid
            global listaEnemyBeam
            global gameOver
            global bana
            global sekund1
            global sekund2
            global minut1
            global minut2
            
            if movement!=0 and hoppa==True:
                    walk.play()
                    
            oldx=spelare.rect.x
            oldy=spelare.rect.y
            screen.blit(background,(0,0))
            spelare.move(movement) #Spelarens riktning n�r den g�r
            lista.draw(screen)
            listaEnemys.draw(screen)
            listaGolv.draw(screen)
            listaTile.draw(screen)
            listaCoin.draw(screen)
            listaEnemyBeam=None
            listaEnemyBeam=Enemy.getLista()
            
            if(bana==7 and len(listaEnemys)==0):
                #man har klarat spelet h�r
                tiden=str(minut2)+str(minut1)+":"+str(sekund2)+str(sekund1)
                TextInput.input(tiden,highScore)
                gameOver=False
                
            if listabeam!=None:
                    listabeam.draw(screen)
                    for i in listabeam:
                        i.move()
                        
            if listaEnemyBeam!=None:
                listaEnemyBeam.draw(screen)
                for iv in listaEnemyBeam:
                    iv.move()
                    main.collideBeamSpelare(iv,spelare)
                    main.collidebeam(iv,listaGolv,listaTile)
                    
            font=pygame.font.SysFont('Arial black',30)
            text=font.render("Life",True,(0,0,0))
            screen.blit(text,[0,0])


            font2=pygame.font.SysFont('Arial black',30)
            text2=font2.render("Score "+str(highScore),True,(0,0,0))
            screen.blit(text2,[500,0])
            main.klocka()

            for ii in listabeam:
                main.collidebeam(ii,listaTile,listaGolv)
                for i in listaEnemys:
                    main.collidebeamenemy(ii,i)
                    
            for i in listaEnemys:
                main.collidespelareenemy(spelare,i)
                main.gravity(i)
                main.collideenemy(i,listaTile)
                main.collidegolv(i,listaGolv)
                i.move()
                i.freeze(spelare.rect.x,spelare.rect.y)
                if(i.ljud==True and i.name=="badguy"):
                    gunFire.play()
                    i.ljud=False
                elif(i.ljudCome==1 and i.name=="badguy"):
                    come.play()

            if(tid==nr2 and countDown>0):
                countDown-=1
                nr2+=1
            elif(countDown >0):
                text=font.render("Game begins in "+str(countDown),True,(0,0,0))
                screen.blit(text,[400,400])
                    
            pygame.draw.rect(screen,(255,2,5),[70,10,spelare.life,25])           
            pygame.display.flip()
        except:
            print("n�got gick snett class spel def updategame")
            


    def collidebeam(self,lista1,lista2):
        try:
            #Om vapnens skott tr�ffar en v�gg eller hinder d� d�r skottet
            if pygame.sprite.spritecollide(self,lista1,False) or pygame.sprite.spritecollide(self,lista2,False):
                shootTile.play()
                self.kill()
        except:
            print("n�got gick snett class spel def collidebeam")
    def collideCoin(self,lista1):
        try:    
            global highScore
            #Om vapnens skott tr�ffar en v�gg eller hinder d� d�r skottet
            if pygame.sprite.spritecollide(self,lista1,True):
                highScore+=5
                cash.play()
        except:
            print("n�got gick snett class spel def collidecoin")

        

    def collidebeamenemy(beam,enemy):
        try:
            global highScore
            #om vapnens skott tr�ffar fienden eller 
            if pygame.sprite.collide_rect(beam, enemy) == True:
                enemyShoot.play()
                enemy.life+=-beam.power
                highScore+=beam.power
                if(enemy.life<=0):
                    #Fienden d�r
                    enemy.kill()
                    beam.kill()
                else:
                    beam.kill()
        except:
            print("n�got gick snett class spel def collidebeamenemy")

    def collideBeamSpelare(beam,spelare):
        try:
            global highScore
            #om vapnens skott tr�ffar spelare 
            if pygame.sprite.collide_rect(beam, spelare) == True:
                spelare.life+=-beam.power
                beam.kill()
        except:
            print("n�got gick snett class spel def collideBeamSpelare")
           
                
    def collidespelareenemy(spelare,enemy):
        try: 
            global traff
            global blinka
            global gameOver
            if(traff+5000<pygame.time.get_ticks()):
                #om spelaren tr�ffar fienden
                if pygame.sprite.collide_rect(enemy, spelare) == True:
                    if(enemy.name=="zombie" and spelare.life>0):
                        spelare.life-=1
                        enemy.life+=1

                    elif(enemy.name!="zombie"):
                        blinka=True
                        traff=pygame.time.get_ticks()
                        spelare.life+=-enemy.power-100
                    elif(spelare.life<=0):
                        #Spelaren d�r
                        gameOver=False
                        womenScream.play()
                        screen=pygame.display.set_mode((640,480),0,32)
                        pygame.mixer.music.stop()
        except:
            print("n�got gick snett class spel def collidespelareenemy")

     

    def collidegolv(enemy,lista2):
        #s� att fienden kan g� p� marken
        try:
            if pygame.sprite.spritecollide(enemy,lista2,False,False):
                enemy.rect.y-=1
        except:
            print("n�got gick snett class spel def collidegolv")


    def collideenemy(enemy,lista2):
        #s� att fienden studsar n�r den tr�ffar en v�gg
        try:
             if pygame.sprite.spritecollide(enemy, lista2, False):
                if enemy.numb==1:
                    enemy.speed(-1,True)
                elif enemy.numb==-1:
                    enemy.speed(1,False)
        except:
            print("n�got gick snett class spel def collideenemy")
            

    def collide(self,lista1,lista2):
        try:
             global hoppa
             #S� att den inte kan g� genom hinder
             if pygame.sprite.groupcollide(lista1,lista2,False,False):
                spelare.rect.x=oldx
             #S� att den kan g� p� hinder
             if pygame.sprite.groupcollide(lista1,lista2,False,False):
                spelare.rect.y=oldy-1
                hoppa=True
        except:
            print("n�got gick snett class spel def collide")
                 
    def collidetile(self,lista1,lista2):
        #S� att den inte kan g� genom hinder
        try:
             if pygame.sprite.groupcollide(lista1,lista2,False,False):
                spelare.rect.x=oldx
        except:
            print("n�got gick snett class spel def collidetile")
                     
            
    def klocka():
        #Tid
        try:
            global sekund1
            global sekund2
            global minut1
            global minut2
            global nr
            global tid
            global gameBegin
            tid=pygame.time.get_ticks()//1000
            if(tid==nr):
                gameBegin=True
                sekund1+=1
                nr+=1
            if(sekund1==10):
                sekund2+=1
                sekund1=0
            elif(sekund2==6):
                minut1+=1
                sekund2=0
            elif(minut1==10):
                minut2+=1
                minut1=0
            font2=pygame.font.SysFont('Arial black',30)
            text2=font2.render(str(minut2)+str(minut1)+":"+str(sekund2)+str(sekund1),True,(0,0,0))
            screen.blit(text2,[700,0])
        except:
            print("n�got gick snett class spel def klocka")

    def gravity(self):
        #S� att spelaren och fienden f�r gravitation
        try:
             if self.rect.y<1000: 
                self.rect.y+=1
        except:
            print("n�got gick snett class spel def gravity")

    def rum(spelarepos):
        #S� att spelaren kan g� till n�sta/f�rrg�ende rum
        try:
            
             global spelare
             global lista
             global listaEnemys
             global listaTile
             global bana
             global listaGolv
             global listabeam
             global listaCoin
             global listaEnemyBeam
             #g�r till n�sta rum
             if(spelarepos>1020):
                 listabeam.empty()
                 listaEnemyBeam.empty()
                 bana+=1
                 listaTile, spelarex,spelarey,r,g,listaEnemys,listaGolv,listaCoin = Tile.ritautbana(bana)
                 spelare.rect.x=spelarex
                 spelare.rect.y=spelarey
             #G�r till f�rreg�ende rum    
             elif(spelarepos<0):
                listabeam.empty()
                listaEnemyBeam.empty()
                bana-=1
                listaTile,x,y,xx,yy,listaEnemys,listaGolv,listaCoin= Tile.ritautbana(bana)
                spelare.rect.x=xx
                spelare.rect.y=yy
        except:
            print("n�got gick snett class spel def rum")


    def spel():
        try: 
            global hoppa
            global spelare
            global oldx
            global oldy
            global screen
            global background
            global movement
            global lista
            global listaEnemys
            global listaTile
            global bana
            global listaGolv
            global hoppa
            global listabeam
            global knapp
            global walk
            global shootTile
            global enemyShoot
            global womenScream
            global traff
            global highScore
            global nr
            global sekund1
            global sekund2
            global minut1
            global minut2
            global blinka
            global tid
            global temp
            global gameOver
            global gameBegin
            global listaCoin
            global gunFire
            global come
            global cash
            global countDown
            global nr2
            global listaEnemyBeam
            listaEnemyBeam.empty()
            gameBegin=False
            gameOver=True
            tid=pygame.time.get_ticks()//1000
            blinka=False
            sekund1=0
            sekund2=0
            minut1=0
            minut2=0
            nr=tid+7
            nr2=tid+1
            highScore=0
            traff=0
            nytid=0
            pygame.init()
            bana=0;
            movement=0
            hoppa=True
            knapp="left"
            countDown=6
            clock = pygame.time.Clock()

            
            #laddar in grafik, ljud och sparar in saker i olika sprite.groups
            screen=pygame.display.set_mode((1024,768),0,32)
            background=pygame.image.load("back.jpg").convert()
            so=pygame.mixer.Sound("jump3.wav")
            walk=pygame.mixer.Sound("walk.wav")
            count=pygame.mixer.Sound("count.wav")
            pygame.mixer.music.load("happywalk.mp3")
            shoot=pygame.mixer.Sound("vap.wav")
            shootTile=pygame.mixer.Sound("vaptile.wav")
            enemyShoot=pygame.mixer.Sound("enemy1.wav")
            womenScream=pygame.mixer.Sound("woscre.wav")
            gunFire=pygame.mixer.Sound("gunfire.wav")
            come=pygame.mixer.Sound("hello.wav")
            cash=pygame.mixer.Sound("cash.wav")
            pygame.mixer.music.play(-1)
            lista = pygame.sprite.Group()
            listabeam=pygame.sprite.Group()
            listaTile, spelarex,spelarey,forx,fory,listaEnemys,listaGolv,listaCoin = Tile.ritautbana(bana)
            spelare=Player(410)
            spelare.rect.x=spelarex
            spelare.rect.y=spelarey
            lista.add(spelare)
            imageleft= pygame.image.load("gal.png").convert_alpha()
            imageright= pygame.image.load("g1.png").convert_alpha()
            imageshootr=pygame.image.load("gaa.png").convert_alpha()
            imageshootl=pygame.image.load("gar.png").convert_alpha()
            imagejumpr=pygame.image.load("galh.png").convert_alpha()
            imagejumpl=pygame.image.load("ghr.png").convert_alpha()
            imagetom=pygame.image.load("tom.png").convert_alpha()
            count.play()
            font=pygame.font.SysFont('Arial black',30)
        except:
            print("n�got gick snett class spel def spel")

            
        while gameOver!=False:#Spel loopen
            try:
                            

                #Knappar
                if(gameBegin==True):    
                    for event in pygame.event.get():
                        if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type==KEYDOWN:
                            if event.key==K_ESCAPE:
                                #avslutar spelet
                                pygame.quit()
                                sys.exit()
                            elif event.key==K_RIGHT:
                                #styrning
                                spelare.image=imageright
                                movement=2
                                knapp="right"
                            elif event.key==K_LEFT:
                                #styrning
                                spelare.image= imageleft
                                movement=-2
                                knapp="left"
                            elif event.key==K_SPACE:
                                #Spelaren skjuter
                                shoot.play()
                                if(knapp=="right"):
                                    #Spelaren skjuter till h�ger
                                    spelare.image=imageshootr
                                    beam=weapon(5,3)
                                    beamy=spelare.rect.y+42
                                    beamx=spelare.rect.x+20
                                    beam.rect.y=beamy
                                    beam.rect.x=beamx
                                    listabeam.add(beam)
                                elif(knapp=="left"):
                                    #Spelaren skjuter till v�nster
                                    spelare.image= imageshootl
                                    beam=weapon(5,-3)
                                    beamy=spelare.rect.y+42
                                    beamx=spelare.rect.x-20
                                    beam.rect.y=beamy
                                    beam.rect.x=beamx
                                    listabeam.add(beam)
                            elif event.key==K_UP:
                                main.updategame()
                                x=0
                                if hoppa:
                                    if(knapp=="left"):
                                        spelare.image= imagejumpr
                                        hoppa=False#S� att gubben inte kan hoppa n�r den �r i luften
                                        so.play()
                                    elif(knapp=="right"):
                                        spelare.image= imagejumpl
                                        hoppa=False#S� att gubben inte kan hoppa n�r den �r i luften
                                        so.play()
                                    while x<40:
                                        #S� att spelaren inte kan hoppa genom en v�gg
                                        if pygame.sprite.groupcollide(lista,listaGolv,False,False)or pygame.sprite.groupcollide(lista,listaTile,False,False):
                                            spelare.rect.x=oldx
                                            spelare.rect.y=oldy+5
                                            x=55
                                            main.updategame()
                                        else:
                                            #H�r hoppar spelaren
                                            spelare.rect.y-=4
                                            for i in listaEnemys:
                                                main.gravity(i)
                                                main.collideenemy(i,listaTile)
                                                main.collidegolv(i,listaGolv)
                                                i.move()
                                                i.freeze(spelare.rect.x,spelare.rect.y)
                                            oldx=spelare.rect.x
                                            oldy=spelare.rect.y
                                            x+=1
                                            main.updategame()
                                            pygame.display.flip()
                        if event.type==KEYUP:
                            if(knapp=="left"):
                                spelare.image= imageleft
                            elif(knapp=="right"):
                                spelare.image= imageright
                            movement=0
           
                #Om spelaren blir tr�ffad av en fiende d� kommer spelarens bild att blinka i 2 sekunder.
                if blinka and  traff+2000>pygame.time.get_ticks() and nytid+20<pygame.time.get_ticks():
                    nytid=pygame.time.get_ticks()
                    spelare.image=imagetom
                elif blinka and traff+2000>pygame.time.get_ticks():
                    if(knapp=="left"):
                        spelare.image= imageleft
                    elif(knapp=="right"):
                        spelare.image=imageright
                elif traff+2000<pygame.time.get_ticks() and blinka==True:
                    blinka=False
                    if(knapp=="left"):
                        spelare.image= imageleft
                    elif(knapp=="right"):
                        spelare.image=imageright
                    
                clock.tick(90)
                main.gravity(spelare)
                main.collideCoin(spelare,listaCoin)

                
                if(spelare.life<1):
                    screen=pygame.display.set_mode((640,480),0,32)
                    gameOver=False

                    
                main.collide(spelare,lista,listaGolv)
                main.collidetile(spelare,lista,listaTile)
                main.rum(spelare.rect.x)
                main.updategame()

            except(ValueError):                       
                print("n�got gick snett class spel def spel2")
                


