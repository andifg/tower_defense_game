import pygame
import os
import conf

# Load Classes
from Classes.hero import Hero
from Classes.bullet import Bullet
from Classes.tower import Tower
from Classes.ork import Ork,processOrks


# Load logging
from logger import logger
logger.info("Game started")

# Load Background and Tower
background = pygame.transform.scale(pygame.image.load('src/Assets/Background/background_new.jpg'), (conf.win_width,conf.win_height))
tower_pic = pygame.transform.scale(pygame.image.load('src/Assets/Tower/Tower.png'),(conf.tower_width,conf.tower_height))

# Draw game method
def draw_game():
    # Draw background
    win.blit(background, (0,0))
    win.blit(tower_pic,(2,260))

    # Draw Hero
    player.drawObject(win)

    # Draw each bullet seperately
    for bullet in player.bullets:
        bullet.drawObject(win)

    # Draw each ork
    for ork in orks:
        # print(f"${ork.x}; ${ork.y}")
        ork.drawObject(win)

    pygame.time.delay(30)
    pygame.display.update()

def collision(type):
    if type == "bullet":
        for ork in orks:
            for bullet in player.bullets:
                ork.intersect_object(bullet,type)
    if type == "hero":
        for ork in orks:
            ork.intersect_object(player,type)
    if type == "tower":
        for ork in orks:
            ork.intersect_object(tower,type)

# Init game
pygame.init()
win = pygame.display.set_mode((1000, 500))

# Intialize Player
player = Hero(300, 350)

# Initialize Tower
tower = Tower(2, 260)

# Initialize Enemies
orks = []

# Mainloop
run = True
while run:

    # Input
    userInput = pygame.key.get_pressed()

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Main log info output
    if conf.logger_main:
        logger.info(f"PLAYER: x: {player.x} | y: {player.y} | Step index: {player.step_index} | Face right: {player.face_right} | Face left: {player.face_left} | Cooldown: {player.cooldown}|  #-Bullets: {len(player.bullets)} | #-Orks {len(orks)}")

    # if userInput[pygame.K_RIGHT] or userInput[pygame.K_LEFT]:

    # Move hero and bullets of hero
    player.move_hero(userInput)
    player.jump_motion(userInput)
    player.shoot(userInput)

    collision("bullet")
    collision("hero")
    collision("tower")

    # Move Orks
    orks = processOrks(orks)

    draw_game()
