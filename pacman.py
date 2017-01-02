#! /usr/bin/python3
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

all_sprites_list = pygame.sprite.Group()
pac = Pac(maze.getPacStart())
all_sprites_list.add(pac)

clock = pygame.time.Clock()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pac.keys(event)

    all_sprites_list.update()

    maze.drawLayout()
    maze.drawSprites(all_sprites_list)

    pygame.display.flip()
    clock.tick(60)
