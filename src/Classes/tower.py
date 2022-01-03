import pygame
import os

from logger import logger
from conf import *

class Tower():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.health = 1000

    def intersect(self):
        self.health -= 10
        if logger_intersect:
            logger.debug(f"ORK-INTERSECT-hero Ork did hit TOWER")