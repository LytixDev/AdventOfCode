# to get my solution to work, add an enter at the bottom of the board input file


def calc_sum(board, move):
    sum = 0
    for line in board:
        for item in line:
            if item != -1:
                sum += item
    return sum * move


def permutate_boards(boards, move):
    for i, board in enumerate(boards):
        for j, line in enumerate(board):
            for k, item in enumerate(line):
                if item == move:
                    boards[i][j][k] = -1

    return boards

def remove_marked(boards):
    # check if entire line is marked (i.e -1)
    to_ret = boards
    for ind, board in enumerate(boards):
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == -1:
                try:
                    to_ret.pop(ind)
                except IndexError as e:
                    pass
            elif board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == -1:
                try:
                    to_ret.pop(ind)
                except IndexError as e:
                    pass
    
    return to_ret


def is_final_state(boards):
    for ind, board in enumerate(boards):
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == -1:
                return True
            elif board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == -1:
                return True

    return False


def main():
    moves = []
    with open("moves1.txt", "r") as f:
        moves = [int(item) for item in f.readlines()[0].split(",")]

    boards = []
    with open("boards1.txt", "r") as f:
        board = []
        for line in f.readlines():
            if line != "\n":
                board.append([int(item) for item in line.split(" ") if item not in ["", " ", "\n"]])
            else:
                boards.append(board)
                board = []

    # define marked as -1
    on_last = False
    prev_board = None
    for i, move in enumerate(moves):
        if not on_last:
            boards = permutate_boards(boards, move)
            boards = remove_marked(boards)
            if len(boards) == 1:
                on_last = True

        else:
            if is_final_state(boards):
                print(calc_sum(boards[0], moves[i-1]))
                exit(0)
            else:
                boards = permutate_boards(boards, move)

if __name__ == "__main__":
    main()
