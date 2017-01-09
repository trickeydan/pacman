from Creature import Creature
from Maze import Maze
import pygame, math

class Pac(Creature):
    STATIONARY = 0
    UP = 1
    RIGHT = 2
    DOWN = -1
    LEFT = -2

    currentPos = [0,0]

    def __init__(self,startpos):
        self.startpos = startpos
        super().__init__(16,16)
        self.rect.x = startpos[0]
        self.rect.y = startpos[1]
        Pac.currentPos = startpos
        self.direction = Pac.STATIONARY

    def drawSurface(self):
        pygame.draw.circle(self.image,(255,255,0),[8,8],7)

    def update(self):
        oldpos = self.getFrontPos()
        self.move()
        super().update()

        pos = self.getFrontPos() #Top left tile coord

        if oldpos != pos:
            #Pacman is trying to move into a new square!
            #print(Maze.exits)
            if pos not in Maze.validTiles and oldpos not in Maze.exits and pos not in Maze.exits:
                self.direction = -self.direction
                self.move()
                self.direction = 0
        Pac.currentPos = self.getPos()

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
