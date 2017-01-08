from Creature import Creature
from Maze import Maze
import pygame, math

class Ghost(Creature):
    STATIONARY = 0
    UP = 1
    RIGHT = 2
    DOWN = -1
    LEFT = -2

    def __init__(self,startpos,number):
        self.startpos = startpos
        super().__init__(16,16)
        self.rect.x = startpos[0]
        self.rect.y = startpos[1]
        self.number = number
        self.active = False

    def drawSurface(self):
        self.image.fill((0,102,255))
    def update(self):
        super().update()

        if not self.active and Maze.SCORE >= (self.number * 50):
            self.active = True
            print("Ghost Activated")
