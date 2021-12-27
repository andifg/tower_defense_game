import pygame
import os

# Init game
pygame.init()
win_height = 500
win_width = 1000
win = pygame.display.set_mode((1000, 500))

# Load and transform images
background = pygame.transform.scale(pygame.image.load('src/Background/background.png'), (1000,500))
stationary = pygame.image.load(os.path.join("src" , "Hero","standing.png"))
bullet =  pygame.transform.scale(pygame.image.load(os.path.join("src" , "Bullets","light_bullet.png")),(7,7))
left = []
right = []
for picIndex in range(1,10):
    right.append(pygame.image.load(os.path.join("src" , "Hero", "R" + str(picIndex) + ".png")))
    left.append(pygame.image.load(os.path.join("src" , "Hero", "L" + str(picIndex) + ".png")))

class Bullet:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.index = 15
        self.direction = direction

    def drawBullet (self, win):
        win.blit(bullet, (self.x, self.y))


    def updateBullet (self):
        self.x += self.index * self.direction


class Hero:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velvx = 10
        self.velvy = 10
        self.face_right = False
        self.face_left  = False
        self.step_index = 0
        self.jump = False
        self.bullets = []
        self.cooldown = 0

    def move_hero (self, userInput):
        if userInput[pygame.K_RIGHT] and self.x < win_width - 40:
            self.x += self.velvx
            self.step_index += 1
            self.face_left = False
            self.face_right = True
            # print(f" RIGHT Self x: {self.x} ; Self y: {self.y} ; Self step index: {self.step_index} ; Self face right {self.face_right} ; Self face left {self.face_left}")
        elif userInput[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velvx
            self.step_index += 1
            self.face_left = True
            self.face_right = False
            # print(f"LEFT Self x: {self.x} ; Self y: {self.y} ; Self step index: {self.step_index} ; Self face right {self.face_right} ; Self face left {self.face_left}")
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

    def draw_hero(self, win):
        print(f"Self x: {self.x} ; Self y: {self.y} ; Self step index: {self.step_index} ; Self face right {self.face_right} ; Self face left {self.face_left} ; Self Cooldown {self.cooldown}; Bullets {len(self.bullets)}")
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
        # print (list(map(lambda x: {"X-Achse":x.x, "Y-Achse":x.y, "Direction": x.direction}, self.bullets)))

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
            if bullet.x > win_width or bullet.x <= 0:
                self.bullets.remove(bullet)
                del bullet
            else:
                bullet.updateBullet()


# Draw game
def draw_game():

    # Draw background black
    win.blit(background, (0,0))
    # Draw Hero
    player.draw_hero(win)

    # Draw each bullet seperately
    for bullet in player.bullets:
        bullet.drawBullet(win)

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

    # if userInput[pygame.K_RIGHT] or userInput[pygame.K_LEFT]:

    # Move hero and bullets of hero
    player.move_hero(userInput)
    player.jump_motion(userInput)
    player.shoot(userInput)
    draw_game()
