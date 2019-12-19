def new_board():
    board = []
    for i in range(0, 8):
        board.append([])
        for j in range(0, 8):
            board[i].append(0)
    board[3][4] = 1
    board[4][3] = 1
    board[3][3] = 2
    board[4][4] = 2

    return board


def score(board):
    player1 = 0
    player2 = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == 1:
                player1 += 1
            if board[i][j] == 2:
                player2 += 1
    return player1, player2


def enemy(player):
    if player == 1:
        return 2
    else:
        return 1


def enclosing(board, player, pos, direct):
    pos = pos[:]

    amount_of_enemys_found = 0
    while True:
        pos[0] += direct[0]
        pos[1] += direct[1]

        if board[pos[0]][pos[1]] == 0:
            return False

        if board[pos[0]][pos[1]] == player and amount_of_enemys_found > 0:
            return True

        if board[pos[0]][pos[1]] != player:
            amount_of_enemys_found += 1


def checkencloses(board, player, pos):
    if board[pos[0]][pos[1]] != 0:
        return False

    for xdirection, ydirection in [[0, 1], [0, -1], [1, -1], [1, 0], [1, 1], [-1, -1], [-1, 0], [-1, 1]]:
        if enclosing(board, player, pos, [xdirection, ydirection]):
            return True
        continue

    return False


def valid_moves(board, player):
    validspots = []
    for i in range(0, 7):
        for j in range(0, 7):
            pos = [i, j]
            if checkencloses(board, player, pos):
                validspots.append(pos)

    return validspots


def remove_spots(board):
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == -1:
                board[i][j] = 0

    return board


def print_board(board, currentplayer=0):
    if currentplayer != 0:
        validspots = valid_moves(board, currentplayer)

        for i in range(0, len(validspots)):
            board[validspots[i][0]][validspots[i][1]] = -1
    row = ""
    print(" --| A | B | C | D | E | F | G | H |")
    for i in range(0, 8):
        print("---+---+---+---+---+---+---+---+---|")
        for j in range(0, 8):
            if j == 0:
                row = " " + str(i + 1) + " |"
            if board[j][i] == 0:
                row += "   |"
            elif board[j][i] == 1:
                row += " B |"
            elif board[j][i] == 2:
                row += " W |"
            else:
                row += " o |"
        print(row)

    remove_spots(board)
    return


def next_state(dupeboard, player, pos):
    for xdirection, ydirection in [[0, 1], [0, -1], [1, -1], [1, 0], [1, 1], [-1, -1], [-1, 0], [-1, 1]]:
        if enclosing(dupeboard, player, pos, [xdirection, ydirection]):
            dupeboard[pos[0]][pos[1]] = player
            moving = [0, 0]
            moving[0] = pos[0]
            moving[1] = pos[1]
            while dupeboard[moving[0]+xdirection][moving[1]+ydirection] != player:
                dupeboard[moving[0]+xdirection][moving[1]+ydirection] = player
                moving[0] += xdirection
                moving[1] += ydirection
            dupeboard[moving[0] + xdirection][moving[1] + ydirection] = player
    return


def user_move():
    LETTERS = 'abcdefgh'
    NUMBERS = '12345678'

    pos = input("Enter move: ")
    pos.lower()
    if pos == 'q':
        quit()

    if len(pos) == 2:
        if pos[0] in LETTERS:
            if pos[1] in NUMBERS:
                return [LETTERS.index(pos[0]),NUMBERS.index(pos[1])]


def boardcopy(board):
    dupeboard = new_board()
    for x in range(8):
        for y in range(8):
            dupeboard[x][y] = board[x][y]
    return dupeboard


def bot_move(board, player):
    bestScore = 0
    for i in range(len(valid_moves(board, player))):
        dupeboard = boardcopy(board)
        next_state(dupeboard, player, valid_moves(dupeboard, player)[i])
        print_board(board, player)
        if score(dupeboard)[1] > bestScore:
            bestScore = score(dupeboard)[1]
            bestScoreIndex = i
    return valid_moves(board, player)[bestScoreIndex]


def multiplayer():
    board = new_board()
    player = 1
    while len(valid_moves(board, player)) != 0 and len(valid_moves(board,enemy(player))) != 0:
        if len(valid_moves(board, player)) != 0:
            print("player", player, "turn")
            print_board(board, player)
            print(score(board))
            pos = user_move()
            while pos not in valid_moves(board,player):
                print(player)
                print("move invalid!")
                pos = user_move()
            print(pos)
            print("move valid!")
            if checkencloses(board, player, pos):
                next_state(board, player, pos)

            player = enemy(player)
        else:
            player = enemy(player)

    if score(board)[0] > score(board)[1]:
        print("player 1 wins with", score(board)[0], "points!")
    elif score(board)[0] < score(board)[1]:
        print("player 2 wins with", score(board[1]), "points!")
    else:
        print("draw!")
    return


def singleplayer():
    board = new_board()
    player = 1
    while len(valid_moves(board, player)) != 0 and len(valid_moves(board,enemy(player))) != 0:
        if len(valid_moves(board, player)) != 0:
            print("player", player, "turn")
            print_board(board, player)
            print(score(board))
            if player == 1:
                pos = user_move()
                while pos not in valid_moves(board, player):
                    print(player)
                    print("move invalid!")
                    pos = user_move()
                print(pos)
                print("move valid!")
            if player == 2:
                pos = bot_move(board, player)

            if checkencloses(board, player, pos):
                next_state(board, player, pos)

            player = enemy(player)
        else:
            player = enemy(player)

    if score(board)[0] > score(board)[1]:
        print("player 1 wins with", score(board)[0], "points!")
    elif score(board)[0] < score(board)[1]:
        print("the cheeky bot wins with", score(board[1]), "points!")
    else:
        print("draw!")
    return


def login():
    print("---[REVERSI]---")
    mode = input("'s' for singleplayer or 'm' for multiplayer: ")
    if mode == 'm':
        multiplayer()
    if mode == 's':
        singleplayer()
    else:
        login()

login()