from random import sample
#Sudoku generation tips https://dlbeer.co.nz/articles/sudoku.html
import tkinter as tk

#GUI integration
root = tk.Tk()
root.title("Sudoku")
root.geometry("400x600")
#greeting = tk.Label(text="Hello, Tkinter")
#greeting.pack()
gameCanvas = tk.Canvas(root)
gameCanvas.place(relwidth=0.1, relheight=0.1)

#table = tk.Frame(window)
#x,y = 0,0
#for row in board:
#    for col in row:
#        create_rectangle(x,y,60,60)
#        x += 60
#    y += 60
#    x = 0
#for i, block_row in enumerate(board):
#    for j, block in enumerate(block_row):
#        block.grid(row=i, column=j)

#greeting.pack()
#Needed to show the window
root.mainloop()



def pattern(r,c,base): 
    return (base*(r%base)+r//base+c)%(base*base)


def randShuffle(s):
    return sample(s,len(s))

#Generates a random sudoku board with solution
def boardGen():
    base = 3
    rBase = range(base)

    print("Initial random sudoku board\n")
    rows = [i*base + r for i in randShuffle(rBase) for r in randShuffle(rBase) ]
    cols = [i*base + c for i in randShuffle(rBase) for c in randShuffle(rBase) ]
    numbers = randShuffle(range(1,(base*base)+1))

    return [ [numbers[pattern(r,c,base)] for c in cols] for r in rows ]

#Generator for playable board, difficulty not integrated
def playBoard(solution):
    base = 3
    side = base*base
    squares = side*side

    board = solution
    empties = squares * 3//4
    for p in sample(range(squares), empties):
        board[p//side][p%side] = 0
    
    #numSize = len(str(side))
    return board

#Generate a random sudoku board
solution = boardGen()
print("This is the solution \n")
for line in solution: print(line)

#Makes the board playable, difficulty not implemented yet..
board = playBoard(solution)
print("This is the playable board\n")
for line in board: print(line)


