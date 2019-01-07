from board import board
import util

def main():
    inputVal = input("What size board would you like? ")

    try:
         size = int(inputVal)
    except ValueError:
        print("Thats not an Int!")
    else:
        gameBoard = board(int(size))
        print(gameBoard.board)

        while(1):
            util.printArray(gameBoard.board)
            gameBoard.runLifeCycle()
            if gameBoard.flag == True:
                break




if __name__ == "__main__":
    main()
