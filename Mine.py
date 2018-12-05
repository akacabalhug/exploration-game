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
size = (700, 700)
MAZEGAME = p.display.set_mode(size)
fpsclock = p.time.Clock()

big = 35
row = int(size[0]/big)
col = int(size[1]/big)

mazegrid = []
current_cell = 0

stack = []

def index(x, y):
    if x < 0 or y < 0 or x > (col - 1) or y > (row - 1):
        return False
    else:
        return x + y * col

class blockcreate():
    global mazegrid

    def __init__( self, x, y ):
        self.realx = x
        self.realy = y
        self.x = x*big
        self.y = y*big
        self.visited = False
        self.current = False
        self.neighbors = []
        self.wall = False

    def draw( self ):
        if self.current:
            p.draw.rect(MAZEGAME, BLUE, (self.x, self.y, big, big))
        if self.visited:
            p.draw.rect(MAZEGAME, PURPLE, (self.x, self.y, big, big) )

    def show(self):
        p.draw.rect( MAZEGAME, GREEN, (self.x, self.y, big, big), 1 )

    def checkneighbors( self ):
        self.top    = mazegrid[ index(self.realx, self.realy - 1) ]
        self.right  = mazegrid[ index(self.realx + 1, self.realy) ]
        self.bottom = mazegrid[ index(self.realx, self.realy + 1) ]
        self.left   = mazegrid[ index(self.realx - 1, self.realy) ]

        if self.top != 0:
            if self.top.visited == False and self.top.wall == False:
                self.neighbors.append( self.top )
        if self.right != 0:
            if self.right.visited == False and self.right.wall == False:
                self.neighbors.append( self.right )
        if self.bottom != 0:
            if self.bottom.visited == False and self.bottom.wall == False:
                self.neighbors.append( self.bottom )
        if self.left != 0:
            if self.left.visited == False and self.left.wall == False:
                self.neighbors.append( self.left )

        if len(self.neighbors) > 0:
            self.nextone = random.choice(self.neighbors)
            self.neighbors.remove(self.nextone)
            for x in self.neighbors:
                x.wall = True
            return self.nextone
        else:
            return stack.pop()

for y in range(row):
    for x in range(col):
        block = blockcreate(x, y)
        mazegrid.append(block)

    current_cell = mazegrid[0]

for x in range( len( mazegrid ) ):
    mazegrid[ x ].show()


p.display.update()

while True:
    fpsclock.tick( 20 )

    current_cell.current = True

    for x in range( len( mazegrid ) ):
        mazegrid[ x ].draw()

    current_cell.visited = True

    nextone = current_cell.checkneighbors()
    print(nextone)
    if nextone != False:
        stack.append(current_cell)
        current_cell = nextone

    # elif len(stack) > 0:
    #     current_cell = stack.pop()

    for event in p.event.get():
        if event.type == QUIT:
            p.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                p.quit()
                sys.exit()

    p.display.update()