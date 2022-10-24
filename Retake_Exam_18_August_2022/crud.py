# matrix_size = 6
#
# matrix = [input().split() for _ in range(matrix_size)]
#
# row_position, col_position = [int(x) for x in input()[1:-1].split(",")]
#
# directions = {"up": [-1, 0],
#               "down": [1, 0],
#               "left": [0, -1],
#               "right": [0, 1]}
#
#
# def add_step(row, col, direction):
#     return row + directions[direction][0], col + directions[direction][1]
#
#
# def number_or_letter():
#     return matrix[row_position][col_position].isalpha() or matrix[row_position][col_position].isdigit()
#
#
# def create(value):
#     if matrix[row_position][col_position] == ".":
#         matrix[row_position][col_position] = value
#
#
# def update(value):
#     matrix[row_position][col_position] = value
#
#
# def delete(_):
#     matrix[row_position][col_position] = "."
#
#
# def read(_):
#     print(matrix[row_position][col_position])
#
#
# commands = {
#     "Create": create,
#     "Update": update,
#     "Read": read,
#     "Delete": delete
# }
#
#
# command, commands_no_create = input(), tuple(commands.keys())[1:]
#
# while command != "Stop":
#     command_type, *info = command.split(", ")
#     row_position, col_position = add_step(row_position, col_position, info[0])
#     if command_type in commands_no_create:
#         if number_or_letter():
#             commands[command_type](info[-1])
#     else:
#         commands[command_type](info[-1])
#     command = input()
#
# [print(*matrix[row]) for row in range(matrix_size)]


matrix_size = 6

directions = {"up": [-1, 0],
              "down": [1, 0],
              "right": [0, 1],
              "left": [0, -1]}

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(matrix_size)]

row, col = map(int, input()[1:-1].split(", "))

while True:

    command = input()

    if "Stop" in command:

        break

    line = command.split(", ")

    if len(line) > 2:

        task, direction, value = line

    else:
        task, direction = line

    row += directions[direction][0]
    col += directions[direction][1]

    if task == "Create":

        if matrix[row][col] == ".":

            matrix[row][col] = value

    elif task == "Update":

        if isinstance(matrix[row][col], int) or matrix[row][col].isalpha():
            matrix[row][col] = value

    elif task == "Delete":

        if isinstance(matrix[row][col], int) or matrix[row][col].isalpha():
            matrix[row][col] = "."


    elif task == "Read":

        if isinstance(matrix[row][col], int) or matrix[row][col].isalpha():

            print(matrix[row][col])

for line in matrix:

    print(' '.join(str(x) for x in line))