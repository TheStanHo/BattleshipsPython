from random import randint
"""
Simple Battleship game created in Python created while doing the Python Codecademy Python 2 course(Code edited to 
 fit Python 3) but is edited and tided a bit to make it smoother and look better.
Author : Stanley Ho  
"""
# This creates a 5 x 5 board and no need for one off error e.g. input 0 x 0 as numbers take index 0
board = [["     1 ", " 2 ", " 3 ", " 4 ", " 5 "],
         [" 1 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
         [" 2 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
         [" 3 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
         [" 4 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
         [" 5 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]]


# Function to print the board  in the format that we want.
def print_board(board):
    for row in board:
        print(" ".join(row))


# Returns a random row for the ship
def random_row(board):
    return randint(1, len(board[1]) - 1)

# Returns a random column for the ship


def random_col(board):
    return randint(1, len(board[1]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

print("Welcome to The Battleships Game you have 5 turns to guess my position. Good luck.")

# Play the game with the player only having a maximum of 5 guesses.
for turn in range(6):
    if turn == 5:
        print("Game Over the ship was at: ("+str(ship_row)+", "+str(ship_col)+")")
    else:
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
                print("Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "[X]":
                print("You guessed that one already.")
            else:

                print("You missed my battleship!")
                board[guess_row][guess_col] = "[X]"
            print("Number of turns left: " + str(5-(turn + 1)))
            print_board(board)
