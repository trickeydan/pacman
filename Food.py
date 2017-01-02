import pygame, math

class Food(pygame.sprite.Sprite):
    """An item of food."""
    def __init__(self,radius,colour):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2])
        pygame.draw.circle(self.image,colour,[radius,radius],radius)
        self.rect = self.image.get_rect()
