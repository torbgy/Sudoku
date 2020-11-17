import pygame, sys
from copy import deepcopy
from settings import *
from buttonClass import *

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.solution = boardGen()
        self.original = playGen(self.solution)
        self.grid = deepcopy(self.original)
        self.selected = None
        self.mousePos = None
        self.state = "playing"
        self.finished = False
        self.cellChanged = False
        self.playingButtons = []
        self.menuButtons = []
        self.endButtons = []
        self.lockedCells = []
        self.incorrectCells = []
        self.font = pygame.font.SysFont("arial", cellSize//2, True)
        self.load()


    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()            
        pygame.quit()
        sys.exit()


### Playing state functions

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # User clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    self.selected = selected
                else:
                    self.selected = None
                    for button in self.playingButtons:
                        if button.highlighted:
                            button.click()

            
            # User input
            if event.type == pygame.KEYDOWN:
                if self.selected != None and self.selected not in self.lockedCells:
                    if self.isInt(event.unicode):
                        self.grid[self.selected[1]][self.selected[0]] = int(event.unicode)
                        self.cellChanged = True
                    elif event.key == 8: #Clear selected cell
                        self.grid[self.selected[1]][self.selected[0]] = 0
                        
    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.playingButtons:
            button.update(self.mousePos)

    def playing_draw(self):
        self.window.fill(WHITE)

        for button in self.playingButtons:
            button.draw(self.window)

        self.shadeIncorrectCells(self.window, self.incorrectCells)

        if self.selected:
            self.drawSelection(self.window, self.selected, LIGHTBLUE)
        
        self.shadeLockedCells(self.window, self.lockedCells)
        
        self.drawNumbers(self.window)

        self.drawGrid(self.window)
        pygame.display.update()
        self.cellChanged = False

    def loadButtons(self):
        ### Check button
        self.playingButtons.append(Button(20, 40, WIDTH//7,40, text="Check", function=self.checkAllCells))

        ### Clear button
        self.playingButtons.append(Button(140, 40, WIDTH//7, 40, text="Clear", function=self.clearBoard))

        ### Note button add for future
        self.playingButtons.append(Button(260, 40, WIDTH//7, 40, text="Notes", function=self.noteMode))
        #self.playingButtons.append(Button(20,40,100,40))

### Board checking functions
    ##Add for future
    def noteMode(self):
        pass


    def clearBoard(self):
        self.grid = deepcopy(self.original)
        self.incorrectCells = []
        self.load()

    def checkAllCells(self):
        #print("checking incorrects")
        self.incorrectCells = []
        for yidx,row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != self.solution[yidx][xidx]:
                    pos = [(xidx*cellSize)+gridPos[0], (yidx*cellSize)+gridPos[1]]
                    self.incorrectCells.append([xidx, yidx])
                    self.shadeIncorrectCells(self.window, self.incorrectCells)
                    #print("adding color")
        if not self.incorrectCells:
            print("finished")
                
            


### helper functions

    def shadeLockedCells(self, window, locked):
        for cell in locked:
            pygame.draw.rect(window, LOCKEDCELLCOLOR, ((cell[0]*cellSize)+gridPos[0], (cell[1]*cellSize+gridPos[1]), cellSize, cellSize))

    def shadeIncorrectCells(self, window, incorrectCells):
        for cell in incorrectCells:
            pygame.draw.rect(window, RED, ((cell[0]*cellSize)+gridPos[0], (cell[1]*cellSize+gridPos[1]), cellSize, cellSize))

    def drawNumbers(self, window):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    pos = [(xidx*cellSize)+gridPos[0], (yidx*cellSize)+gridPos[1]]
                    self.textToScreen(window, str(num), pos)

    def drawSelection(self, window, pos, color):
        pygame.draw.rect(window, color, ((pos[0]*cellSize)+gridPos[0], (pos[1]*cellSize)+gridPos[1], cellSize, cellSize))

    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH-150, HEIGHT-150),2)
        for x in range(9):
            
            pygame.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1]+450),2 if x % 3 == 0 else 1)
            pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1]+(x*cellSize)), (gridPos[0]+450, gridPos[1]+(x*cellSize)),2 if x % 3 == 0 else 1)
    

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
            return False
        if self.mousePos[0] > gridPos[0]+gridSize or self.mousePos[1] > gridPos[1]+gridSize:
            return False
        return ((self.mousePos[0]-gridPos[0])//cellSize, (self.mousePos[1]-gridPos[1])//cellSize)

    def textToScreen(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize - fontWidth)//2
        pos[1] += (cellSize - fontHeight)//2
        window.blit(font, pos)

    def load(self):
        self.loadButtons()
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    self.lockedCells.append([xidx, yidx])

    def isInt(self, string):
        try:
            int(string)
            return True
        except:
            return False
        