import pygame
import sys
import random
import textwrap

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Space Dink")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('earth5001.png')
char = pygame.image.load('standing.png')
Lectrumimg = pygame.image.load('Lectrum.png')
Mineshaftimg = pygame.image.load('mineshaft.png')

clock = pygame.time.Clock()
from pygame.locals import *

score = 0
age = 18
level = 1
lectrum = 0


class player (object):
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        self.walkCount = 0
    
    def draw(self,win):
    
        if self.walkCount +1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right :
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))


def redrawGameWindow():
    win.blit(bg, (0,0))
    textscore = font.render('Bollar DIlls:' + str(score), 1, (255,255,0))
    textage = font.render('Age:' + str(age),1, (0,255,0))
    textlectrum = font.render( str(lectrum),1,(102,153,204))
    man.draw(win)
    win.blit(Lectrumimg, (5,5))
    win.blit(Mineshaftimg,(5, 325))
    win.blit(textlectrum, (50,15))
    win.blit(textscore, (300,10))
    win.blit(textage, (100,10))
  

    pygame.display.update()


##MAIN LOOP##
font = pygame.font.SysFont('comicsans', 20, True, True)
man = player(220,0,64,64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys= pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width -man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    elif keys[pygame.K_UP] and man.y > man.vel:
        man.y -= man.vel
        man.up = True
        man.down = False
    elif keys[pygame.K_DOWN] and man.y < 500 - man.height- man.vel:
        man.y+= man.vel
        man.down = True
        man.down = False
    else:
        man.right = False
        man.left = False
        man.up = False
        man.down = False
        man.walkCount = 0
##SCREEN INTERACTION##

        
    if (man.x <= 5) and (man.y <= 350 and man.y >=295): #Left Hunting?#

        clock = pygame.time.Clock()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            current_time = pygame.time.get_ticks()
            message_surf = font.render('Mining Crypto!', True, (255, 0, 0))
            message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
            if current_time < message_end_time:
                win.blit(message_surf, (140, 200))
                pygame.display.flip()
                pygame.time.delay(500)
                lectrum += random.randrange(1,4,1)
                age += .12
                break

    if (man.x >= 432) and (man.y <= 250 and man.y >=150) and lectrum >= 1 : #Sell?#
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            current_time = pygame.time.get_ticks()
            message_surf = font.render('Selling 1 Lectrum', True, (102,153,204))
            message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
            if current_time < message_end_time:
                win.blit(message_surf, (400, 200))
                pygame.display.flip()
                pygame.time.delay(500)
                score += random.randrange(5,75,1)
                lectrum -= 1
                break

    if (man.x >= 180 and man.x <= 250) and (man.y >= 400) and score >= 1000: #Down Buy ship and go to space#
        bg = pygame.image.load('mARS.jpg')
        score -= 1000
        age += 5

    redrawGameWindow()
    


pygame.quit()