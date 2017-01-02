import pygame, math

class Food(pygame.sprite.Sprite):
    """An item of food."""
    def __init__(self,width,height,colour):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
