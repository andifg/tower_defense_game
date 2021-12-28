import pygame
import os

from Classes.base import Base
from logger import logger

bullet =  pygame.transform.scale(pygame.image.load(os.path.join("src", "Assets" , "Bullets","light_bullet.png")),(7,7))


class Bullet(Base):
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.index = 15
        self.direction = direction

    def drawObject(self, win):
        win.blit(bullet, (self.x, self.y))


    def updateBullet (self):
        self.x += self.index * self.direction
