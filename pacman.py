def drawLayout(screen):
    screen.fill(BLACK)
    if DEBUG:
        for x in range(0,x_count):
            pygame.draw.line(screen,WHITE,(x*grid_size,0),(x*grid_size,height))
        for y in range(0,y_count):
            pygame.draw.line(screen,WHITE,(0,y*grid_size),(width,y*grid_size))
    for y,row in enumerate(rows):
        for x,char in enumerate(row):

            if char == "%":
                pygame.draw.rect(screen,WALLCOLOUR,[x * grid_size,y*grid_size,grid_size,grid_size])
            elif char == ".":
                pygame.draw.rect(screen,DOTCOLOUR,[x * grid_size,y*grid_size,grid_size,grid_size])
            elif char == "P":
                pygame.draw.rect(screen,(255,255,0),[x * grid_size,y*grid_size,grid_size,grid_size])
            elif char == "o":
                pygame.draw.rect(screen,(255,0,255),[x * grid_size,y*grid_size,grid_size,grid_size])
            elif char == "G":
                pygame.draw.rect(screen,(0,102,255),[x * grid_size,y*grid_size,grid_size,grid_size])

layout_file = "board.layout"
grid_size = 16
DEBUG = True
BLACK = 0,0,0
WHITE = 255,255,255
WALLCOLOUR = WHITE
DOTCOLOUR = 255,0,0

import sys, pygame, os, time
pygame.init()

if(not os.path.exists(layout_file)): sys.exit()
f = open(layout_file)
rows = []
for i,line in enumerate(f):
    rows.append(line.strip())
x_count = len(rows[0])
y_count =len(rows)

screen_size = width, height = int(grid_size * x_count), int(grid_size * y_count)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pacman")

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    drawLayout(screen)

    pygame.display.flip()
    clock.tick(60)
