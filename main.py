from board import board

def main():
    gameBoard = board(4)
    print(gameBoard.board)

    for _ in range(100):
        gameBoard.runLifeCycle()
        print(gameBoard.board)



if __name__ == "__main__":
    main()
