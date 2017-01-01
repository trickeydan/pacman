from Creature import Creature
from Maze import Maze
import pygame, math

class Pac(Creature):
    STATIONARY = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def __init__(self,startpos):
        self.startpos = startpos
        super().__init__(16,16,(255,255,0))
        self.rect.x = startpos[0]
        self.rect.y = startpos[1]
        self.direction = Pac.STATIONARY

    def update(self):
        #Update position from direction
        if self.direction == Pac.UP:
            self.rect.y -= self.speed
        elif self.direction == Pac.RIGHT:
            self.rect.x += self.speed
        elif self.direction == Pac.DOWN:
            self.rect.y += self.speed
        elif self.direction == Pac.LEFT:
            self.rect.x -= self.speed
        super().update()

        pos = self.getPos()
        if self.direction == Pac.UP or self.direction == Pac.DOWN:
            self.rect.x = Maze.grid_size * round(self.rect.x/Maze.grid_size,0)
        elif self.direction == Pac.LEFT or self.direction == Pac.RIGHT:
            self.rect.y = Maze.grid_size * round(self.rect.y/Maze.grid_size,0)
