import os, pygame
class Maze(object):
    """The Maze class"""
    def __init__(self,layout_file,grid_size):
        self.layout_file = layout_file
        self.grid_size = grid_size

    def setup(self):
        if(not os.path.exists(self.layout_file)): return False
        f = open(self.layout_file)
        self.rows = []
        for i,line in enumerate(f):
            self.rows.append(line.strip())
        self.x_count = len(self.rows[0])
        self.y_count =len(self.rows)
        screen_size = self.width, self.height = int(self.grid_size * self.x_count), int(self.grid_size * self.y_count)
        self.screen = pygame.display.set_mode(screen_size)
        return True

    def drawLayout(self):

        self.screen.fill((0,0,0))
        if False:
            for x in range(0,self.x_count):
                pygame.draw.line(self.screen,(255,255,255),(x*self.grid_size,0),(x*self.grid_size,self.height))
            for y in range(0,self.y_count):
                pygame.draw.line(self.screen,(255,255,255),(0,y*self.grid_size),(self.width,y*self.grid_size))
        for y,row in enumerate(self.rows):
            for x,char in enumerate(row):

                if char == "%":
                    pygame.draw.rect(self.screen,(255,255,255),[x * self.grid_size,y*self.grid_size,self.grid_size,self.grid_size])
                elif char == ".":
                    pygame.draw.circle(self.screen,(255,0,0),[int((x+0.5) * self.grid_size),int((y+0.5) * self.grid_size)],2,0)
                elif char == "P":
                    pygame.draw.rect(self.screen,(255,255,0),[x * self.grid_size,y*self.grid_size,self.grid_size,self.grid_size])
                elif char == "o":
                    pygame.draw.circle(self.screen,(255,0,255),[int((x+0.5) * self.grid_size),int((y+0.5) * self.grid_size)],4,0)
                elif char == "G":
                    pygame.draw.rect(self.screen,(0,102,255),[x * self.grid_size,y*self.grid_size,self.grid_size,self.grid_size])
