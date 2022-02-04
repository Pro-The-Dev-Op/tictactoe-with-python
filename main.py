'build a tic tac toe game'
def tictactoe():
    'build a tic tac toe game'
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    def printboard(board):
        'print the board'
        print('\n')
        for row in board:
            print(row)
    def checkwin(board):
        'check if someone won'
        for row in board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != ' ':
                return True
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return True
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return True
        return False
    def checktie(board):
        'check if the game is a tie'
        for row in board:
            if ' ' in row:
                return False
        return True
    def checkmove(board, move):
        'check if the move is valid'
        if move in range(1,10):
            if board[0][move-1] == ' ':
                return True
        return False
    def makemove(board, move, player):
        'make a move'
        if player == 'X':
            board[0][move-1] = 'X'
        else:
            board[0][move-1] = 'O'
    def getmove(board):
        'get a move'
        move = input('Enter your move: ')
        while not checkmove(board, move):
            move = input('Enter your move: ')
        return move
    def playgame(board):
        'play the game'
        player = 'X'
        while not checkwin(board) and not checktie(board):
            printboard(board)
            move = getmove(board)
            makemove(board, move, player)
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        printboard(board)
        if checkwin(board):
            print('Congratulations! You won!')
        else:
            print('The game is a tie!')
    playgame(board)
tictactoe()
if __name__ == '__main__':
    tictactoe()