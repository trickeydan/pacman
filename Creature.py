import pygame, math
from Maze import Maze
class Creature(pygame.sprite.Sprite):
    """Something that can move in the maze"""
    def __init__(self,width,height,speed = 1):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.drawSurface()
        self.rect = self.image.get_rect()
        self.speed = speed #Speed in pixels per frame

    def drawSurface(self):
        self.image.fill((255,255,255))

    def update(self):
        if self.rect.x >= Maze.width:
            self.rect.x = 6- Maze.grid_size
        elif self.rect.x <= 0-Maze.grid_size:
            self.rect.x = Maze.width -6
        elif self.rect.y > Maze.height:
            self.rect.y = -16
        elif self.rect.y < -16:
            self.rect.y = Maze.height -1

    def getPos(self):
        """Returns the current tile coord"""
        #return [math.floor(self.rect.x/Maze.grid_size) + int(Maze.grid_size/2),math.floor(self.rect.y/Maze.grid_size) + int(Maze.grid_size/2)]
        return self.toTile([self.rect.x + int(Maze.grid_size/2),self.rect.y + int(Maze.grid_size/2)])

    def toTile(self,raw):
        return [math.floor(raw[0]/Maze.grid_size),math.floor(raw[1]/Maze.grid_size)]
