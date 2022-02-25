# TODO#1: make a gameboard
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('   0  1  2')
for count, row in enumerate(game):
    print(count, row)

# TODO#2: move around the gameboard
for ix in range(len(game)):
    game[ix][ix] = 1

print('   0  1  2')
for count, row in enumerate(game):
    print(count, row)




# TODO#3: create logic for wins