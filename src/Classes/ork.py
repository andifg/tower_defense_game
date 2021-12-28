import pygame
import os
import random

from Classes.base import Base
from logger import logger
from conf import *


# stationary = pygame.image.load(os.path.join("src", "Assets" , "Hero","standing.png"))
ork_left = []
ork_right = []
for picIndex in range(1,10):
    ork_right.append(pygame.image.load(os.path.join("src", "Assets" , "Orc_1", "RUN_0" + str(picIndex) + ".png")))
    ork_left.append(pygame.transform.scale(pygame.image.load(os.path.join("src" , "Assets", "Orc_1", "RUN_0" + str(picIndex) + ".png")),(250,149)))


def processOrks(orks):
    # if random.random() < 50 / 100:
    if len(orks)==0:
        ork = Ork((win_width-50)*3, 500)
        orks.append(ork)

    for ork in orks:
        if ork.off_screen():
            orks.remove(ork)
        ork.move_ork()
    return orks

class Ork():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.step_index = 1
        self.velvx = 8
        self.face_left  = True
        self.face_right = False

    def move_ork (self):
        if self.face_left:
            self.x -= self.velvx
        else:
            self.x += self.velvx
        self.step_index += 1

    def drawObject(self, win):
        if self.step_index >= 27:
            self.step_index = 0
        if self.face_right:
            win.blit(ork_right[self.step_index//3], (self.x, self.y))
        else:
            win.blit(ork_left[self.step_index//3],(self.x//3,280))

    def off_screen(self):
        return not(self.x >= -300 and self.x//3 <= win_width + 50)