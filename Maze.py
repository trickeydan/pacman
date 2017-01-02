import os, pygame
from Food import Food
class Maze(object):
    """The Maze class"""
    def __init__(self,layout_file,grid_size):
        self.layout_file = layout_file
        Maze.grid_size = grid_size


    def setup(self):
        if(not os.path.exists(self.layout_file)): return False
        f = open(self.layout_file)
        self.rows = []
        for i,line in enumerate(f):
            self.rows.append(line.strip())
        self.x_count = len(self.rows[0])
        self.y_count =len(self.rows)
        screen_size = Maze.width, Maze.height = int(Maze.grid_size * self.x_count), int(Maze.grid_size * self.y_count)
        self.screen = pygame.display.set_mode(screen_size)

        #Define permitted positions
        Maze.validTiles = []
        Maze.food = pygame.sprite.Group()
        for y,row in enumerate(self.rows):
            for x,char in enumerate(row):
                if char in ["E",".","P","o"]:
                    Maze.validTiles.append([x,y])
                if char == ".":
                    food = Food(2,(255,0,0))
                    food.rect.x = int((x+0.5) * Maze.grid_size) -1
                    food.rect.y = int((y+0.5) * Maze.grid_size) -1
                    Maze.food.add(food)
                elif char == "o":
                    energizer = Food(4,(255,0,255))
                    energizer.rect.x = int((x+0.5) * Maze.grid_size) -4
                    energizer.rect.y = int((y+0.5) * Maze.grid_size) -4
                    Maze.food.add(energizer)
        return True

    def drawLayout(self):
        self.screen.fill((0,0,0))
        if False:
            for x in range(0,self.x_count):
                pygame.draw.line(self.screen,(255,255,255),(x*Maze.grid_size,0),(x*Maze.grid_size,Maze.height))
            for y in range(0,self.y_count):
                pygame.draw.line(self.screen,(255,255,255),(0,y*Maze.grid_size),(Maze.width,y*Maze.grid_size))
        for y,row in enumerate(self.rows):
            for x,char in enumerate(row):

                if char == "%":
                    pygame.draw.rect(self.screen,(255,255,255),[x * Maze.grid_size,y*Maze.grid_size,Maze.grid_size,Maze.grid_size])
                elif char == "G":
                    pygame.draw.rect(self.screen,(0,102,255),[x * Maze.grid_size,y*Maze.grid_size,Maze.grid_size,Maze.grid_size])

    def getPacStart(self):
        for y,row in enumerate(self.rows):
            for x,char in enumerate(row):
                if char == "P":
                    return [x * Maze.grid_size,y*Maze.grid_size]

    def drawSprites(self,list):
        list.draw(self.screen)
