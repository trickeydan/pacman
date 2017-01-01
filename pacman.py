layout_file = "board.layout"
grid_size = 16
DEBUG = True


import sys, pygame, os, time
from Creature import Creature
from Maze import Maze
from Pac import Pac
pygame.init()

maze = Maze(layout_file,grid_size)
maze.setup()
pygame.display.set_caption("Pacman")

clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()

pac = Pac(maze.getPacStart())
all_sprites_list.add(pac)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.scancode == 111 or event.scancode == 25:
                pac.direction = Pac.UP
            elif event.scancode == 114 or event.scancode == 40:
                pac.direction = Pac.RIGHT
            elif event.scancode == 116 or event.scancode == 39:
                pac.direction = Pac.DOWN
            elif event.scancode == 113 or event.scancode == 38:
                pac.direction = Pac.LEFT
    all_sprites_list.update()

    maze.drawLayout()
    maze.drawSprites(all_sprites_list)

    pygame.display.flip()
    clock.tick(60)
