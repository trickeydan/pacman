#! /usr/bin/python3
layout_file = "board.layout"
grid_size = 16
DEBUG = True


import sys, pygame, os, time
from Creature import Creature
from Maze import Maze
from Pac import Pac
from Ghost import Ghost
pygame.init()

maze = Maze(layout_file,grid_size)
maze.setup()

all_sprites_list = pygame.sprite.Group()
pac = Pac(maze.getPacStart())
all_sprites_list.add(pac)

for pos in maze.getGhostStart():
    ghost = Ghost(pos)
    all_sprites_list.add(ghost)


score = 0
clock = pygame.time.Clock()


while 1:
    pygame.display.set_caption("Pacman Score: " + str(score))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pac.keys(event)

    all_sprites_list.update()
    Maze.food.update()

    food_eaten = pygame.sprite.spritecollide(pac,Maze.food, True)
    score += len(food_eaten)

    maze.drawLayout()
    maze.drawSprites(Maze.food)
    maze.drawSprites(all_sprites_list)

    pygame.display.flip()
    clock.tick(60)
