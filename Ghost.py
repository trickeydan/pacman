from Creature import Creature
from Maze import Maze
import pygame, math

class Ghost(Creature):
    STATIONARY = 0
    UP = 1
    RIGHT = 2
    DOWN = -1
    LEFT = -2

    def __init__(self,startpos):
        self.startpos = startpos
        super().__init__(16,16)
        self.rect.x = startpos[0]
        self.rect.y = startpos[1]

    def drawSurface(self):
        self.image.fill((0,102,255))
