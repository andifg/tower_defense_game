import pygame
import os
import random

# Load Classes
from Classes.hero import Hero
from Classes.bullet import Bullet
from Classes.tower import Tower
from Classes.ork import Ork
from conf import win_width,win_height,tower_width,tower_height,ork_move_factor



# Load Background and Tower
background = pygame.transform.scale(pygame.image.load('src/Assets/Background/background_new.jpg'), (win_width,win_height))
tower_pic = pygame.transform.scale(pygame.image.load('src/Assets/Tower/Tower.png'),(tower_width,tower_height))



class Game():
    def __init__(self):
        self.gameover = False
        self.player = None
        self.tower = None
        self.window = pygame.display.set_mode((1000, 500))
        self.orks = []
        self.ork_cooldown = 0

    def init_Game(self):
        pygame.init()
        self.player = Hero(300, 350)
        self.tower = Tower(2, 260)


    def move_GameObjects(self):
        #Input
        userInput = pygame.key.get_pressed()

        # First the new position for the player gets calculated as well as the movement of all bullets
        self.player.move_hero(userInput)
        self.player.jump_motion(userInput)
        self.player.shoot(userInput)

        # Decide whether to add Orks in this iteration and move all existing Orks
        self.addOrks()
        self.moveOrks()

        # Calcualate wether there are intersections between the orks and the player, his bullets or the tower
        self.collision("bullet")
        self.collision("hero")
        self.collision("tower")

        # Remove orks and bullets if needed (Either ork is dead or bullet hit a target or is outside of screen)
        self.removeOrks()
        self.player.remove_Bullets()



    def addOrks(self):
        if random.random() < 1 / 100 and len(self.orks) < 5 and self.ork_cooldown <= 0:
        # if len(orks)==0:
            ork = Ork((win_width-50)*ork_move_factor, 280)
            self.orks.append(ork)
            self.ork_cooldown = 20

        self.ork_cooldown -= 1

    def moveOrks(self):
        for ork in self.orks:
            ork.move_ork()

    def removeOrks(self):
        for ork in self.orks:
            if ork.remove() or ork.dead:
                self.orks.remove(ork)


    def processOrks(self):
        for ork in orks:
            if ork.remove() or ork.dead:
                orks.remove(ork)
            ork.move_ork()
        return orks

    def collision(self,type):
        if type == "bullet":
            for ork in self.orks:
                for bullet in self.player.bullets:
                    ork.intersect_object(bullet,type)
        if type == "hero":
            for ork in self.orks:
                ork.intersect_object(self.player,type)
        if type == "tower":
            for ork in self.orks:
                ork.intersect_object(self.tower,type)

    def draw_Game(self):
        # Draw background
        self.window.blit(background, (0,0))
        self.window.blit(tower_pic,(2,260))

        # # Draw Hero
        self.player.drawObject(self.window)

        # Draw each bullet
        for bullet in self.player.bullets:
            bullet.drawObject(self.window)

        # Draw each ork
        for ork in self.orks:
            # print(f"${ork.x}; ${ork.y}")
            ork.drawObject(self.window)

        pygame.time.delay(30)
        pygame.display.update()
