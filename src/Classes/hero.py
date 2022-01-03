import pygame
import os

from Classes.bullet import Bullet
from Classes.base import Base
from logger import logger
from conf import *

stationary = pygame.image.load(os.path.join("src", "Assets" , "Hero","standing.png"))
left = []
right = []
for picIndex in range(1,10):
    right.append(pygame.image.load(os.path.join("src", "Assets" , "Hero", "R" + str(picIndex) + ".png")))
    left.append(pygame.image.load(os.path.join("src" , "Assets", "Hero", "L" + str(picIndex) + ".png")))

class Hero(Base):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velvx = 7
        self.velvy = 10
        self.face_right = False
        self.face_left  = False
        self.step_index = 0
        self.jump = False
        self.bullets = []
        self.cooldown = 0
        self.health = 100

    def move_hero (self, userInput):
        if userInput[pygame.K_RIGHT] and self.x < win_width - 40:
            self.x += self.velvx
            self.step_index += 1
            self.face_left = False
            self.face_right = True
        elif userInput[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velvx
            self.step_index += 1
            self.face_left = True
            self.face_right = False
        else:
            self.face_left = False
            self.face_right = False
            self.step_index = 0


    def jump_motion(self, userInput):

        if self.jump == False and userInput[pygame.K_SPACE]:
            self.jump = True

        if self.jump == True:
            self.y -= self.velvy*4
            self.velvy -= 1
            if self.velvy < -10:
                self.jump = False
                self.velvy = 10

    def drawObject(self, win):
        # win.blit(right[0], (250 ,250 ))
        if self.step_index >= 36:
            self.step_index = 0
        if self.face_right:
            win.blit(right[self.step_index//4], (self.x, self.y))
        elif self.face_left:
            win.blit(left[self.step_index//4], (self.x, self.y))
        else:
            win.blit(stationary, (self.x,self.y))

    def shoot(self, userInput):
        if logger_bullets:
            logger.debug("BULLETS "+ ''.join(str(a) for a in map(lambda x: {"X-Achse":x.x, "Y-Achse":x.y, "Direction": x.direction}, self.bullets)))

        if self.cooldown > 0:
            self.cooldown -= 1

        if userInput[pygame.K_f] and self.cooldown == 0:
            self.cooldown = 10
            if userInput[pygame.K_LEFT]:
                bullet = Bullet(self.x + 50, self.y + 20, -1)
                self.bullets.append(bullet)
            else:
                bullet = Bullet(self.x + 50, self.y + 20, 1)
                self.bullets.append(bullet)

        # Call function to process the movement of each bullet
        for bullet in self.bullets:
            if bullet.x > win_width or bullet.x <= 0 or bullet.delete:
                print(f"delete bullet {bullet.x}")
                self.bullets.remove(bullet)
                del bullet
            else:
                bullet.updateBullet()

    # Function to reduce Health
    def intersect(self):
        if logger_intersect:
            logger.debug(f"ORK-INTERSECT-hero Ork did hit HERO")