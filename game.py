import pygame
import sys
import random
import textwrap

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Space Dink")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('earth500.png')
char = pygame.image.load('standing.png')
Lectrumimg = pygame.image.load('Lectrum.png')
chrolastinimg = pygame.image.load('Chrolastin.png')
Mineshaftimg = pygame.image.load('mineshaft.png')
eleriumimg = pygame.image.load('elerium.png')

clock = pygame.time.Clock()
from pygame.locals import *

score = 0
age = 18
level = 0
lectrum = 0
chrolastin = 0
elerium = 0


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


def redrawGameWindowearth():
    win.blit(bg, (0,0))
    textscore = font.render('Bollar DIlls:' + str(score), 1, (255,255,0))
    textage = font.render(f'Age:{age:.2f}',1, (0,255,0))
    textlectrum = font.render( str(lectrum),1,(102,153,204))
    man.draw(win)
    win.blit(Lectrumimg, (5,5))
    win.blit(textlectrum, (50,5))
    win.blit(textscore, (350,5))
    win.blit(textage, (350,20))
  
    pygame.display.update()

def redrawGameWindowDead():
    win.blit(bg, (0,0))
    
    pygame.display.update()


def redrawGameWindowmars():
    win.blit(bg, (0,0))
    textscore = font.render('Bollar DIlls:' + str(score), 1, (255,255,0))
    textage = font.render(f'Age:{age:.2f}',1, (0,255,0))
    textchrolastin = font.render( str(chrolastin),1,(52,165,111))
    textlectrum = font.render( str(lectrum),1,(102,153,204))
    man.draw(win)
    win.blit(chrolastinimg, (5,45))
    win.blit(textchrolastin, (50,50))
    win.blit(Lectrumimg, (5,5))
    win.blit(textlectrum, (50,5))
    win.blit(textscore, (350,5))
    win.blit(textage, (350,20))

    pygame.display.update()

def redrawGameWindowskorasta():
    win.blit(bg, (0,0))
    textscore = font.render('Bollar DIlls:' + str(score), 1, (255,255,0))
    textage = font.render(f'Age:{age:.2f}',1, (0,255,0))
    textchrolastin = font.render( str(chrolastin),1,(52,165,111))
    textlectrum = font.render( str(lectrum),1,(102,153,204))
    textelerium = font.render( str(elerium),1,(152,53,0))
    man.draw(win)
    win.blit(chrolastinimg, (5,45))
    win.blit(eleriumimg, (100,5 ))
    win.blit( textelerium, (145,5))
    win.blit(textchrolastin, (50,50))
    win.blit(Lectrumimg, (5,5))
    win.blit(textlectrum, (50,5))
    win.blit(textscore, (350,5))
    win.blit(textage, (350,20))
  
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
    elif keys[pygame.K_ESCAPE]:
            quit()
    else:
        man.right = False
        man.left = False
        man.up = False
        man.down = False
        man.walkCount = 0
##SCREEN INTERACTION##

    if level == -1:
        redrawGameWindowDead()
        bg = pygame.image.load('Dead.png')
        man.right = False
        man.left = False
        man.up = False
        man.down = False
        man.walkCount = 0

        pygame.display.update()

    elif level == 0:    
        if(man.x <= 5) and (man.y <= 150 and man.y >=100): #Left Mine Lectrum#

            clock = pygame.time.Clock()

            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Mining Lectrum', True, (102,153,204))
                message_end_time = pygame.time.get_ticks() + 15000 
                if current_time < message_end_time:
                    win.blit(message_surf, (100, 100))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    lectrum += random.randrange(1,4,1)
                    age += 12
                    if age >= 65:
                        level = -1
                        redrawGameWindowDead()
                    break

        if (man.x >= 432) and (man.y <= 150 and man.y >=100) and lectrum >= 1 : #Sell#
            clock = pygame.time.Clock()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Selling Lectrum', True, (102,153,204))
                message_end_time = pygame.time.get_ticks() + 15000
                if current_time < message_end_time:
                    win.blit(message_surf, (300, 100))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    score += random.randrange(5,75,1)
                    lectrum -= 1
                    break

        if (man.x >= 200 and man.x <= 250) and (man.y >= 400) and score >= 1000 and level == 0: #Down Buy ship and go to space#
            bg = pygame.image.load('Mars.png')
            score -= 1000
            age += 5
            level = 1

        redrawGameWindowearth()

    elif level == 1:
        if(man.x <= 5) and (man.y) <= 350 and man.y >=300: #Bottom left Farming chrolastin#

            clock = pygame.time.Clock()

            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Farming Chrolastin', True, (52,165,111))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (100, 350))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    chrolastin += random.randrange(1,8,1)
                    age += .12
                    if age >= 65:
                        level = -1
                    break

        if (man.x <= 5) and (man.y <= 150 and man.y >=100) and chrolastin >= 1 : #Sell Chrolastin#
            clock = pygame.time.Clock()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Selling 1 Chrolastin', True, (52,165,111))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (100, 150))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    score += random.randrange(5,75,5)
                    chrolastin -= 1
                    break

        if (man.x >= 432) and (man.y >= 100 and man.y <=150) and lectrum >= 1: # Sell Lectrum#
            clock = pygame.time.Clock()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Selling 1 Lectrum', True, (52,165,111))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (350, 100))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    score += random.randrange(25,100,10)
                    lectrum -= 1
                    break
        
        if (man.x >=432) and (man.y >=300 and man.y <=450) and (lectrum >= 1):
            clock = pygame.time.Clock()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Trading 1 Lectrum for Chrolastin', True, (52,165,111))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (350, 100))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    chrolastin += random.randrange(1,4,1)
                    lectrum -= 1
                    break

        if (man.x >= 200 and man.x <= 250) and (man.y <= 5) and (score >= 5000):
            bg = pygame.image.load('Skorasta.png')
            score -= 5000
            age += 5
            level = 2

        redrawGameWindowmars()

    elif level == 2:
        if(man.x <= 5) and man.y >=400: #Bottom left Sell Elerium#

            clock = pygame.time.Clock()

            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Selling Elerium', True, (152,53,0))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (100, 450))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    elerium += random.randrange(2,10,2)
                    age += .12
                    if age >= 65:
                        level = -1
                    break

        if (man.x <= 5) and (man.y <= 200 and man.y >=100) and chrolastin >= 1 : #Trade Chrolastin for Elerium#
            clock = pygame.time.Clock()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Trading Chlorastin for Elerium', True, (152,53,0))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (150, 100))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    elerium += random.randrange(1,5,1)
                    chrolastin -= 1
                    break

        if (man.x >= 432) and (man.y >= 100 and man.y <=150):
            clock = pygame.time.Clock()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Refining Elerium', True, (152,53,0))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (300, 150))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    elerium += random.randrange(1,10,2)
                    break
        
        if (man.x >=432) and (man.y >= 400) and chrolastin >= 1:
            clock = pygame.time.Clock()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Selling Chrolastin', True, (52,165,111))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (300, 400))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    score += random.randrange(25,100,100)
                    lectrum -= 1
                    break

        if (man.x <= 5) and (man.y >200 and man.y <= 300) and (score >= 10000):
            bg = pygame.image.load('AlphaCentauri.png')
            score -= 10000
            age += 10
            level = 3

        redrawGameWindowskorasta()   

    elif level == 3:
        if(man.x <= 5)  and man.y >=400: #Bottom left Sell Elerium#

            clock = pygame.time.Clock()

            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Selling Elerium', True, (152,53,0))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (100, 450))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    score += random.randrange(20,100,2)
                    age += .12
                    if age >= 65:
                        level = -1
                    break

        if (man.x <= 5) and (man.y <= 200 and man.y >=100) and chrolastin >= 1 : #Trade Chrolastin for Elerium#
            clock = pygame.time.Clock()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Trading Chlorastin for Elerium', True, (152,53,0))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (150, 100))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    elerium += random.randrange(1,5,1)
                    chrolastin -= 1
                    break

        if (man.x >= 432) and (man.y >= 100 and man.y >=150):
            clock = pygame.time.Clock()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Refining Elerium', True, (152,53,0))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (350, 150))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    elerium += random.randrange(1,10,2)
                    age += .12
                    if age >= 65:
                        level = -1
                    break
        
        if (man.x >=432) and (man.y >= 400) and chrolastin >= 1:
            clock = pygame.time.Clock()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                current_time = pygame.time.get_ticks()
                message_surf = font.render('Selling Chrolastin', True, (52,165,111))
                message_end_time = pygame.time.get_ticks() + 15000 # display for 3 seconds
                if current_time < message_end_time:
                    win.blit(message_surf, (350, 100))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    score += random.randrange(25,100,100)
                    lectrum -= 1
                    break

        if (man.x <= 5) and (man.y >200 and man.y <= 300) and (score >= 10000):
            bg = pygame.image.load('AlphaCentauri.png')
            score -= 10000
            age += 10
            level = 3

        redrawGameWindowAlphaCentauri()  

pygame.quit()