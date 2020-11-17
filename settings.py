from random import sample

WIDTH = 600
HEIGHT = 600

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTBLUE = (96,216,232)
RED = (255,100,100)
LOCKEDCELLCOLOR = (189,189,189)

#Cells and grid
gridPos = (75, 100)
cellSize = 50
gridSize = cellSize*9

### Boards
solutionBoard =  [[4,6,9,2,5,7,8,3,1],
              [3,5,1,9,8,4,6,7,2],
              [2,8,7,6,1,3,5,4,9],
              [9,4,6,8,3,2,1,5,7],
              [5,7,3,1,9,6,2,8,4],
              [1,2,8,7,4,5,3,9,6],
              [7,3,4,5,6,1,9,2,8],
              [8,1,5,4,2,9,7,6,3],
              [6,9,2,3,7,8,4,1,5]]

originalBoard = [[4,6,9,2,5,7,8,3,1],
              [3,5,1,9,8,4,6,7,2],
              [0,8,7,6,1,3,5,4,9],
              [9,4,6,8,3,2,1,5,7],
              [5,7,3,1,9,6,0,8,4],
              [1,2,8,7,4,5,3,9,6],
              [7,3,4,5,6,1,9,2,8],
              [8,1,5,4,2,9,7,6,3],
              [6,9,0,3,7,8,4,1,5]]




#Variables
base = 3
rBase = range(base)
side = base*base
squares = side*side



##Functions
def pattern(r, c, based):
    return (based*(r%based)+r//based+c)%(based*based)

def randShuffle(s):
    return sample(s, len(s))

def boardGen():
    print("Init: Random board gen")
    rows = [i*base + r for i in randShuffle(rBase) for r in randShuffle(rBase)]
    cols = [i*base + c for i in randShuffle(rBase) for c in randShuffle(rBase)]
    numbers = randShuffle(range(1, (side) + 1))
    temp = []
    for c in cols:
        numbers[pattern(r, c, base)]
        for r in rows:
            temp.append(])
    print(temp)
    return originalBoard



#playingBoard = testBoard2
#testBoard2 = [[0,6,0,2,0,0,8,3,1],
              #[0,0,0,0,8,4,0,0,0],
              #[0,0,7,6,0,3,0,4,9],
              #[0,4,6,8,0,2,1,0,0],
              #[0,0,3,0,9,6,0,0,0],
              #[1,2,0,7,0,5,0,0,6],
              #[7,3,0,0,0,1,0,2,0],
              #[8,1,5,0,2,9,7,0,0],
              #[0,0,0,0,7,0,0,1,5]]

#positions and sizes



