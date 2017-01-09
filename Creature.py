import pygame, math
from Maze import Maze
class Creature(pygame.sprite.Sprite):
    """Something that can move in the maze"""

    STATIONARY = 0
    UP = 1
    RIGHT = 2
    DOWN = -1
    LEFT = -2

    def __init__(self,width,height,speed = 1):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.drawSurface()
        self.image.set_colorkey((0,0,0)) # Make transparent
        self.rect = self.image.get_rect()
        self.speed = speed #Speed in pixels per frame

    def drawSurface(self):
        self.image.fill((255,255,255))

    def update(self):
        #Wrap Around
        if self.rect.x >= Maze.width:
            self.rect.x = 6- Maze.grid_size
        elif self.rect.x <= 0-Maze.grid_size:
            self.rect.x = Maze.width -6
        elif self.rect.y > Maze.height:
            self.rect.y = -16
        elif self.rect.y < -16:
            self.rect.y = Maze.height -1

        #Snap to grid
        if self.direction == Creature.UP or self.direction == Creature.DOWN:
            self.rect.x = Maze.grid_size * round(self.rect.x/Maze.grid_size,0)
        elif self.direction == Creature.LEFT or self.direction == Creature.RIGHT:
            self.rect.y = Maze.grid_size * round(self.rect.y/Maze.grid_size,0)

    def move(self):
        if self.direction == Creature.UP:
            self.rect.y -= self.speed
        elif self.direction == Creature.RIGHT:
            self.rect.x += self.speed
        elif self.direction == Creature.DOWN:
            self.rect.y += self.speed
        elif self.direction == Creature.LEFT:
            self.rect.x -= self.speed

    def getPos(self):
        """Returns the current tile coord based on the centre"""
        #return [math.floor(self.rect.x/Maze.grid_size) + int(Maze.grid_size/2),math.floor(self.rect.y/Maze.grid_size) + int(Maze.grid_size/2)]
        return self.toTile([self.rect.x + int(Maze.grid_size/2),self.rect.y + int(Maze.grid_size/2)])

    def getCornerPos(self):
        """Returns the current tile coord based on the TL Corner"""
        #return [math.floor(self.rect.x/Maze.grid_size) + int(Maze.grid_size/2),math.floor(self.rect.y/Maze.grid_size) + int(Maze.grid_size/2)]
        return self.toTile([self.rect.x,self.rect.y])

    def toTile(self,raw):
        return [math.floor(raw[0]/Maze.grid_size),math.floor(raw[1]/Maze.grid_size)]

    def getFrontPos(self):
        if self.direction == Creature.UP:
            return self.toTile([self.rect.x + int(Maze.grid_size/2),self.rect.y])
        elif self.direction == Creature.RIGHT:
            return self.toTile([self.rect.x + Maze.grid_size -1,self.rect.y + int(Maze.grid_size/2)])
        elif self.direction == Creature.DOWN:
            return self.toTile([self.rect.x + int(Maze.grid_size/2),self.rect.y + Maze.grid_size -1])
        elif self.direction == Creature.LEFT:
            return self.toTile([self.rect.x,self.rect.y + int(Maze.grid_size/2)])
        return self.getPos()
