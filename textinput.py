# -*- coding: cp1252 -*-
# windows 8     python 3.3      pygame_version 1.9.2pre


import pygame,sys
from pygame.locals import *


class TextInput():
    #I den h�r classen skapas textinput n�r man har klarat banan och ska skriva namn till sin highscore
    def input(time,points):
        black=(0,0,0)
        red=(250,0,0)
        print(time,points)
        
        
            
        pygame.init()
        namn=""
        screen=pygame.display.set_mode((640,480),0,32)
        background=pygame.image.load("ba.jpg").convert()
        screen.blit(background,(0,0))
        font = pygame.font.Font(None, 30)
        text=font.render("Skriv namn: ",True,black)
        screen.blit(text,[150,150])
        font2 = pygame.font.Font(None, 30)
        loop=True
        
        while loop:
            
            
            for event in pygame.event.get():
                #knappar
                    if event.type==QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYDOWN:
                        if event.key==K_a:
                            namn+="a"
                        elif event.key==K_b:
                            namn+="b"
                        elif event.key==K_c:
                            namn+="c"
                        elif event.key==K_d:
                            namn+="d"
                        elif event.key==K_e:
                            namn+="e"
                        elif event.key==K_f:
                            namn+="f"
                        elif event.key==K_g:
                            namn+="g"
                        elif event.key==K_h:
                            namn+="h"
                        elif event.key==K_i:
                            namn+="i"
                        elif event.key==K_j:
                            namn+="j"
                        elif event.key==K_k:
                            namn+="k"
                        elif event.key==K_l:
                            namn+="l"
                        elif event.key==K_m:
                            namn+="m"
                        elif event.key==K_n:
                            namn+="n"
                        elif event.key==K_o:
                            namn+="o"
                        elif event.key==K_p:
                            namn+="p"
                        elif event.key==K_q:
                            namn+="q"
                        elif event.key==K_r:
                            namn+="r"
                        elif event.key==K_s:
                            namn+="s"
                        elif event.key==K_t:
                            namn+="t"
                        elif event.key==K_y:
                            namn+="y"
                        elif event.key==K_v:
                            namn+="v"
                        elif event.key==K_w:
                            namn+="w"
                        elif event.key==K_x:
                            namn+="x"
                        elif event.key==K_y:
                            namn+="y"
                        elif event.key==K_z:
                            namn+="z"
                        elif event.key==K_u:
                            namn+="u"
                        elif event.key==K_RETURN:
                            textFile=open("highscore.txt","a")
                            temp=namn+" "+str(points)+" "+str(time)+"\n"
                            textFile.write(temp)
                            textFile.close()
                            loop=False
                            
                            
                            
                            
            text2=font2.render(namn,True,black)
            screen.blit(text2,[350,150])

                        
                            
            pygame.display.flip()

