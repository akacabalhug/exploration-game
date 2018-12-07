from pygame.locals import *
import pygame as p
import sys
import random

class MazeGrid(object):
    def __init__(self):
        self._size = (20,10)
        


class Maze(object):
    def __init__(self, maze):
        self.rowNum = 11
        
        self.colNum = 41
        self.maze = maze

    def draw(self, display_surf, vertical_block, horizontal_block):
        blockX = 0
        blockY = 0
        for i in range(0, self.rowNum * self.colNum):
            if self.maze[blockX + (blockY * self.colNum)] == "|":
                display_surf.blit(vertical_block, ( blockX * 25, blockY * 25))

            elif self.maze[blockX + (blockY * self.colNum)] == "_":
                display_surf.blit(horizontal_block, ( blockX * 25, blockY * 25))

            blockX = blockX + 1
            if blockX > self.colNum - 1:
                blockX = 0
                blockY = blockY + 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

p.init()
mazeSize = (1025, 275)

display_surf = p.display.set_mode(mazeSize)
fpsClock = p.time.Clock()

p.display.set_caption('Exploration Game')
player = p.image.load("student_front.gif").convert()
vertical_block = p.image.load("Sprites//block.gif").convert()
horizontal_block = p.image.load("Sprites//hBlock.png").convert()

maze = []
mazefh = open("maze.txt")
for line in mazefh:
    maze += tuple(line.rstrip("\n"))
mazefh.close()

mazeGrid = Maze(maze)


print(len(maze))
ctr = 0
for item in maze:
    ctr += 1
    print(item, end="")
    if ctr == 41:
        print("")
        ctr = 0

while True:
    fpsClock.tick(5)
    for event in p.event.get():
        if event.type == QUIT:
            p.quit()
            sys.exit()
            
    mazeGrid.draw(display_surf, vertical_block, horizontal_block)

    #p.display.flip()
    p.display.update()

