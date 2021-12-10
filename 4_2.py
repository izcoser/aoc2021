def get_board_score(board, n): # the score of the winning board
                                # is the (sum of all unmarked numbers) * last number called
    s = 0
    for line in board:
        for number, marked in line:
            if not marked:
                s += number

    return s * n
    

def mark_number(n, boards): # marks number n across all boards
    for board in boards:
        for line in board:
            for i, (number, marked) in enumerate(line):
                if number == n:
                    line[i] = (number, True)

def get_column(board, n): # returns nth column of a board
    return [line[n] for line in board]

def check_winning_line(line): # check whether a line or column won
    for _, marked in line:
        if not marked:
            return False
    return True

def check_win(board):
    for line in board:
        if check_winning_line(line):
            return True

    for i in range(5):
        if check_winning_line(get_column(board, i)):
            return True

    return False

def read_board(f):
    board = []
    s = f.readline() # eat one empty line
    if not s:
        return []

    for i in range(5):
        numbers = [(int(n), False) for n in f.readline().strip().split()]
        board.append(numbers)

    return board
    
with open('input4', 'r') as f:
    numbers = [int(n) for n in f.readline().strip().split(',')]
    boards = []
    board = read_board(f)
    while board != []:
        boards.append(board)
        board = read_board(f)


i = 0

last_number_for_last_board = -1
last_board_to_win = -1
already_won = []

while True:
    i += 1

    mark_number(numbers[i], boards)
    for idx, board in enumerate(boards):
        if idx in already_won:
            continue
        elif check_win(board):
            last_board_to_win = idx
            last_number_for_last_board = numbers[i]
            already_won.append(idx)

    if len(boards) == len(already_won):
        break



print(get_board_score(boards[last_board_to_win], last_number_for_last_board))
