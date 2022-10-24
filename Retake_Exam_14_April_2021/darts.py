# matrix_size = 7   # 7 rows, 7 cols
#
# first_player, second_player = input().split(", ")
#
# first_player_points, second_player_points = 501, 501
#
# matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range (matrix_size)]
#
# count_of_throws = 0
#
# first_player_throws = 0
#
# second_player_throws = 0
#
# while not (first_player_points <= 0 or second_player_points <= 0):
#
#     count_of_throws += 1
#
#     row, col = map(int, input()[1:-1].split(", "))
#
#     if count_of_throws % 2 != 0:
#
#         first_player_throws += 1
#
#     elif count_of_throws % 2 == 0:
#
#         second_player_throws += 1
#
#     if row > 7 or col > 7:
#
#         continue
#
#     symbol = matrix[row][col]
#
#     if isinstance(symbol, int):
#
#         if count_of_throws % 2 != 0:
#
#             first_player_points -= matrix[row][col]
#
#
#         else:
#
#             second_player_points -= matrix[row][col]
#
#     elif symbol == "D":
#
#         result = 0
#
#         for x in range(matrix_size):
#
#             if isinstance(matrix[x][col], int):
#
#                 result += matrix[x][col]
#
#             if isinstance(matrix[row][x], int):
#
#                 result += matrix[row][x]
#
#         if count_of_throws % 2 != 0:
#
#             first_player_points -= (result * 2)
#
#         elif count_of_throws % 2 == 0:
#
#             second_player_points -= (result * 2)
#
#     elif symbol == "T":
#
#         result = 0
#
#         for x in range(matrix_size):
#
#             num = matrix[x][col]
#
#             if isinstance(num, int):
#
#                 result += num
#
#         for y in range (matrix_size):
#
#             num = matrix[col][y]
#
#             if isinstance(num, int):
#                 result += num
#
#         if count_of_throws % 2 != 0:
#
#             first_player_points -= (result * 4)
#
#         elif count_of_throws % 2 == 0:
#
#             second_player_points -= (result * 4)
#
#     elif symbol == "B":
#
#         if count_of_throws % 2 != 0:
#             print(f"{first_player} won the game with {first_player_throws} throws!")
#
#         elif count_of_throws % 2 == 0:
#
#             print(f"{second_player} won the game with {second_player_throws} throws!")
#
#         break
#
# if first_player_points <= 0:
#
#     print(f"{first_player} won the game with {first_player_throws} throws!")
#
# elif second_player_points <= 0:
#
#     print(f"{second_player} won the game with {second_player_throws} throws!")


matrix_size = 7

first_player, second_player = input().split(", ")

first_player_points, second_player_points = 501, 501

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(matrix_size)]

i = 0

first_player_throws, second_player_throws = 0, 0


while first_player_points > 0 or second_player_points > 0:

    if first_player_points <= 0 or second_player_points <= 0:

        break

    row, col = [int(x) for x in input()[1:-1].split(", ")]

    i += 1

    if i % 2 != 0:
        first_player_throws += 1
    else:
        second_player_throws += 1

    if row >= matrix_size or col >= matrix_size:
        continue

    position = matrix[row][col]

    if isinstance(position, int):

        if i % 2 != 0:

            first_player_points -= position

        else:

            second_player_points -= position

    elif position == "D":

        for x in range(matrix_size):

            if isinstance(matrix[x][col], int):

                if i % 2 != 0:

                    first_player_points -= matrix[x][col] * 2

                else:
                    second_player_points -= matrix[x][col] * 2

            if isinstance(matrix[row][x], int):

                if i % 2 != 0:

                    first_player_points -= matrix[row][x] * 2

                else:
                    second_player_points -= matrix[row][x] * 2

    elif position == "T":

        for x in range(matrix_size):

            if isinstance(matrix[x][col], int):

                if i % 2 != 0:

                    first_player_points -= matrix[x][col] * 3

                else:
                    second_player_points -= matrix[x][col] * 3

            if isinstance(matrix[row][x], int):

                if i % 2 != 0:

                    first_player_points -= matrix[row][x] * 3

                else:
                    second_player_points -= matrix[row][x] * 3

    elif position == "B":

        if i % 2 != 0:

            print(f"{first_player} won the game with {first_player_throws} throws!")

        else:

            print(f"{second_player} won the game with {second_player_throws} throws!")

        break

if first_player_points <= 0:
    print(f"{first_player} won the game with {first_player_throws} throws!")

elif second_player_points <= 0:
    print(f"{second_player} won the game with {second_player_throws} throws!")