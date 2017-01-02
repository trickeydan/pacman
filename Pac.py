from Creature import Creature
from Maze import Maze
import pygame, math

class Pac(Creature):
    STATIONARY = 0
    UP = 1
    RIGHT = 2
    DOWN = -1
    LEFT = -2

    def __init__(self,startpos):
        self.startpos = startpos
        super().__init__(16,16,(255,255,0))
        self.rect.x = startpos[0]
        self.rect.y = startpos[1]
        self.direction = Pac.STATIONARY

    def update(self):
        oldpos = self.getFrontPos()
        self.move()
        super().update()

        pos = self.getFrontPos() #Top left tile coord

        if self.direction == Pac.UP or self.direction == Pac.DOWN:
            self.rect.x = Maze.grid_size * round(self.rect.x/Maze.grid_size,0)
        elif self.direction == Pac.LEFT or self.direction == Pac.RIGHT:
            self.rect.y = Maze.grid_size * round(self.rect.y/Maze.grid_size,0)

        if oldpos != pos:
            #Pacman is trying to move into a new square!
            if pos not in Maze.validTiles:
                self.direction = -self.direction
                self.move()
                self.direction = 0

    def move(self):
        if self.direction == Pac.UP:
            self.rect.y -= self.speed
        elif self.direction == Pac.RIGHT:
            self.rect.x += self.speed
        elif self.direction == Pac.DOWN:
            self.rect.y += self.speed
        elif self.direction == Pac.LEFT:
            self.rect.x -= self.speed

    def keys(self,event):
        if event.scancode == 111 or event.scancode == 25: #UP
            self.setDirectionWC(Pac.UP)
        elif event.scancode == 114 or event.scancode == 40: #RIGHT
            self.setDirectionWC(Pac.RIGHT)
        elif event.scancode == 116 or event.scancode == 39: #DOWN
            self.setDirectionWC(Pac.DOWN)
        elif event.scancode == 113 or event.scancode == 38: #LEFT
            self.setDirectionWC(Pac.LEFT)

    def setDirectionWC(self,direction):
        if direction != self.direction:
            pos = self.getFrontPos()
            if direction == Pac.UP: #UP
                pos[1] -= 1
                if pos in Maze.validTiles:
                    self.direction = Pac.UP
            elif direction == Pac.RIGHT: #RIGHT
                pos[0] += 1
                if pos in Maze.validTiles:
                    self.direction = Pac.RIGHT
            elif direction == Pac.DOWN: #DOWN
                pos[1] += 1
                if pos in Maze.validTiles:
                    self.direction = Pac.DOWN
            elif direction == Pac.LEFT: #LEFT
                pos[0] -= 1
                if pos in Maze.validTiles:
                    self.direction = Pac.LEFT

    def getFrontPos(self):
        if self.direction == Pac.UP:
            return self.toTile([self.rect.x + int(Maze.grid_size/2),self.rect.y])
        elif self.direction == Pac.RIGHT:
            return self.toTile([self.rect.x + Maze.grid_size -1,self.rect.y + int(Maze.grid_size/2)])
        elif self.direction == Pac.DOWN:
            return self.toTile([self.rect.x + int(Maze.grid_size/2),self.rect.y + Maze.grid_size -1])
        elif self.direction == Pac.LEFT:
            return self.toTile([self.rect.x,self.rect.y + int(Maze.grid_size/2)])
        return self.getPos()
