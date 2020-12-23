BOARD = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],]


def check_win(token_list, token):
    count = 0
    for tok in token_list:
        if tok == token:
            count = count + 1

    if count == 3:
        print(f"{token} won the game!!!!")
        exit()


def draw_board(board):
    print('    0   1   2')
    for idx, rows in enumerate(board):
        print(f'{idx}   {rows[0]} | {rows[1]} | {rows[2]}')
        print('  ------------')


def check_board(board, token):
    token_list = []
    #horizontal win

    for i in range(3):
        token_list = []
        for j in range(3):
            if board[i][j] == token:
                token_list.append(board[i][j])
        check_win(token_list, token)

    token_list = []
    #vertical check
    for i in range(3):
        token_list = []
        for j in range(3):
            if board[j][i] == token:
                token_list.append(board[j][i])
        check_win(token_list, token)


    token_list = []
    #primary diagonal check
    for i in range(3):
        if board[i][i] == token:
            token_list.append(board[i][i])
    check_win(token_list, token)

    token_list = []
    #secondary diagonal check
    for i in range(3):
        if board[i][2-i] == token:
            token_list.append(board[i][2-i])
    check_win(token_list, token)


def update_board(board, token):
    while True:
        print(f'{token} enter the co-ordinates:')
        i = int(input('Enter row number:'))
        j = int(input('Enter column number:'))

        try:
            # check if the position is occupied
            if board[i][j] != ' ':
                print('Position already occupied, try again')

            else:
                board[i][j] = token
                return board

        except IndexError:
            print('Invalid Poisition')

def play(board):
    player1 = input('Player1 enter your token: ')
    player2 = input('Player2 enter your token: ')

    turn = 0
    empty = 0

    while True:
        draw_board(BOARD)
        # check empty spaces in the board
        for row in board:
            for item in row:
                if item == ' ':
                    empty = empty + 1

        if empty:
            if turn % 2 == 0:
                player_token = player1
            else:
                player_token = player2

            board = update_board(board, player_token)
            check_board(board, player_token)
            turn = turn + 1
        else:
            print("tie!!!!")
            exit()


play(BOARD)