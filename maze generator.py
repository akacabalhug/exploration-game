import pygame as p
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

p.init()
mazeSize = (500, 500)
maze = p.display.set_mode(mazeSize)
fpsClock = p.time.Clock()

cellSize = 25
rowNum = int(mazeSize[0]/cellSize)
colNum = int(mazeSize[1]/cellSize)

mazeGrid = []
currentCell = 0

stack = []

def index(x, y):
    if x < 0 or y < 0 or x > (colNum - 1) or y > (rowNum - 1):
        return False
    else:
        return x + y * colNum
 
class Cell(object):

    global mazeGrid

    def __init__(self, row, col):
        self.xCor = col
        self.yCor = row
        self.scaledX = col * cellSize
        self.scaledY = row * cellSize
        self.walls = [True, True, True, True]
        self.wall = True
        self.visited = False
        self.current = False
        self.neighbors = []
        
    def showCell(self):
        if self.walls[0]:
            p.draw.line(maze, WHITE, (self.scaledX, self.scaledY),(self.scaledX + cellSize, self.scaledY), 1)
        if self.walls[1]:
            p.draw.line(maze, WHITE, (self.scaledX + cellSize, self.scaledY), (self.scaledX + cellSize, self.scaledY + cellSize), 1)
        if self.walls[2]:
            p.draw.line(maze, WHITE, (self.scaledX + cellSize, self.scaledY + cellSize), (self.scaledX, self.scaledY + cellSize), 1)
        if self.walls[3]:
            p.draw.line(maze, WHITE, (self.scaledX, self.scaledY + cellSize), (self.scaledX, self.scaledY), 1)

    def highlightCurrentCell(self):
        if self.current:
            p.draw.rect(maze, PURPLE, (self.scaledX, self.scaledY, cellSize, cellSize))

    def drawCell(self):
        if self.visited:
            p.draw.rect(maze, BLUE, (self.scaledX, self.scaledY, cellSize, cellSize))
        
    def checkNeighbors(self):
        self.top = mazeGrid[ index( self.xCor, self.yCor - 1 ) ]
        self.right = mazeGrid[ index( self.xCor + 1, self.yCor ) ]
        self.bottom = mazeGrid[ index( self.xCor, self.yCor + 1 ) ]
        self.left = mazeGrid[ index( self.xCor - 1, self.yCor ) ]

        if self.top != 0 and self.top.visited == False and self.top.wall == True:
            self.neighbors.append(self.top)
        if self.right != 0 and self.right.visited == False and self.right.wall == True:
            self.neighbors.append(self.right)
        if self.bottom != 0 and self.bottom.visited == False and self.bottom.wall == True:
            self.neighbors.append(self.bottom)
        if self.left != 0 and self.left.visited == False and self.left.wall == True:
            self.neighbors.append(self.left)

        if len(self.neighbors) > 0:
            self.nextCell = random.choice(self.neighbors)
            self.neighbors.remove(self.nextCell)
            for cell in self.neighbors:
                cell.wall = True
            return self.nextCell
        else:
            return None

    def removeWalls(self, currentCell, nextCell):
        positionX = currentCell.xCor - nextCell.xCor

        if positionX == 1:
            currentCell.walls[3] = False
            nextCell.walls[1] = False
            currentCell.wall = False
            nextCell.wall = False
        elif positionX == -1:
            currentCell.walls[1] = False
            nextCell.walls[3] = False
            currentCell.wall = False
            nextCell.wall = False

        positionY = currentCell.yCor - nextCell.yCor

        if positionY == 1:
            currentCell.walls[0] = False
            nextCell.walls[2] = False
            currentCell.wall = False
            nextCell.wall = False
            
        elif positionY == -1:
            currentCell.walls[2] = False
            nextCell.walls[0] = False
            currentCell.wall = False
            nextCell.wall = False
        

for row in range(rowNum):
    for col in range(colNum):
        cell = Cell(row,col)
        mazeGrid.append(cell)

    currentCell = mazeGrid[0]


p.display.update()

while True:
    fpsClock.tick(5)

    currentCell.current = True

    for cell in range(len(mazeGrid)):
        mazeGrid[cell].drawCell()

    for cell in range(len(mazeGrid)):
        mazeGrid[cell].showCell()

    currentCell.visited = True

    currentCell.highlightCurrentCell()
    nextCell = currentCell.checkNeighbors()
    
    if nextCell:
        nextCell.visited = True
        stack.append(currentCell)
        
        nextCell.removeWalls(currentCell, nextCell)
        
        currentCell = nextCell

    elif len(stack) > 0:
        currentCell = stack.pop()
        
        

    for event in p.event.get():
        if event.type == QUIT:
            p.quit()
            sys.exit()

    p.display.update()

