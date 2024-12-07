import pygame, sys
from pygame.locals import *
import random

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_X = 500
SCREEN_Y = 700
RECT_X = 400
RECT_Y = 500
BKG = (184, 208, 252)
WALL = (51, 28, 2)
# bottom colors
PINK = (209, 17, 103)
BLACK = (7, 8, 8)
BOT1 = (117, 160, 235)
# lightest brown
FILL1 = (194, 157, 114)
# middle brown
FILL2 = (181, 143, 101)
# bottom brown
FILL3 = (173, 141, 102)
sizes = [36, 40, 44, 48, 53, 57, 61, 66, 70]

pygame.display.set_caption('.  Keihatsu Game')
Icon = pygame.image.load('assets/boba-pink.png')
pygame.display.set_icon(Icon)



screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  #creates x by y screen
icon1 = pygame.image.load('assets/adam-smith.png')
icon2 = pygame.image.load('assets/baron-montesquieu.png')
icon3 = pygame.image.load('assets/denis-diderot.png')
icon4 = pygame.image.load('assets/john-locke.png')
icon5 = pygame.image.load('assets/mary-wollstonecraft.png')
icon6 = pygame.image.load('assets/simon-bolivar.png')
icon7 = pygame.image.load('assets/thomas-hobbes.png')
icon8 = pygame.image.load('assets/thomas-paine.png')
icon9 = pygame.image.load('assets/voltaire.png')
icon = [icon1, icon2, icon3, icon4, icon5, icon6, icon7, icon8, icon9]

str1 = 'assets/adam-smith.png'
str2 = 'assets/baron-montesquieu.png'
str3 = 'assets/denis-diderot.png'
str4 = 'assets/john-locke.png'
str5 = 'assets/mary-wollstonecraft.png'
str6 = 'assets/simon-bolivar.png'
str7 = 'assets/thomas-hobbes.png'
str8 = 'assets/thomas-paine.png'
str9 = 'assets/voltaire.png'
str = [str1, str2, str3, str4, str5, str6, str7, str8, str9]

width = icon[0].get_rect().width
height = icon[0].get_rect().height


class Face(pygame.sprite.Sprite):  #class for face objects

    def __init__(self):
        super().__init__()
        self.id = random.randint(0, 3)
        self.image = pygame.transform.scale(pygame.image.load(str[self.id]),(sizes[self.id], sizes[self.id]))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_X - 50), 50)
        self.doneFalling = False
        self.isFalling = False
        self.addFace = False

    def update(self):
        #
        # move on x-axis
        if not self.doneFalling:
            if not self.isFalling:
                mx, my = pygame.mouse.get_pos()
                if mx < 50 + sizes[self.id] / 2:
                    self.rect.left = 50
                elif mx > SCREEN_X - 50 - sizes[self.id] / 2:
                    self.rect.right = SCREEN_X - 50
                else:
                    self.rect.center = (mx, 50)
        # drop
            else:
                self.fall()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def fall(self):
        self.isFalling = True
        self.velocity = 10
        self.accel = 20
        self.rect.move_ip(0, self.velocity)
        self.velocity += self.accel
        if self.rect.bottom > RECT_Y:
            self.rect.bottom = RECT_Y
            self.isFalling = False
            self.doneFalling = True
            self.addFace = True

face1 = Face()
# face2 = Face('assets/baron-montesquieu.png')
# face3 = Face('assets/denis-diderot.png')
# face4 = Face('assets/john-locke.png')
# face5 = Face('assets/mary-wollstonecraft.png')
# face6 = Face('assets/simon-bolivar.png')
# face7 = Face('assets/thomas-hobbes')
# face8 = Face('assets/thomas-paine')
# face9 = Face('assets/voltaire.png')

faces = [face1]

font = pygame.font.Font('freesansbold.ttf', 10)

# create a text surface object,
# on which text is drawn on it.
text = font.render('Designed by: Kailua Cheng, Alice Su, Paige Xu', True, PINK)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (250, 660)

while True:
    pressed = False
    for event in pygame.event.get():  #ends game if quitted
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            pressed = True

    #draw background
    screen.fill(BKG)
    
    # top lightest
    pygame.draw.rect(screen,
         FILL1,
         pygame.Rect(50, 50, RECT_X, RECT_Y - 50),
                     border_bottom_left_radius=35,
                     border_bottom_right_radius=35)
    pygame.draw.rect(screen,
         FILL2,
         pygame.Rect(50, 150, RECT_X, RECT_Y - 150),
                     border_bottom_left_radius=35,
                     border_bottom_right_radius=35)

    pygame.draw.rect(screen,
         FILL3,
         pygame.Rect(50, 250, RECT_X, RECT_Y - 250),
                     border_bottom_left_radius=35,
                     border_bottom_right_radius=35)


    pygame.draw.rect(screen,
         WALL,
         pygame.Rect(50, 50, RECT_X, RECT_Y - 50),
         4,
         border_bottom_left_radius=35,
         border_bottom_right_radius=35)

    pygame.draw.rect(screen,
         BLACK,
         pygame.Rect(0, 560, RECT_X+100, 200))

    pygame.draw.rect(screen,
         BOT1,
         pygame.Rect(0, 550, RECT_X+100, 100))

    screen.blit(text, textRect)

    # straw
    pygame.draw.rect(screen,
         WALL,
         pygame.Rect(350, 0, 20, 50))

    #draw images at bottom
    images = []
    ratio = 0.05
    step = 0.006
    for i in range(9):
        image = pygame.transform.scale(
            icon[i], (width * (ratio + step * i), height * (ratio + step * i)))
        images.append(image)

    x = 0
    y = 0
    gap = 2
    prev_width = 0

    for i in range(9):
        x = x + prev_width + gap
        y = 600 - images[i].get_rect().height / 2
        prev_width = images[i].get_rect().width
        screen.blit(images[i], (x, y))

    #deal with every sprite 
    for face in faces:
        face.draw(screen)
        face.update()
        if not face.doneFalling and pressed:
            # print("fall")
            face.isFalling = True
        if face.addFace:
            faces.append(Face())
            face.addFace = False
            # print(len(faces))

    pygame.display.update()
    FramePerSec.tick(FPS)
