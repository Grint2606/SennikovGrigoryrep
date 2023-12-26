def checkWinner(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return symbol
    for col in zip(*board):
        if all(cell == symbol for cell in col):
            return symbol
    if all(board[i][i] == symbol for i in range(len(board))) or all(board[i][len(board) - i - 1] == symbol for i in range(len(board))):
        return symbol
    return ""

def print_result(board):
    winner = checkWinner(board, "X")
    if winner:
        print(winner)
    else:
        winner = checkWinner(board, "O")
        if winner:
            print(winner)
        else:
            print("Ничья")
