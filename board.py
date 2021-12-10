
def printboard(board):
    for i in reversed(board):  # Without the reversed function the Y axis is flipped
        print(i)


win = 0
player = 'X'
running = True
row1 = ['-', '-', '-']
row2 = ['-', '-', '-']
row3 = ['-', '-', '-']
board = [row1, row2, row3]
printboard(board)
while running:  # Starts game
    gettinginput = True
    while gettinginput:  # This loop ensures that cell input is not out of bounds or on a filled location
        column = int(input("Player list a column of where you want to place your mark: "))
        row = int(input("Player list a row of where you want to place your mark:  "))
        if 3 >= column >= 1:
            if 3 >= row >= 1:
                if board[row - 1][column - 1] == '-':
                    gettinginput = False
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    board[row - 1][column - 1] = player  # This is where the indicated cell is filled
    printboard(board)
    if board[0][0] == board[0][1] == board[0][2] != '-':  # This checks the 8 possible win conditions
        win = 1
    if board[1][0] == board[1][1] == board[1][2] != '-':
        win = 1
    if board[2][0] == board[2][1] == board[2][2] != '-':
        win = 1
    if board[0][0] == board[1][0] == board[2][0] != '-':
        win = 1
    if board[0][1] == board[1][1] == board[2][1] != '-':
        win = 1
    if board[0][2] == board[1][2] == board[2][2] != '-':
        win = 1
    if board[0][0] == board[1][1] == board[2][2] != '-':
        win = 1
    if board[2][0] == board[1][1] == board[0][2] != '-':
        win = 1
    if win == 1:
        print(player + " has won")
        running = False  # Break condition for a win
    else:
        if any('-' in sublist for sublist in board):  # Checks if board is full
            print("Please switch players")
            if player == 'X':  # Switches variable that fills cell if board is not full and restarts loop
                player = 'O'
            else:
                player = 'X'
        else:
            print("The game is a draw")
            running = False  # Break condition for a full board










