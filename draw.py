import pygame
from pygame.locals import *
import sys
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Draw  by Rithik')
while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN :
            pixObj = pygame.PixelArray(screen)
            if event.button == 1 :
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                pixObj[x][y] = (0,0,0)
                del pixObj



    pygame.display.update()