import pygame
import os

# Init game
pygame.init()
win_height = 500
win_width = 1000
win = pygame.display.set_mode((1000, 500))

# Load and transform images
background = pygame.transform.scale(pygame.image.load('src/background.png'), (1000,500))
stationary = pygame.image.load(os.path.join("src" , "Hero","standing.png"))
left = []
right = []
for picIndex in range(1,10):
    right.append(pygame.image.load(os.path.join("src" , "Hero", "R" + str(picIndex) + ".png")))
    left.append(pygame.image.load(os.path.join("src" , "Hero", "L" + str(picIndex) + ".png")))

class Hero:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velvx = 10
        self.face_right = True
        self.face_left  = False
        self.step_index = 0

    def move_hero (self, userInput):
        if userInput[pygame.K_RIGHT]:
            self.x += self.velvx
            self.step_index += 1
            self.face_left = False
            self.face_right = True
            print(f" RIGHT Self x: {self.x} ; Self y: {self.y} ; Self step index: {self.step_index} ; Self face right {self.face_right} ; Self face left {self.face_left}")
        elif userInput[pygame.K_LEFT]:
            self.x -= self.velvx
            self.step_index += 1
            self.face_left = True
            self.face_right = False
            print(f"LEFT Self x: {self.x} ; Self y: {self.y} ; Self step index: {self.step_index} ; Self face right {self.face_right} ; Self face left {self.face_left}")
        else:
            self.step_index = 0

    def draw_hero(self, win):
        print(f"Self x: {self.x} ; Self y: {self.y} ; Self step index: {self.step_index} ; Self face right {self.face_right} ; Self face left {self.face_left}")
        # win.blit(right[0], (250 ,250 ))
        if self.step_index >= 36:
            self.step_index = 0
        if self.face_right:
            win.blit(right[self.step_index//4], (self.x, self.y))
        elif self.face_left:
            win.blit(left[self.step_index//4], (self.x, self.y))
        else:
            win.blit(stationary, (self.x,self.y))



# Draw game
def draw_game():
    pass
    # win.fill((10, 10, 10))
    win.blit(background, (0,0))
    player.draw_hero(win)
    pygame.time.delay(30)
    pygame.display.update()

# Intialize Player
player = Hero(300, 350)


# Mainloop
run = True
while run:

    # Input
    userInput = pygame.key.get_pressed()

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if userInput[pygame.K_RIGHT] or userInput[pygame.K_LEFT]:
        player.move_hero(userInput)
        draw_game()
