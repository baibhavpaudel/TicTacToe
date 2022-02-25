import itertools


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
    # Displays gamemap/ moves
    try:
        if not just_display:
            gamemap[row][col] = player
        print('   0  1  2')
        for count, row in enumerate(gamemap):
            print(count, row)
        return gamemap, True
    except IndexError as e:
        print(f"That is not a valid position! Error: {e}.")
        return gamemap, False
    except Exception as e:
        print(f"Something went wrong! Error: {e}.")
        return gamemap, False


players = [1, 2]
player = itertools.cycle(players)
play = True

while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game, _ = gameboard(game, just_display=True)
    game_won = False
    player = itertools.cycle(players)

    while not game_won:
        current_player = next(player)
        played = False

        while not played:
            print(f"Current Player: {current_player}")
            row_choice = int(input("Which row position would you like to play? (0 1 2): "))
            col_choice = int(input("Which column position would you like to play? (0 1 2): "))

            game, played = gameboard(gamemap=game, player=current_player, row=row_choice, col=col_choice)

        if win(game, current_player):
            print("Game Over....")
            game_won = True

    again = input("Do you want to play another game? (y/n): ")
    if again.lower() == 'n':
        print("Got it! See you soon....")
        play = False
    elif again.lower() == 'y':
        print("Restarting.....")
        play = True
    else:
        print("Invalid option x.x! Exiting....")
        play = False

