import itertools

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def win(gamemap, player):
    # Horizontal win
    for row in gamemap:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {player} wins horizontally!")
            return True

    # Vertical win
    # makes a list of columns in the gameboard
    columns = [[gamemap[row][i] for row in range(len(gamemap))] for i in range(len(gamemap))]
    for col in columns:
        if col.count(col[0]) == len(col) and col[0] != 0:
            print(f"Player {player} wins vertically!")
            return True

    # Diagonal win
    check = [game[row][col] for row, col in enumerate(range(len(game)))]
    if check.count(check[0]) == len(check) and check[0] != 0:
        print(f"Player {player} wins diagonally! (\\)")
        return True

    check = [game[row][col] for row, col in enumerate(reversed(range(len(game))))]
    if check.count(check[0]) == len(check) and check[0] != 0:
        print(f"Player {player} wins diagonally! (/)")
        return True


def gameboard(gamemap, player=0, row=0, col=0, just_display=False):
    def show_gamemap(gamemap):
        print('   0  1  2')
        for count, row in enumerate(gamemap):
            print(count, row)

    # Displays gamemap/ moves
    try:
        if not just_display:
            gamemap[row][col] = player
            show_gamemap(gamemap)
            return gamemap
        else:
            show_gamemap(gamemap)
    except IndexError as e:
        print(f"That is not a valid position! Error: {e}.")
    except Exception as e:
        print(f"Something went wrong! Error: {e}.")


gameboard(game, just_display=True)

# TODO: Change between two players and play one by one
players = [1, 2]
player = itertools.cycle(players)
play = True

while play:
    current_player = next(player)
    print(f"Current Player : {current_player}")
    row_choice = int(input("Which row position would you like to play? (0 1 2): "))
    col_choice = int(input("Which column position would you like to play? (0 1 2): "))

    game = gameboard(gamemap=game, player=current_player, row=row_choice, col=col_choice)

    if win(game, current_player):
        play = False

