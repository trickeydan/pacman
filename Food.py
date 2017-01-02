import pygame, math

class Food(pygame.sprite.Sprite):
    """An item of food."""
    def __init__(self,radius):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2])
        pygame.draw.circle(self.image,(255,0,0),[radius,radius],radius)
        #self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
