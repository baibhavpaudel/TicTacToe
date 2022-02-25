# TODO#1: make a gameboard
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


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

for i in range(3):
    row_choice = int(input("Which row position would you like to play? (0 1 2):  "))
    col_choice = int(input("Which column position would you like to play? (0 1 2):  "))

    gameboard(gamemap=game, player=1, row=row_choice, col=col_choice)


# TODO#3: create logic for wins
def win(gamemap):
    # Horizontal win
    for row in gamemap:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"The player wins horizontally!")
        print(row)

    # Vertical win
    # makes a list of columns in the gameboard
    columns = [[gamemap[row][i] for row in range(len(gamemap))] for i in range(len(gamemap))]
    for col in columns:
        if col.count(col[0]) == len(col) and col[0] != 0:
            print("Vertical win")