# “To be happy is to be able to become aware of oneself without fright.”
# ― Walter Benjamin

import random

square_dict = {"1a": (0, 0), "1b": (0, 1), "1c": (0, 2), "2a": (1, 0), "2b": (1, 1),
               "2c": (1, 2), "3a": (2, 0), "3b": (2, 1), "3c": (2, 2)}
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def board_game(board):
    columne = 1
    print("   a", " b", " c")
    for row in board:
        print(columne, row)
        columne += 1
    return board


def player_square():
    play = True
    while play == True:
        player_choose = input("Please, choose a square:\n")
        if player_choose.lower() in square_dict.keys():
            play == False
            player_square_choose = square_dict[player_choose]
            print("you choose the square " + player_choose)
            print("the coordenates of this square are: \n" + str(player_square_choose))
            return player_square_choose


def cpu_square():
    cpu_choose = random.choice(list(square_dict.keys()))
    cpu_square_choose = square_dict[cpu_choose]
    print("the CPU choose the square: " + cpu_choose)
    print("the coordenates of this square are: \n" + str(cpu_square_choose))
    return cpu_square_choose


def round_ver(player, cpu):
    verif = True
    while verif == True:
        if player == cpu:
            verif == True
            player_square()
            cpu_square()
        else:
            verif == False
    return player_square(), cpu_square()


def update():
    board_status = board_game(board)
    a, b = player_square()
    x, y = cpu_square()
    board_status[a][b] = 1
    board_status[x][y] = 2
    #board_game(board_status)
    return board_status


def execution():

    while True:
        board_actual = update()
        h1 = sum(board_actual[0])
        h2 = sum(board_actual[1])
        h3 = sum(board_actual[2])
        v1 = sum([item[0] for item in board_actual])
        v2 = sum([item[1] for item in board_actual])
        v3 = sum([item[2] for item in board_actual])
        d1 = board_actual[0][0] + board_actual[1][1] + board_actual[2][2]
        d2 = board_actual[2][0] + board_actual[1][1] + board_actual[0][2]
        if h1 == 3 and 0 not in board_actual[0]:
            print(board_game(board_actual))
            print("TIC TAC TOE on row 1\nYou won the game!!")
            break
        if h1 == 6 and 0 not in board_actual[0]:
            print(board_game(board_actual))
            print("TIC TAC TOE on row 1\nYou lost the game!!")
            break
        if h2 == 3 and 0 not in board_actual[1]:
            print(board_game(board_actual))
            print("TIC TAC TOE on row 2\nYou won the game!!")
            break
        if h2 == 6 and 0 not in board_actual[1]:
            print(board_game(board_actual))
            print("TIC TAC TOE on row 2\nYou lost the game!!")
            break
        if h3 == 3 and 0 not in board_actual[2]:
            print(board_game(board_actual))
            print("TIC TAC TOE on row 3\nYou won the game!!")
            break
        if h3 == 6 and 0 not in board_actual[2]:
            print(board_game(board_actual))
            print("TIC TAC TOE on row 3\nYou lost the game!!")
            break
        if v1 == 3 and 0 not in [item[0] for item in board_actual]:
            print(board_game(board_actual))
            print("TIC TAC TOE on colomn A\nYou won the game!!")
            break
        if v1 == 6 and 0 not in [item[0] for item in board_actual]:
            print(board_game(board_actual))
            print("TIC TAC TOE on colomn A\nYou lost the game!!")
            break
        if v2 == 3 and 0 not in [item[1] for item in board_actual]:
            print(board_game(board_actual))
            print("TIC TAC TOE on colomn B\nYou won the game!!")
            break
        if v2 == 6 and 0 not in [item[1] for item in board_actual]:
            print(board_game(board_actual))
            print("TIC TAC TOE on colomn B\nYou lost the game!!")
            break
        if v3 == 3 and 0 not in [item[2] for item in board_actual]:
            print(board_game(board_actual))
            print("TIC TAC TOE on colomn C\nYou won the game!!")
            break
        if v3 == 6 and 0 not in [item[2] for item in board_actual]:
            print(board_game(board_actual))
            print("TIC TAC TOE on colomn C\nYou lost the game!!")
            break
        if d1 == 3 and board_actual[0][0] != 0 and board_actual[1][1] != 0 and board_actual[2][2] != 0:
            print(board_game(board_actual))
            print("TIC TAC TOE on the left diagonal\nYou won the game!!")
            break
        if d1 == 6 and board_actual[0][0] != 0 and board_actual[1][1] != 0 and board_actual[2][2] != 0:
            print(board_game(board_actual))
            print("TIC TAC TOE on the left diagonal\nYou lost the game!!")
            break
        if d2 == 3 and board_actual[0][2] != 0 and board_actual[1][1] != 0 and board_actual[2][0] != 0:
            print(board_game(board_actual))
            print("TIC TAC TOE on the left diagonal\nYou won the game!!")
            break
        if d2 == 6 and board_actual[0][2] != 0 and board_actual[1][1] != 0 and board_actual[2][0] != 0:
            print(board_game(board_actual))
            print("TIC TAC TOE on the left diagonal\nYou lost the game!!")
            break


execution()

"""board2 = [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
board3 = []
# board3 = board2.reverse()
print(board3)
winning_combinations = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 1), (2, 2), (2, 3)],
                        [(0, 0), (1, 0), (2, 0)],
                        [(0, 1), (0, 2), (0, 3)], [(1, 0), (1, 1), (1, 2)], [(0, 0), (1, 1), (2, 2)],
                        [(0, 2), (1, 1), (2, 0)]]

h1 = sum(board2[0])
if h1 == 3 or h1 == 6 and 0 not in board2[0]:
    print("esta pasando")
h2 = sum(board2[1])
if h2 == 3 or h2 == 6 and 0 not in board2[0]:
    print("esta pasando")
h3 = sum(board2[2])
if h3 == 3 or h3 == 6 and 0 not in board2[0]:
    print("esta pasando")

print(h1, h2, h3)

v1 = sum([item[0] for item in board2])
if v1 == 3 or v1 == 6 and 0 not in [item[0] for item in board2]:
    print("daleboca")
v2 = sum([item[1] for item in board2])
if v2 == 3 or v2 == 6 and 0 not in [item[0] for item in board2]:
    print("daleboca")
v3 = sum([item[2] for item in board2])
if v3 == 3 or v3 == 6 and 0 not in [item[0] for item in board2]:
    print("daleboca")

print(v1, v2, v3)

d1 = board_actual[0][0] + board_actual[1][1] + board_actual[2][2]
d2 = board_actual[2][0] + board_actual[1][1] + board_actual[0][2]
print(d1, d2)"""

"""choose_player = player_square()
def cpu_square(choose_player):
    cpu = True
    while cpu == True:
        cpu_choose = random.choice(list(square_dict.keys()))
        cpu_square_choose = square_dict[cpu_choose]
        if cpu_square_choose != choose_player:
            cpu == False
            print("the CPU choose the square: " + cpu_choose)
            print("the coordenates of this square are: \n" + str(cpu_square_choose))
            return cpu_square_choose"""

"""def cpu_square():
    c = player_square()
    cpu = True
    while cpu == True:
        cpu_choose = random.choice(list(square_dict.keys()))
        cpu_square_choose = square_dict[cpu_choose]
        if cpu_square_choose != c:
            cpu == False
            print("the CPU choose the square: " + cpu_choose)
            print("the coordenates of this square are: \n" + str(cpu_square_choose))
            return cpu_square_choose"""

"""def update_board():
    board = update_list()
    for cel in range(len(board)):
        for rows in range(len(board[cel])):
            columne = 0
            print("   a", " b", " c")
            for row in board:
                print(columne, row)
                columne += 1
            return board"""

"""def execution():
    i = 0
    update_board()
    for row in range(len(update_board())):
        for cel in range(len(update_board(row))):
            if cel == 0:
                update_board()"""

# update_board()
"""while boarding == True:
        #[row for col in range(len(board)) for row in col if board[col][row] != 0]
        for wor in range(len(board)):
            for num in wor:
                if board[wor][num] != 0:
                    boarding == False"""

"""if square_dict.keys("0a","0b","0c") ==0:
    print("vamos boca")"""

"""a, b = player_square()
board_status[a][b] = 1

board_game()"""
"""board[player_square_choose[0]][player_square_choose[1]]=1
print(board)"""

"""import random

toss = random.randint(0,1)
if toss == 1:
    coin = "heads"
if toss == 0:
    coin = "tails"

choice_toss = input("Hello! lets see who starts the game.\nPick heads or tails:\n")
if choice_toss.lower() == coin:
    print("Well done,", choice_toss.lower(), "wons the flip.\nYou start the match")
if choice_toss.lower() != coin:
    print("The CPU will starts this game ")"""

"""def update_list():
    board_status = board_game(board)
    a, b = player_square()
    x, y = cpu_square()
    board_status[a][b] = 1
    board_status[x][y] = 2
    return board_status"""
