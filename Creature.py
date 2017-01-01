import pygame, math
from Maze import Maze
class Creature(pygame.sprite.Sprite):
    """Something that can move in the maze"""
    def __init__(self,width,height,colour):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.speed = 1 #Speed in pixels per frame

    def update(self):
        #Wrap around
        if self.rect.x > Maze.width:
            self.rect.x = -16
        elif self.rect.x < -16:
            self.rect.x = Maze.width -1
        elif self.rect.y > Maze.height:
            self.rect.y = -16
        elif self.rect.y < -16:
            self.rect.y = Maze.height -1

    def getPos(self):
        """Returns the current tile coord"""
        return [math.floor(self.rect.x/Maze.grid_size) + int(Maze.grid_size/2),math.floor(self.rect.y/Maze.grid_size) + int(Maze.grid_size/2)]
