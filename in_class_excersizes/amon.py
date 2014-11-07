# -*- coding: utf-8 -*-
"""
"""

import pygame
from pygame.locals import *
import time

class Quadrilateral(object):
    """ Represents a quadrilateral that can draw itself to a pygame window """
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def draw(self,screen):
        pygame.draw.line(screen, pygame.Color(0,0,0), (self.x1, self.y1), (self.x2, self.y2))
        pygame.draw.line(screen, pygame.Color(0,0,0), (self.x2, self.y2), (self.x3, self.y3))
        pygame.draw.line(screen, pygame.Color(0,0,0), (self.x3, self.y3), (self.x4, self.y4))
        pygame.draw.line(screen, pygame.Color(0,0,0), (self.x4, self.y4), (self.x1, self.y1))
	       
if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)
    quad = Quadrilateral(100,100,200,90,200,300,100,300)
    running = True

    while running:
        screen.fill(pygame.Color(255,255,255))
        quad.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.01)
        pygame.display.update()

    pygame.quit()