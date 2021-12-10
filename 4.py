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

while True:
    last_number = numbers[i]
    i += 1

    mark_number(last_number, boards)
    for board in boards:
        if check_win(board):
            print(get_board_score(board, last_number))
            exit(0)

