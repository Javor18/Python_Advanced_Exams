# matrix_size = 6
#
# matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(matrix_size)]
#
# prize, total_score = "", [0]
#
# def check_valid_index(row, col):
#     return 0 <= row < matrix_size and 0 <= col < matrix_size
#
#
# def get_score(col):
#     for row in range(matrix_size):
#         symbol = matrix[row][col]
#         total_score[0] += symbol
#
#
# for throw in range(3):
#     row, col = [int(x) for x in input()[1:-1].split(", ")]
#     if check_valid_index(row, col) and matrix[row][col] == "B":
#         matrix[row][col] = 0
#         get_score(col)
#
# if 100 > total_score[0]:
#     print(f"Sorry! You need {100 - total_score[0]} points more to win a prize.")
# else:
#     if 100 <= total_score[0] <= 199:
#         prize = "Football"
#     elif total_score[0] <= 299:
#         prize = "Teddy Bear"
#     elif total_score[0] >= 300:
#         prize = "Lego Construction Set"
#     print(f"Good job! You scored {total_score[0]} points, and you've won {prize}.")


matrix_size = 6

throws = 0

points = 0

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(matrix_size)]

football = 0
teddy_bear = 0
lego_construction = 0

while throws < 3:

    throws += 1

    row, col = [int(x) for x in input()[1:-1].split(", ")]

    if row >= matrix_size or col >= matrix_size:
        continue

    if matrix[row][col] == "B":

        for t_row in range(matrix_size):

            if isinstance(matrix[t_row][col], int):

                points += matrix[t_row][col]

            matrix[t_row][col] = "-"

if 100 <= points <= 199:

    prize = "Football"
    football += 1

elif 200 <= points <= 299:

    prize = "Teddy Bear"
    teddy_bear += 1

elif points >= 300:

    prize = "Lego Construction Set"
    lego_construction += 1

if football or teddy_bear or lego_construction:

    print(f"Good job! You scored {points} points, and you've won {prize}.")

else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")