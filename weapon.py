# -*- coding: cp1252 -*-
# windows 8     python 3.3      pygame_version 1.9.2pre

import pygame


class weapon(pygame.sprite.Sprite):
     #H�r skapas vapnens skott
     def __init__(self,power,b):
          
          try:
               self.power=power
               self.rikt=b
               pygame.sprite.Sprite.__init__(self)
               self.image = pygame.image.load("vapen.png").convert()
               self.rect = self.image.get_rect()
          except:
               print("n�got gick fel")

     def move(self):
          #skottets riktning
          try:
              self.rect.x+=self.rikt
          except:
               print("n�got gick fel")

        
         
    
