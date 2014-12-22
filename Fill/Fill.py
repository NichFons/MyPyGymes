#########################################
############### Fill Game ###############
##  A game that fills in values until  ##
##     all the values are the same.    ##
##  Scores are kept by the number of   ##
##             turns used.             ##
#########################################
#########################################


from random import randint # Only needs randint


# Create the board and fill it with A's, B's, C's, or D's
def make_board():
    board = ['X']
    for i in range(1,101):
        chooser = randint(1,4)
        if chooser == 1:
            a = 'A'
        elif chooser == 2:
            a = 'B'
        elif chooser == 3:
            a = 'C'
        if chooser == 4:
            a = 'D'
        board.append(a)
    return board


# Prints out the boards row by row
def print_board(board):
    for i in range(0,10):
        row = [ ]
        for c in range(1,11):
            row.append(board[i * 10 + c])
        print("".join(row))
    print()
    print()


# User chooses the input of A, B, C, or D, or redo
def choose_to_change():
    letter = input("INSERT LETTER: A, B, C, or D: ").upper()
    if letter != 'A' and letter != 'B' and letter != 'C' and letter != 'D':
        return choose_to_change()
    return letter


#Recursive definition of letter change
def change_letters(letter,board,pos, current):
    # Changing Letter Algorithm:
    # FLOOD FILL ALGORITHM
    # Use recursive definition
    # Check left, right, down, up
    # Not certain direction on edges
    if board[pos] != current:
        return board
    board[pos] = letter
    if pos % 10 != 1:
        board = change_letters(letter, board, pos - 1, current)
    if pos % 10 != 0:
        board = change_letters(letter, board, pos + 1, current)
    if pos > 10:
        board = change_letters(letter, board, pos - 10, current)
    if pos < 90:
        board = change_letters(letter, board, pos + 10, current)
    return board


# Checks if the game has been won
def check(board):
    current_letter = board[1]
    for i in range(1, 101):
        if board[i] != current_letter:
            loss = True
            break
        loss = False
    return loss


# Main Game Loop
def main():
    play = True
    while play:
        board = make_board()
        print_board(board)
        not_won = True
        count = 1
        while not_won:
            count += 1
            letter = choose_to_change()
            board = change_letters(letter, board, 1, board[1])
            print_board(board)
            not_won = check(board)
            
        print("Congrats! You won in {0} turns!".format(count))
        play_choice = input("Input 0 to play again, else to quit \n")
        print()
        if play_choice != '0':
            play = False



main()
