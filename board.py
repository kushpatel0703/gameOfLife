from random import getrandbits

class board:
    def __init__(self, size):
        self.board = []

        for i in range(size):
            self.board.append([])
            for j in range(size):
                self.board[i].append(getrandbits(1))
