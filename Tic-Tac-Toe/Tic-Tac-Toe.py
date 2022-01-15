# Author: Bryce Francom
# date: 1/15/2022
def printBoard(playArray):
    print(f"{playArray[0]} | {playArray[1]} | {playArray[2]}")
    print("- + - + -")
    print(f"{playArray[3]} | {playArray[4]} | {playArray[5]}")
    print("- + - + -")
    print(f"{playArray[6]} | {playArray[7]} | {playArray[8]}")

def changeGameOver(GAMEOVER):
    GAMEOVER = True
    return GAMEOVER

# check function for end game
def checkGameStatus(test, GAMEOVER):
    
    testArray = ["1","2","3","4","5","6","7","8","9"]
    if ("1" not in test and "2" not in test and "3" not in test and "4" not in test and "5" not in test
    and "6" not in test and "7" not in test and "8" not in test and "9" not in test):
        return changeGameOver(GAMEOVER)
    # Is top row complete?
    elif (test[0] == "x" and test[1] == "x" and test[2] == "x" ):
        return changeGameOver(GAMEOVER)
    elif (test[0] == "o" and test[1] == "o" and test[2] == "o"):
        return changeGameOver(GAMEOVER)
    # Second row complete?
    elif (test[3] == "x" and test[4] == "x" and test[5] == "x"):
        return changeGameOver(GAMEOVER)
    elif (test[3] == "o" and test[4] == "o" and test[5] == "o"):
        return changeGameOver(GAMEOVER)
    # Third Row?
    elif (test[6] == "x" and test[7] == "x" and test[8] == "x"):
        return changeGameOver(GAMEOVER)
    elif (test[6] == "o" and test[7] == "o" and test[8] == "o"):
        return changeGameOver(GAMEOVER)
    # First Column?
    elif (test[0] == "x" and test[3] == "x" and test[6] == "x"):
        return changeGameOver(GAMEOVER)
    elif (test[0] == "o" and test[3] == "o" and test[6] == "o"):
        return changeGameOver(GAMEOVER)
    # Second Column?
    elif (test[1] == "x" and test[4] == "x" and test[7] == "x"):
        return changeGameOver(GAMEOVER)
    elif (test[1] == "o" and test[4] == "o" and test[7] == "o"):
        return changeGameOver(GAMEOVER)
    # Third Column?
    elif (test[2] == "x" and test[5] == "x" and test[8] == "x"):
        return changeGameOver(GAMEOVER)
    elif (test[2] == "o" and test[5] == "o" and test[8] == "o"):
        return changeGameOver(GAMEOVER)
    # Top Left Diagnal?
    elif (test[0] == "x" and test[4] == "x" and test[8] == "x"):
        return changeGameOver(GAMEOVER)
    elif (test[0] == "o" and test[4] == "o" and test[8] == "o"):
        return changeGameOver(GAMEOVER)
    # Top Right Diagnal?
    elif (test[2] == "x" and test[4] == "x" and test[6] == "x"):
        return changeGameOver(GAMEOVER)
    elif (test[2] == "o" and test[4] == "o" and test[6] == "o"):
        return changeGameOver(GAMEOVER)
    else:
        pass



def main():
    
    PLAYAGAIN = True

    # greeting
    print("Welcome to a friendly game of Tic-Tac-Toe!")
    print()
    
    # Play again loop
    while PLAYAGAIN:
        GAMEOVER = False
    # create an array to be used in the the grid
        playArray = ["1","2","3","4","5","6","7","8","9"]
        playerOne = True
    # while loop for the game
        while not GAMEOVER:
            # place holder variables
            choice = None
            # determine the layer turn
            

            printBoard(playArray)

            # take a turn
            print()
            if playerOne:
                try:
                    choice = int(input("x's turn to choose a square (1-9):")) - 1
                    playArray[choice] = "x"
                    GAMEOVER = checkGameStatus(playArray, GAMEOVER)
                    playerOne = False
                
                except ValueError() or IndexError():
                    print("Not a valid input!")
                    print("Try again.")
            else:
                try:
                    choice = int(input("o's turn to choose a square (1-9):")) - 1
                    playArray[choice] = "o"
                    GAMEOVER = checkGameStatus(playArray, GAMEOVER)
                    playerOne = True
                
                except ValueError() or IndexError():
                    print("Not a valid input!")
                    print("Try again.")
        printBoard(playArray)
        print()
        print("Good game, thanks for playing")
        anotherRound = None
        while anotherRound != "y" or anotherRound != "n":
            anotherRound = input("play again (y/n)? ")
            if anotherRound == "y":
                PLAYAGAIN = True
                break
            elif anotherRound == "n":
                PLAYAGAIN = False
                break
            else:
                print("Invalid response, try again.")


if __name__ == "__main__":
    main()