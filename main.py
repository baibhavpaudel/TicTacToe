# TODO#1: make a gameboard
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def gameboard(gamemap, player=0, row=0, col=0, just_display=False):
    def show_gamemap(gamemap):
        print('   0  1  2')
        for count, row in enumerate(gamemap):
            print(count, row)

    try:
        if not just_display:
            gamemap[row][col] = player
            show_gamemap(gamemap)
        else:
            show_gamemap(gamemap)
    except IndexError as e:
        print(f"That is not a valid position! Error: {e}.")
    except Exception as e:
        print(f"Something went wrong! Error: {e}.")


gameboard(game, just_display=True)

# TODO#2: move around the gameboard
# gameboard(game, player=1, row=1, col=1)

row_choice = int(input("Which row position would you like to play? (0 1 2):  "))
col_choice = int(input("Which column position would you like to play? (0 1 2):  "))

gameboard(gamemap=game, player=1, row=row_choice, col=col_choice)


# TODO#3: create logic for wins
