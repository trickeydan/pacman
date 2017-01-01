def drawGame(screen):
    screen.fill(BLACK)
    if DEBUG:
        for x in range(0,int(width/grid_size)):
            pygame.draw.line(screen,WHITE,(x*grid_size,0),(x*grid_size,height))
        for y in range(0,int(height/grid_size)):
            pygame.draw.line(screen,WHITE,(0,y*grid_size),(width,y*grid_size))
    #Draw walls
    for wall in walls:
        pygame.draw.rect(screen,WALLCOLOUR,[wall[0] * grid_size,wall[1] * grid_size,wall[2] * grid_size+1,wall[3] *grid_size+1])
    for door in ghost_door:
        pygame.draw.rect(screen,GHOSTDOOR_COLOUR,[door[0] * grid_size,door[1] * grid_size,door[2] * grid_size+1,door[3] *grid_size +1])

import sys, pygame, time
pygame.init()

grid_size = 16 #Size of a grid square in pixels
screen_size = width, height = int(224 *(grid_size/8)), int(288*(grid_size/8))
walls = [ \
[0,3,28,1],[0,4,1,8],[13,3,2,5],[27,4,1,8], \
[2,5,4,3],[7,5,5,3],[16,5,5,3],[22,5,4,3], \
[2,9,4,2],[7,9,2,8],[10,9,8,2],[19,9,2,8], \
[22,9,4,2],[0,12,6,1],[9,12,3,2],[16,12,3,2], \
[22,12,6,1],[5,13,1,3],[22,13,1,3],[0,16,6,1], \
[22,16,6,1],[10,15,3,1],[15,15,3,1],[10,16,1,3], \
[17,16,1,3],[10,19,8,1]
]
ghost_door = [[13,15,2,1]]
BLACK = 0, 0, 0
WHITE = 255,255,255
WALLCOLOUR = WHITE
GHOSTDOOR_COLOUR = 255,0,0
DEBUG = True

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pacman")

#ball = pygame.image.load("ball.gif")
#ballrect = ball.get_rect()

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #ballrect = ballrect.move(speed)
    #if ballrect.left < 0 or ballrect.right > width:
    #    speed[0] = -speed[0]
    #if ballrect.top < 0 or ballrect.bottom > height:
    #    speed[1] = -speed[1]
    drawGame(screen)
    #screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(60)
