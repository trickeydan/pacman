from Creature import Creature
from Maze import Maze
from Pac import Pac
import pygame, math, time

class Ghost(Creature):

    SCATTER = 0
    CHASE = 1
    FRIGHTENED = 2

    BLINKY = 0
    COLOURS = [(255,95,95),(255,184,255),(1,255,255),(255,184,81)]

    def __init__(self,startpos,number):
        self.startpos = startpos
        self.nextSquare = self.toTile(startpos)
        self.number = number
        super().__init__(16,16)
        self.rect.x = startpos[0]
        self.rect.y = startpos[1]
        self.active = False
        self.target = [0,0]
        self.mode = Ghost.CHASE
        self.direction = Creature.STATIONARY

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

                    if self.nextSquare == self.getPos():
                        #time.sleep(1)
                        self.chooseDirection()

                else:
                    #print("Ghost Active but has no programming.")
                    pass
            else:
                print("Ghost in unimplemented state!")
            self.move()


    def chooseDirection(self):
        current = self.getCornerPos()
        up = [current[0],current[1] -1]
        left = [current[0] -1,current[1]]
        down = [current[0],current[1] + 1]
        right = [current[0] + 1,current[1]]
        available = []
        if up in Maze.validTiles:
            available.append([up,Creature.UP])
        if left in Maze.validTiles:
            available.append([left,Creature.LEFT])
        if down in Maze.validTiles:
            available.append([down,Creature.DOWN])
        if right in Maze.validTiles:
            available.append([right,Creature.RIGHT])

        lowest = 1000
        diret = Creature.STATIONARY
        self.nextSquare = self.getCornerPos()
        for direction in available:
            dist = ((self.target[0] - direction[0][0])** 2 + (self.target[1] - direction[0][1])** 2)** 0.5
            if dist < lowest:
                lowest = dist
                closest = direction
                
        self.nextSquare = closest[0]
        self.direction = closest[1]
