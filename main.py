import pygame
from pygame.locals import *

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((512, 512))

# Background
background = pygame.image.load('Chess_Board.png')

BLUE = (0, 0, 255)

# Caption and Icon
pygame.display.set_caption("Floatboard")
icon = pygame.image.load('float.jpg')
pygame.display.set_icon(icon)

# Player
pawnWhiteImg = pygame.image.load('pawn_white.png')
a2_X = 3
a2_Y = 390
b2_X = 67
b2_Y = 390
c2_X = 133
c2_Y = 390
d2_X = 197
d2_Y = 390
e2_X = 261
e2_Y = 390
f2_X = 325
f2_Y = 390
g2_X = 389
g2_Y = 390
h2_X = 453
h2_Y = 390

def pawnWhite(x, y):
    screen.blit(pawnWhiteImg, (x, y))

pawnBlackImg = pygame.image.load('pawn_black.png')

a7_X = 3
a7_Y = 70
b7_X = 67
b7_Y = 70
c7_X = 133
c7_Y = 70
d7_X = 197
d7_Y = 70
e7_X = 261
e7_Y = 70
f7_X = 325
f7_Y = 70
g7_X = 389
g7_Y = 70
h7_X = 453
h7_Y = 70

def pawnBlack(x, y):
    screen.blit(pawnBlackImg, (x, y))

rookBlackImg = pygame.image.load('rook_black.png')    
a8_X = 3
a8_Y = 10
h8_X = 453
h8_Y = 10
def rookBlack(x, y):
    screen.blit(rookBlackImg, (x, y))

rookWhiteImg = pygame.image.load('rook_white.png')    
a1_X = 3
a1_Y = 450
h1_X = 453
h1_Y = 450
def rookWhite(x, y):
    screen.blit(rookWhiteImg, (x, y))

knightBlackImg = pygame.image.load('knight_black.png')    
b8_X = 67
b8_Y = 10
g8_X = 389
g8_Y = 10
def knightBlack(x, y):
    screen.blit(knightBlackImg, (x, y))

knightWhiteImg = pygame.image.load('knight_white.png')    
b1_X = 67
b1_Y = 450
g1_X = 389
g1_Y = 450
def knightWhite(x, y):
    screen.blit(knightWhiteImg, (x, y))

bishopBlackImg = pygame.image.load('bishop_black.png')    
c8_X = 131
c8_Y = 10
f8_X = 325
f8_Y = 10
def bishopBlack(x, y):
    screen.blit(bishopBlackImg, (x, y))

bishopWhiteImg = pygame.image.load('bishop_white.png')    
c1_X = 131
c1_Y = 450
f1_X = 325
f1_Y = 450
def bishopWhite(x, y):
    screen.blit(bishopWhiteImg, (x, y))



kingWhiteImg = pygame.image.load('king_white.png')
kingWhiteImg.convert()    
e1_X = 259
e1_Y = 450
def kingWhite(x, y):
    screen.blit(kingWhiteImg, (x, y))

kingBlackImg = pygame.image.load('king_black.png')    
kingBlackImg.convert()
e8_X = 259
e8_Y = 10
def kingBlack(x, y):
    screen.blit(kingBlackImg, (x, y))

queenWhiteImg = pygame.image.load('Queen_white.png')   
queenWhiteImg.convert()   
d1_X = 195
d1_Y = 450
def queenWhite(x, y):
    screen.blit(queenWhiteImg, (x, y))

queenBlackImg = pygame.image.load('Queen_black.png') 
queenBlackImg.convert()   
d8_X = 195
d8_Y = 10
def queenBlack(x, y):
    screen.blit(queenBlackImg, (x, y))

rectkingWhite = kingWhiteImg.get_rect()
rectkingWhite.center = 289, 480

rectkingBlack = kingBlackImg.get_rect()
rectkingBlack.center = 289, 40

rectqueenBlack = queenBlackImg.get_rect()
rectqueenBlack.center = 225, 40

rectqueenWhite = queenWhiteImg.get_rect()
rectqueenWhite.center = 225, 480

rectbishopBlackone = bishopBlackImg.get_rect()
rectbishopBlackone.center = 161, 40

rectbishopWhiteone = bishopWhiteImg.get_rect()
rectbishopWhiteone.center = 161, 480

rectbishopBlacktwo = bishopBlackImg.get_rect()
rectbishopBlacktwo.center = 355, 40

rectbishopWhitetwo = bishopWhiteImg.get_rect()
rectbishopWhitetwo.center = 355, 480

rectknightBlackone = knightBlackImg.get_rect()
rectknightBlackone.center = 97, 40

rectknightWhiteone = knightWhiteImg.get_rect()
rectknightWhiteone.center = 97, 480

rectknightBlacktwo = knightBlackImg.get_rect()
rectknightBlacktwo.center = 419, 40

rectknightWhitetwo = knightWhiteImg.get_rect()
rectknightWhitetwo.center = 419, 480

rectrookBlackone = rookBlackImg.get_rect()
rectrookBlackone.center = 33, 40

rectrookWhiteone = rookWhiteImg.get_rect()
rectrookWhiteone.center = 33, 480

rectrookBlacktwo = rookBlackImg.get_rect()
rectrookBlacktwo.center = 483, 40

rectrookWhitetwo = rookWhiteImg.get_rect()
rectrookWhitetwo.center = 483, 480

rectpawnWhiteA = pawnWhiteImg.get_rect()
rectpawnWhiteA.center = 33, 420

rectpawnBlackA = pawnBlackImg.get_rect()
rectpawnBlackA.center = 33, 100

rectpawnWhiteB = pawnWhiteImg.get_rect()
rectpawnWhiteB.center = 97, 420

rectpawnBlackB = pawnBlackImg.get_rect()
rectpawnBlackB.center = 97, 100

rectpawnWhiteC = pawnWhiteImg.get_rect()
rectpawnWhiteC.center = 165, 420

rectpawnBlackC = pawnBlackImg.get_rect()
rectpawnBlackC.center = 165, 100

rectpawnWhiteD = pawnWhiteImg.get_rect()
rectpawnWhiteD.center = 229, 420

rectpawnBlackD = pawnBlackImg.get_rect()
rectpawnBlackD.center = 229, 100

rectpawnWhiteE = pawnWhiteImg.get_rect()
rectpawnWhiteE.center = 293, 420

rectpawnBlackE = pawnBlackImg.get_rect()
rectpawnBlackE.center = 293, 100

rectpawnWhiteF = pawnWhiteImg.get_rect()
rectpawnWhiteF.center = 357, 420

rectpawnBlackF = pawnBlackImg.get_rect()
rectpawnBlackF.center = 357, 100

rectpawnWhiteG = pawnWhiteImg.get_rect()
rectpawnWhiteG.center = 421, 420

rectpawnBlackG = pawnBlackImg.get_rect()
rectpawnBlackG.center = 421, 100

rectpawnWhiteH = pawnWhiteImg.get_rect()
rectpawnWhiteH.center = 485, 420

rectpawnBlackH = pawnBlackImg.get_rect()
rectpawnBlackH.center = 485, 100

# Game Loop
running = True
moving = False

while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background,(0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left')
        elif event.type == MOUSEBUTTONDOWN:
            if rectkingWhite.collidepoint(event.pos):
                moving = True
            elif rectkingBlack.collidepoint(event.pos):
                moving = True
            elif rectqueenBlack.collidepoint(event.pos):
                moving = True
            elif rectqueenWhite.collidepoint(event.pos):
                moving = True
            elif rectbishopWhiteone.collidepoint(event.pos):
                moving = True
            elif rectbishopBlackone.collidepoint(event.pos):
                moving = True
            elif rectbishopWhitetwo.collidepoint(event.pos):
                moving = True
            elif rectbishopBlacktwo.collidepoint(event.pos):
                moving = True
            elif rectknightWhiteone.collidepoint(event.pos):
                moving = True
            elif rectknightBlackone.collidepoint(event.pos):
                moving = True
            elif rectknightWhitetwo.collidepoint(event.pos):
                moving = True
            elif rectknightBlacktwo.collidepoint(event.pos):
                moving = True
            elif rectrookWhiteone.collidepoint(event.pos):
                moving = True
            elif rectrookBlackone.collidepoint(event.pos):
                moving = True
            elif rectrookWhitetwo.collidepoint(event.pos):
                moving = True
            elif rectrookBlacktwo.collidepoint(event.pos):
                moving = True
            elif rectpawnWhiteA.collidepoint(event.pos):
                moving = True
            elif rectpawnBlackA.collidepoint(event.pos):
                moving = True
            elif rectpawnWhiteB.collidepoint(event.pos):
                moving = True
            elif rectpawnBlackB.collidepoint(event.pos):
                moving = True
            elif rectpawnWhiteC.collidepoint(event.pos):
                moving = True
            elif rectpawnBlackC.collidepoint(event.pos):
                moving = True
            elif rectpawnWhiteD.collidepoint(event.pos):
                moving = True
            elif rectpawnBlackD.collidepoint(event.pos):
                moving = True
            elif rectpawnWhiteE.collidepoint(event.pos):
                moving = True
            elif rectpawnBlackE.collidepoint(event.pos):
                moving = True
            elif rectpawnWhiteF.collidepoint(event.pos):
                moving = True
            elif rectpawnBlackF.collidepoint(event.pos):
                moving = True
            elif rectpawnWhiteG.collidepoint(event.pos):
                moving = True
            elif rectpawnBlackG.collidepoint(event.pos):
                moving = True
            elif rectpawnWhiteH.collidepoint(event.pos):
                moving = True
            elif rectpawnBlackH.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving:
            if rectkingWhite.collidepoint(event.pos):
                rectkingWhite.move_ip(event.rel)
            elif rectkingBlack.collidepoint(event.pos):
                rectkingBlack.move_ip(event.rel)
            elif rectqueenBlack.collidepoint(event.pos):
                rectqueenBlack.move_ip(event.rel)
            elif rectqueenWhite.collidepoint(event.pos):
                rectqueenWhite.move_ip(event.rel)
            elif rectbishopWhiteone.collidepoint(event.pos):
                rectbishopWhiteone.move_ip(event.rel)
            elif rectbishopBlackone.collidepoint(event.pos):
                rectbishopBlackone.move_ip(event.rel)
            elif rectbishopWhitetwo.collidepoint(event.pos):
                rectbishopWhitetwo.move_ip(event.rel)
            elif rectbishopBlacktwo.collidepoint(event.pos):
                rectbishopBlacktwo.move_ip(event.rel)
            elif rectknightWhiteone.collidepoint(event.pos):
                rectknightWhiteone.move_ip(event.rel)
            elif rectknightBlackone.collidepoint(event.pos):
                rectknightBlackone.move_ip(event.rel)
            elif rectknightWhitetwo.collidepoint(event.pos):
                rectknightWhitetwo.move_ip(event.rel)
            elif rectknightBlacktwo.collidepoint(event.pos):
                rectknightBlacktwo.move_ip(event.rel)
            elif rectrookWhiteone.collidepoint(event.pos):
                rectrookWhiteone.move_ip(event.rel)
            elif rectrookBlackone.collidepoint(event.pos):
                rectrookBlackone.move_ip(event.rel)
            elif rectrookWhitetwo.collidepoint(event.pos):
                rectrookWhitetwo.move_ip(event.rel)
            elif rectrookBlacktwo.collidepoint(event.pos):
                rectrookBlacktwo.move_ip(event.rel)
            elif rectpawnWhiteA.collidepoint(event.pos):
                rectpawnWhiteA.move_ip(event.rel)
            elif rectpawnBlackA.collidepoint(event.pos):
                rectpawnBlackA.move_ip(event.rel)
            elif rectpawnWhiteB.collidepoint(event.pos):
                rectpawnWhiteB.move_ip(event.rel)
            elif rectpawnBlackB.collidepoint(event.pos):
                rectpawnBlackB.move_ip(event.rel)
            elif rectpawnWhiteC.collidepoint(event.pos):
                rectpawnWhiteC.move_ip(event.rel)
            elif rectpawnBlackC.collidepoint(event.pos):
                rectpawnBlackC.move_ip(event.rel)
            elif rectpawnWhiteD.collidepoint(event.pos):
                rectpawnWhiteD.move_ip(event.rel)
            elif rectpawnBlackD.collidepoint(event.pos):
                rectpawnBlackD.move_ip(event.rel)
            elif rectpawnWhiteE.collidepoint(event.pos):
                rectpawnWhiteE.move_ip(event.rel)
            elif rectpawnBlackE.collidepoint(event.pos):
                rectpawnBlackE.move_ip(event.rel)
            elif rectpawnWhiteF.collidepoint(event.pos):
                rectpawnWhiteF.move_ip(event.rel)
            elif rectpawnBlackF.collidepoint(event.pos):
                rectpawnBlackF.move_ip(event.rel)
            elif rectpawnWhiteG.collidepoint(event.pos):
                rectpawnWhiteG.move_ip(event.rel)
            elif rectpawnBlackG.collidepoint(event.pos):
                rectpawnBlackG.move_ip(event.rel)
            elif rectpawnWhiteH.collidepoint(event.pos):
                rectpawnWhiteH.move_ip(event.rel)
            elif rectpawnBlackH.collidepoint(event.pos):
                rectpawnBlackH.move_ip(event.rel)

        

    # pawnWhite(a2_X, a2_Y)
    # pawnWhite(b2_X, b2_Y)
    # pawnWhite(c2_X, c2_Y)
    # pawnWhite(d2_X, d2_Y)
    # pawnWhite(e2_X, e2_Y)
    # pawnWhite(f2_X, f2_Y)
    # pawnWhite(g2_X, g2_Y)
    # pawnWhite(h2_X, h2_Y)

    # pawnBlack(a7_X, a7_Y)
    # pawnBlack(b7_X, b7_Y)
    # pawnBlack(c7_X, c7_Y)
    # pawnBlack(d7_X, d7_Y)
    # pawnBlack(e7_X, e7_Y)
    # pawnBlack(f7_X, f7_Y)
    # pawnBlack(g7_X, g7_Y)
    # pawnBlack(h7_X, h7_Y)

    # rookBlack(a8_X, a8_Y)
    # rookBlack(h8_X, h8_Y)

    # rookWhite(a1_X, a1_Y)
    # rookWhite(h1_X, h1_Y)

    # knightWhite(b1_X, b1_Y)
    # knightWhite(g1_X, g1_Y)

    # knightBlack(b8_X, b8_Y)
    # knightBlack(g8_X, g8_Y)

    # bishopWhite(c1_X, c1_Y)
    # bishopWhite(f1_X, f1_Y)

    # bishopBlack(c8_X, c8_Y)
    # bishopBlack(f8_X, f8_Y)

    # kingBlack(e8_X, e8_Y)
    # kingWhite(e1_X, e1_Y)

    # queenBlack(d8_X, d8_Y)
    # queenWhite(d1_X, d1_Y)

    screen.blit(kingWhiteImg, rectkingWhite)
    screen.blit(kingBlackImg, rectkingBlack)
    screen.blit(queenBlackImg, rectqueenBlack)
    screen.blit(queenWhiteImg, rectqueenWhite)
    screen.blit(bishopWhiteImg, rectbishopWhiteone)
    screen.blit(bishopBlackImg, rectbishopBlackone)
    screen.blit(bishopWhiteImg, rectbishopWhitetwo)
    screen.blit(bishopBlackImg, rectbishopBlacktwo)
    screen.blit(knightWhiteImg, rectknightWhiteone)
    screen.blit(knightBlackImg, rectknightBlackone)
    screen.blit(knightWhiteImg, rectknightWhitetwo)
    screen.blit(knightBlackImg, rectknightBlacktwo)
    screen.blit(rookWhiteImg, rectrookWhiteone)
    screen.blit(rookBlackImg, rectrookBlackone)
    screen.blit(rookWhiteImg, rectrookWhitetwo)
    screen.blit(rookBlackImg, rectrookBlacktwo)
    screen.blit(pawnWhiteImg, rectpawnWhiteA)
    screen.blit(pawnBlackImg, rectpawnBlackA)
    screen.blit(pawnWhiteImg, rectpawnWhiteB)
    screen.blit(pawnBlackImg, rectpawnBlackB)
    screen.blit(pawnWhiteImg, rectpawnWhiteC)
    screen.blit(pawnBlackImg, rectpawnBlackC)
    screen.blit(pawnWhiteImg, rectpawnWhiteD)
    screen.blit(pawnBlackImg, rectpawnBlackD)
    screen.blit(pawnWhiteImg, rectpawnWhiteE)
    screen.blit(pawnBlackImg, rectpawnBlackE)
    screen.blit(pawnWhiteImg, rectpawnWhiteF)
    screen.blit(pawnBlackImg, rectpawnBlackF)
    screen.blit(pawnWhiteImg, rectpawnWhiteG)
    screen.blit(pawnBlackImg, rectpawnBlackG)
    screen.blit(pawnWhiteImg, rectpawnWhiteH)
    screen.blit(pawnBlackImg, rectpawnBlackH)
    # pygame.draw.rect(screen, BLUE, rectkingBlack, 2)

    pygame.display.update()

pygame.quit()