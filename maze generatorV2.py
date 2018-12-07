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

cellSize = 50
rowNum = int(mazeSize[0]/cellSize)
colNum = int(mazeSize[1]/cellSize)

mazeGrid = []
visitCount = 0

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

        self.visited = False
        self.current = False
        self.neighbors = []
        
    def showCell(self):
        if self.walls[0]:
            p.draw.line(maze, BLACK, (self.scaledX-7, self.scaledY),(self.scaledX + cellSize +7, self.scaledY), 15)
        if self.walls[1]:
            p.draw.line(maze, BLACK, (self.scaledX + cellSize, self.scaledY-7), (self.scaledX + cellSize, self.scaledY + cellSize+7), 15)
        if self.walls[2]:
            p.draw.line(maze, BLACK, (self.scaledX + cellSize, self.scaledY + cellSize), (self.scaledX, self.scaledY + cellSize), 15)
        if self.walls[3]:
            p.draw.line(maze, BLACK, (self.scaledX, self.scaledY + cellSize), (self.scaledX, self.scaledY), 15)

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

        if self.top != 0 and self.top.visited == False:
            self.neighbors.append(self.top)
        if self.right != 0 and self.right.visited == False:
            self.neighbors.append(self.right)
        if self.bottom != 0 and self.bottom.visited == False:
            self.neighbors.append(self.bottom)
        if self.left != 0 and self.left.visited == False:
            self.neighbors.append(self.left)

        if len(self.neighbors) > 0:
            self.nextCell = random.choice(self.neighbors)
            return self.nextCell
        else:
            return False

    def removeWalls(self, currentCell, nextCell):
        positionX = currentCell.xCor - nextCell.xCor

        if positionX == 1:
            currentCell.walls[3] = False
            nextCell.walls[1] = False

        elif positionX == -1:
            currentCell.walls[1] = False
            nextCell.walls[3] = False

        positionY = currentCell.yCor - nextCell.yCor

        if positionY == 1:
            currentCell.walls[0] = False
            nextCell.walls[2] = False

        elif positionY == -1:
            currentCell.walls[2] = False
            nextCell.walls[0] = False

for row in range(rowNum):
    for col in range(colNum):
        cell = Cell(row,col)
        mazeGrid.append(cell)

    currentCell = mazeGrid[0]

while doneNa == False:
    # fpsClock.tick(60)

    visitCount = 0

    currentCell.current = True

    for cell in range(len(mazeGrid)):
        mazeGrid[cell].drawCell()

    for cell in range(len(mazeGrid)):
        mazeGrid[cell].showCell()

    currentCell.visited = True

    for x in mazeGrid:
        if x.visited == True:
            visitCount += 1
    if visitCount == len(mazeGrid):
        for cell in range( len( mazeGrid ) ):
            mazeGrid[ cell ].drawCell()

        for cell in range( len( mazeGrid ) ):
            mazeGrid[ cell ].showCell()
        break
    print(visitCount, len(mazeGrid))

    currentCell.highlightCurrentCell()

    nextCell = currentCell.checkNeighbors()

    # p.display.update()
    print(nextCell)

    if nextCell != False:
        currentCell.neighbors = []

        stack.append(currentCell)

        nextCell.removeWalls(currentCell, nextCell)

        currentCell = nextCell

    elif len(stack) > 0:
        currentCell = stack.pop()

    for event in p.event.get():
        if event.type == QUIT:
            p.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                p.quit()
                sys.exit()

p.display.update()

while True:
    for event in p.event.get():
        if event.type == QUIT:
            p.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                p.quit()
                sys.exit()
    p.display.update()

