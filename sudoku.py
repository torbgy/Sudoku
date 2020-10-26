import numpy as np
#Sudoku generation tips https://dlbeer.co.nz/articles/sudoku.html

print("Initial random sudoku board")

#Generate empty board
board = np.zeros((9,9))
print(board)
#pos_val = [1,2,3,4,5,6,7,8,9]

#setting first box to random numbers
rng = np.random.default_rng()
randomFirst = rng.choice(9,size=9, replace=False)
randomFirstMod = [i+1 for i in randomFirst]
#print(randomFirst)
for x in range(3):
    for y in range(3):
        board[x][y] = randomFirstMod[y]
    randomFirstMod = np.delete(randomFirstMod, [0,1,2])

randomFirstMod = [i+1 for i in randomFirst]
y = 0
k= 0
for x in range(3):
    notInBoard = ~np.in1d(randomFirstMod,board[:3][k])
    notInBoard = np.array(randomFirstMod)[notInBoard]
    for y in range(3):        
        #notInBoard = np.setdiff1d(randomFirstMod,board[:3][y])
        board[x][y+3] = notInBoard[y]
    k += 1
    test = ~np.in1d(randomFirstMod,notInBoard[:3])
    randomFirstMod = np.array(randomFirstMod)[test]
    #randomFirstMod = np.delete(randomFirstMod,np.where([randomFirstMod == k for k in notInBoard[:2]]))
    
print(board)
print(randomFirstMod)


#board[0][:3] = randomFirst[:3]
#randomFirst = np.delete(randomFirst, [1,2,3])
