# to get my solution to work, add an enter at the bottom of the board input file
# see line 10-15 for why that is needed
# could make stuff into functions but ehhh cba

# read in input
moves = []
with open("moves.txt", "r") as f:
    moves = [int(item) for item in f.readlines()[0].split(",")]

boards = []
with open("boards.txt", "r") as f:
    board = []
    for line in f.readlines():
        if line != "\n":
            board.append([int(item) for item in line.split(" ") if item not in ["", " ", "\n"]])
        else:
            boards.append(board)
            board = []


def calc_sum(board, move):
    sum = 0
    for line in board:
        for item in line:
            if item != -1:
                sum += item

    return sum * move


# define marked as -1
# beautiful O(n^4) solution!!
for move in moves:
    for i, board in enumerate(boards):
        for j, line in enumerate(board):
            for k, item in enumerate(line):
                if item == move:
                    boards[i][j][k] = -1

        # check if entire line is marked (i.e -1)
        for board in boards:
            for i in range(len(board)):
                if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == -1:
                    print(calc_sum(board, move))
                    exit()
                elif board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == -1:
                    print(calc_sum(board, move))
                    exit()
