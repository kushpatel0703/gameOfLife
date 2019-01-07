from random import getrandbits

class board:
    def __init__(self, size):
        self.board = []
        self.size = size

        for i in range(self.size):
            self.board.append([])
            for j in range(self.size):
                self.board[i].append(getrandbits(1))

    def runLifeCycle(self):
        newBoard = []

        for i in range(self.size):
            newBoard.append([])
            for j in range(self.size):
                newBoard[i].append(self.checkNeighbors(i, j))

        if newBoard != self.board:
            self.board = newBoard

    def checkNeighbors(self, i, j):
        liveNeighbors = self.checkNeighborsHelper(i,j)

        if self.board[i][j] == 1:
            if liveNeighbors == 2 or liveNeighbors == 3:
                return 1
            else:
                return 0
        else:
            if liveNeighbors == 3:
                return 1
            else:
                return 0

    def checkNeighborsHelper(self, i, j):
        liveNeighbors = 0

        if (i-1) > 0 and (i-1) < (self.size - 1):
            if self.board[i-1][j] == 1:
                liveNeighbors += 1

        if (i+1) > 0 and (i+1) < (self.size - 1):
            if self.board[i+1][j] == 1:
                liveNeighbors += 1

        if (j-1) > 0 and (j-1) < (self.size - 1):
            if self.board[i][j-1] == 1:
                liveNeighbors += 1

        if (j+1) > 0 and (j+1) < (self.size - 1):
            if self.board[i][j+1] == 1:
                liveNeighbors += 1

        return liveNeighbors
