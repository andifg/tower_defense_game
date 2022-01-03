import pygame
import os
import random

from Classes.base import Base
from logger import logger
from conf import *


# stationary = pygame.image.load(os.path.join("src", "Assets" , "Hero","standing.png"))
ork_left = []
ork_right = []
ork_dying = []
ork_attacking = []
for picIndex in range(1,10):
    ork_right.append(pygame.image.load(os.path.join("src", "Assets" , "Orc", "RUN_0" + str(picIndex) + ".png")))
    ork_left.append(pygame.transform.scale(pygame.image.load(os.path.join("src" , "Assets", "Orc", "RUN_0" + str(picIndex) + ".png")),(ork_width,ork_height)))
    ork_dying.append(pygame.transform.scale(pygame.image.load(os.path.join("src" , "Assets", "Orc", "DIE_0" + str(picIndex) + ".png")),(ork_width,ork_height)))
    ork_attacking.append(pygame.transform.scale(pygame.image.load(os.path.join("src" , "Assets", "Orc", "ATT_0" + str(picIndex) + ".png")),(ork_width,ork_height)))


def processOrks(orks):
    if random.random() < 1 / 100 and len(orks) < 5:
    # if len(orks)==0:
        ork = Ork((win_width-50)*ork_move_factor, 280)
        orks.append(ork)

    for ork in orks:
        if ork.remove() or ork.dead:
            orks.remove(ork)
        ork.move_ork()
    return orks

class Ork():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.step_index = 0
        self.velvx = 8
        self.face_left  = True
        self.face_right = False
        self.health = 3
        self.dying = False
        self.dead = False
        self.attacking = False

    def move_ork (self):
        if self.face_left:
            self.x -= self.velvx
        else:
            self.x += self.velvx
        self.step_index += 1

    def intersect_object(self,object,type):
        if type == "bullet" and not self.dying:
            if (self.x//ork_move_factor + ork_distance_to_middle <= object.x <= (self.x//ork_move_factor + ork_width) and self.y <= object.y and object.y < (self.y + ork_height)):
                self.health -= 1
                if self.health == 0:
                    self.dying = True
                    self.step_index = 0
                object.intersect()
                if logger_intersect:
                    logger.debug(f"ORK-INTERSECT-{type} Ork x1: {self.x//ork_move_factor} | Object x1: {object.x}) | Ork x2 {self.x//ork_move_factor + ork_width} | Object x2: {object.x} | Ork y1: {self.y} | Object y1: {object.y} | Ork y2: {self.y + ork_height}")

        if type == "hero" and not self.dying:
            if (self.x//ork_move_factor + ork_distance_to_middle <= object.x <= (self.x//ork_move_factor + ork_width - 140) and self.y <= object.y and object.y < (self.y + ork_height)):
                if not self.attacking:
                    self.attacking = True
                    self.velvx = 0
                    self.step_index = 0
                if self.attacking and self.step_index == 21:
                    object.intersect()
                if logger_intersect:
                    logger.debug(f"ORK-INTERSECT-{type} Ork x1: {self.x//ork_move_factor} | Object x1: {object.x}) | Ork x2 {self.x//ork_move_factor + ork_width - 140} | Object x2: {object.x} | Ork y1: {self.y} | Object y1: {object.y} | Ork y2: {self.y + ork_height}")

        if type == "tower" and not self.dying:
            if (self.x//ork_move_factor <= object.x + tower_distance_intersect):
                if not self.attacking:
                    self.attacking = True
                    self.velvx = 0
                    self.step_index = 0
                if self.attacking and self.step_index == 21:
                    object.intersect()
                if logger_intersect:
                    logger.debug(f"ORK-INTERSECT-{type} Ork x1: {self.x//ork_move_factor} | Object x1: {object.x}) | Ork x2 {self.x//ork_move_factor + ork_width} | Object x2: {object.x} | Ork y1: {self.y} | Object y1: {object.y} | Ork y2: {self.y + ork_height}")



    def drawObject(self, win):
        if self.step_index >= 27:
            self.step_index = 0
        if self.dying:
            win.blit(ork_dying[self.step_index//3],(self.x//ork_move_factor,self.y))
            if self.step_index == 26:
                self.dead = True
        elif self.attacking:
            win.blit(ork_attacking[self.step_index//3],(self.x//ork_move_factor,self.y))
            if self.step_index == 26:
                self.attacking = False
                self.velvx = 10
        elif self.face_left:
            win.blit(ork_left[self.step_index//3],(self.x//ork_move_factor,self.y))
        elif self.face_right:
            win.blit(ork_right[self.step_index//3], (self.x//ork_move_factor, self.y))

    def remove(self):
        return not(self.x >= -300 and self.x//3 <= win_width + 50)