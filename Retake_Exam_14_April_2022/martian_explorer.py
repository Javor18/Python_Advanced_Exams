from collections import deque

matrix_size = 6

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

matrix = []

directions = {"up": [-1, 0],
              "down": [1, 0],
              "left": [0, -1],
              "right": [0, 1]}

for x_row in range(matrix_size):

    matrix.append(input().split())

    if "E" in matrix[x_row]:

        row, col = x_row, matrix[x_row].index("E")

commands = deque(input().split(", "))

while commands:

    direction = commands.popleft()

    row += directions[direction][0]
    col += directions[direction][1]

    # if direction == "down":
    #
    #     r_row += 1
    #
    # elif direction == "up":
    #     r_row -= 1
    #
    # elif direction == "left":
    #
    #     r_col -= 1
    #
    # elif direction == "right":
    #
    #     r_col += 1

    if row > matrix_size - 1:

        row = 0

    elif row < 0:

        row = matrix_size - 1

    if col > matrix_size - 1:

        col = 0

    elif col < 0:

        col = matrix_size - 1


    position = matrix[row][col]

    if position == "W":

        print(f"Water deposit found at ({row}, {col})")
        water_deposit += 1

    elif position == "M":

        print(f"Metal deposit found at ({row}, {col})")
        metal_deposit += 1

    elif position == "C":

        print(f"Concrete deposit found at ({row}, {col})")
        concrete_deposit += 1

    elif position == "R":

        print(f"Rover got broken at ({row}, {col})")
        break


if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:

    print("Area suitable to start the colony.")

else:

    print("Area not suitable to start the colony.")