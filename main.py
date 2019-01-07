from board import board
import util

def main():
    gameBoard = board(4)
    print(gameBoard.board)

    for _ in range(100):
        util.printArray(gameBoard.board)
        gameBoard.runLifeCycle()
        if gameBoard.flag == True:
            break




if __name__ == "__main__":
    main()
