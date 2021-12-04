import pygame
import os

pygame.init()
win = pygame.display.set_mode((1000, 500))

bg_image = pygame.image.load('src/background.png')
bg = pygame.transform.scale(bg_image, (1000,500))

# Load images
stationary = pygame.image.load(os.path.join("src" , "Hero","standing.png"))

left = []
right = []
for picIndex in range(1,10):
    right.append(pygame.image.load(os.path.join("src" , "Hero", "R" + str(picIndex) + ".png")))
    left.append(pygame.image.load(os.path.join("src" , "Hero", "L" + str(picIndex) + ".png")))



width = 1000
height = 500

x = 500
y = 350
vel_x = 10
vel_y = 10
jump = False
run = True
move_left = False
move_right = False
stepIndex = 0
i = 0


def draw_game():
    global stepIndex
    global i
    win.blit(bg,(i,0))
    win.blit(bg,(width+i,0))

    if stepIndex >= 9:
        stepIndex = 0

    if move_left:
        win.blit(left[stepIndex], (x,y))
        stepIndex += 1
    elif move_right:
        win.blit(left[stepIndex], (x,y))
        stepIndex += 1
    else:
        win.blit(stationary, (x,y))

    # Make background fluent
    i -= 1
    if i == -1000:
        i = 0


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movement
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x > 0:
        x -= vel_x
        move_left = True

    elif userInput[pygame.K_RIGHT] and x < width:
        x += vel_x
        move_right = True
    else:
        move_left = False
        move_right = False


    #Jump
    if jump is False and userInput[pygame.K_SPACE]:
        jump = True
    if jump is True:
        y -= vel_y*5
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    draw_game()

    pygame.time.delay(20)
    pygame.display.update()