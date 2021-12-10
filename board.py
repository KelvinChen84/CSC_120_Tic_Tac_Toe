row1 = ['-', '-', '-']
row2 = ['-', '-', '-']
row3 = ['-', '-', '-']
board = [row3, row2, row1]


def printboard(board):
    for i in board:
        print(i)

printboard(board)

def main():
    printboard(board)
    player = 'X'
    running = True
    while(running):
        printboard(board)
        gettinginput = True
        while(gettinginput):
            column = input("Player list a column of where you want to place your mark: ")
            row = input("Player list a row of where you want to place your mark:  ")
            if column <= 3 and column >= 1:
                if row <=3 and row >= 1:
                    if board[row - 1][column - 1] == '-':
                        gettinginput = False
    board[row - 1][column - 1] = player
    printboard(board)
    print("Please switch players")
    if player == 'X':
        player = 'O'
    else:
        player = 'X'


