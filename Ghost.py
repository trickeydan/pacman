from Creature import Creature
from Maze import Maze
from Pac import Pac
import pygame, math

class Ghost(Creature):

    SCATTER = 0
    CHASE = 1
    FRIGHTENED = 2

    BLINKY = 0
    COLOURS = [(255,95,95),(255,184,255),(1,255,255),(255,184,81)]

    def __init__(self,startpos,number):
        self.startpos = startpos
        self.number = number
        super().__init__(16,16)
        self.rect.x = startpos[0]
        self.rect.y = startpos[1]
        self.active = False
        self.target = [0,0]
        self.mode = Ghost.CHASE

    def drawSurface(self):
        self.image.fill(Ghost.COLOURS[self.number])

    def update(self):
        super().update()

        if not self.active and Maze.SCORE >= (self.number * 50):
            self.active = True

        if self.active:
            if self.mode == Ghost.CHASE:
                if self.number == Ghost.BLINKY:
                    self.target = Pac.currentPos
                    self.advanceTarget()
                else:
                    print("Ghost Active but has no programming.")
            else:
                print("Ghost in unimplemented state!")

    def advanceTarget(self):
        current = self.getPos()
        up = [current[0],current[1] -1]
        left = [current[0] -1,current[1]]
        down = [current[0],current[1] + 1]
        right = [current[0] + 1,current[1]]
        available = []
        if up in Maze.validTiles:
            available.append([up,"UP"])
        if left in Maze.validTiles:
            available.append([left,"LEFT"])
        if down in Maze.validTiles:
            available.append([down,"DOWN"])
        if right in Maze.validTiles:
            available.append([right,"RIGHT"])

        lowest = 1000
        diret = "NONE"
        for direction in available:
            dist = ((self.target[0] - direction[0][0])** 2 + (self.target[1] - direction[0][1])** 2)** 0.5
            if dist < lowest:
                diret = direction[1]
            print(diret)
