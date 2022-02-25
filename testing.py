import itertools

game = [[1, 2, 2],
        [1, 2, 2],
        [2, 1, 1]]

# Horizontal
# for row in game:
#     print(row)
#     if row.count(row[0]) == len(row) and row[0] != 0:
#         print("Horizontal win")

# Vertical
# 00 10 20   01 11 21
#
# for row in game:
#     print(row)

# # makes a list of columns in the gameboard

# for i in range((len(game))):
#     # 0 1 2
#     for row in range(len(game)):
#         # 0 1 2
#         col = game[row][i]
#         columns.append(col)

# columns = [[game[row][i] for row in range(len(game))] for i in range(len(game))]
# for col in columns:
#     if col.count(col[0]) == len(col) and col[0] != 0:
#         print("Vertical win")


# Diags

# check = [game[row][col] for row, col in enumerate(range(len(game)))]
# if check.count(check[0]) == len(check) and check[0] != 0:
#     print("Diagonal win \\")
#
# check = [game[row][col] for row, col in enumerate(reversed(range(len(game))))]
# if check.count(check[0]) == len(check) and check[0] != 0:
#     print("Diagonal win /")

players = [1, 2]
current_player = itertools.cycle(players)
for i in range(3):
    print(next(current_player))