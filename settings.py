from random import sample
from copy import deepcopy

##Window size
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




#Global variables
base = 3
randBase = range(base)
side = base*base
squares = side*side


##Functions
def pattern(r, c):
    #Check for patterns
    return (base*(r%base)+r//base+c)%(base*base)

def randShuffle(s):
    #Returns a random sample of length 3 e.g. [1, 4, 2]
    return sample(s, len(s))


def boardGen():
    print("Init: Random board gen")
    rows = []
    cols = []
    solution = []
    for r in randShuffle(randBase):
        for i in randShuffle(randBase):
            rows.append(i*base + r + 1)

    for c in randShuffle(randBase):
        for i in randShuffle(randBase):
            cols.append(i*base + c + 1)

    numbers = randShuffle(range(1,(base*base)+1))
 
    for c in cols:
        tempRow = []
        for r in rows:
            tempRow.append(numbers[pattern(r, c)])
        solution.append(tempRow)
    print("solution generated")
    return solution

def playGen(original):
    print("Creating playing board")
    playBoard = deepcopy(original)
    empties = squares * 3//4

    for i in sample(range(squares), empties):
        playBoard[i//side][i%side] = 0
    return playBoard


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



