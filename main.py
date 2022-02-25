# TODO#1: make a gameboard
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def gameboard(gamemap, player=0, row=0, col=0, just_display=False):
    def show_gamemap(gamemap):
        print('   0  1  2')
        for count, row in enumerate(gamemap):
            print(count, row)

    if not just_display:
        gamemap[row][col] = player
        show_gamemap(gamemap)
    else:
        show_gamemap(gamemap)


gameboard(game, just_display=True)

# TODO#2: move around the gameboard
gameboard(game, player=1, row=1, col=1)


# TODO#3: create logic for wins

