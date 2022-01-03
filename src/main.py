import pygame
import os
import conf

# Load Classes
from Classes.hero import Hero
from Classes.bullet import Bullet
from Classes.tower import Tower
from Classes.ork import Ork
from Classes.game import Game


# Load logging
from logger import logger
logger.info("Game started")


run = True

game = Game()
game.init_Game()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    game.move_GameObjects()

    if conf.logger_main:
        logger.info(f"PLAYER: x: {game.player.x} | y: {game.player.y} | Step index: {game.player.step_index} | Face right: {game.player.face_right} | Face left: {game.player.face_left} | Cooldown: {game.player.cooldown}|  #-Bullets: {len(game.player.bullets)} | #-Orks {len(game.orks)}")

    game.draw_Game()