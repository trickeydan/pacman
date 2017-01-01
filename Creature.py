import pygame
class Creature(pygame.sprite.Sprite):
    """Something that can move in the maze"""
    def __init__(self,width,height,colour):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.speed = 1 #Speed in pixels per frame
