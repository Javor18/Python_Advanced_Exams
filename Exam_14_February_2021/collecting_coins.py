# matrix_size = int(input())
# matrix = []
#
# player_positon = []
#
# for row in range(matrix_size):
#     matrix.append(input().split())
#     if "P" in matrix[row]:
#         player_positon.append([row, matrix[row].index("P")])
#
# coins = 0
#
# row = player_positon[0][0]
# col = player_positon[0][1]
#
# directions = {"up": [-1, 0],
#               "down": [1, 0],
#               "left": [0, -1],
#               "right": [0, 1]}
#
# hit_wall = False
#
# while coins < 100:
#
#     direction = input()
#
#     if direction == "up":
#
#         row += directions[direction][0]
#
#         if row < 0:
#
#             row = matrix_size - 1
#
#     elif direction == "down":
#
#         row += directions[direction][0]
#
#         if row >= matrix_size:
#             row = 0
#
#     elif direction == "left":
#
#         col += directions[direction][1]
#
#         if col < 0:
#
#             col = matrix_size - 1
#
#     elif direction == "right":
#
#         col += directions[direction][1]
#
#         if col >= matrix_size:
#
#             col = 0
#
#     position = matrix[row][col]
#
#     if position.isdigit():
#
#         coins += int(position)
#         matrix[row][col] = "-"
#
#     elif position == "X":
#
#         coins //= 2
#         hit_wall = True
#         player_positon.append([row, col])
#         break
#
#     player_positon.append([row, col])
#
# if hit_wall == False and coins > 0:
#
#     print(f"You won! You've collected {coins} coins.")
#
# else:
#     print(f"Game over! You've collected {coins} coins.")
#
# print('Your path:')
# for position in player_positon:
#
#     print(position)
#



matrix_size = int(input())

coins = 0
matrix = []

for x_row in range(matrix_size):

    matrix.append([int(x) if x.isdigit() else x for x in input().split()])

    if "P" in matrix[x_row]:

        row, col = x_row, matrix[x_row].index("P")

my_position = []

survive = True

my_position.append([row, col])

directions = {"up": [-1, 0],
              "down": [1, 0],
              "left": [0, -1],
              "right": [0, 1]}

while coins < 100:

    direction = input()

    row += directions[direction][0]
    col += directions[direction][1]

    if row >= matrix_size:

        row = 0

    elif row < 0:

        row = matrix_size - 1

    if col >= matrix_size:

        col = 0

    elif col < 0:

        col = matrix_size - 1

    if isinstance(matrix[row][col], int):

        coins += matrix[row][col]

        matrix[row][col] = "-"

    elif matrix[row][col] == "X":

        coins //= 2
        my_position.append([row, col])
        survive = False
        break

    my_position.append([row, col])

if survive == True:

    print(f"You won! You've collected {coins} coins.")

else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")

for position in my_position:

    print(position)