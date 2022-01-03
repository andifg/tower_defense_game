import pygame
import os

from Classes.base import Base
from logger import logger
from conf import bullet_height, bullet_width, logger_intersect

bullet =  pygame.transform.scale(pygame.image.load(os.path.join("src", "Assets" , "Bullets","light_bullet.png")),(bullet_width,bullet_height))


class Bullet(Base):
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.index = 10
        self.direction = direction
        self.delete = False

    def drawObject(self, win):
        win.blit(bullet, (self.x, self.y))


    def updateBullet (self):
        self.x += self.index * self.direction

    def intersect (self):
        if logger_intersect:
            logger.debug(f"ORK-INTERSECT-bullet Bullet did hit and will be deleted")
        self.delete = True
        self.index = 0
