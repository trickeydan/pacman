layout_file = "board.layout"
grid_size = 16
DEBUG = True


import sys, pygame, os, time
from Creature import Creature
from Maze import Maze
pygame.init()

maze = Maze(layout_file,grid_size)
maze.setup()
pygame.display.set_caption("Pacman")

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    maze.drawLayout()

    pygame.display.flip()
    clock.tick(60)
