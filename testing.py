game = [[1, 2, 1],
        [1, 0, 2],
        [1, 1, 0]]

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


