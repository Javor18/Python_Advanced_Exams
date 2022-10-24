first_player, second_player = input().split(", ")

matrix_size = 6

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(matrix_size)]

counter = 0

while True:

    counter += 1

    row, col = map(int, input()[1:-1].split(", "))

    letter = matrix[row][col]

    if letter == "E":

        if counter % 2 != 0 :

            print(f"{first_player} found the Exit and wins the game!")

        elif counter % 2 == 0 :

            print(f"{second_player} found the Exit and wins the game!")

        break

    elif letter == "T":

        if counter % 2 != 0 :

            print(f"{first_player} is out of the game! The winner is {second_player}.")


        elif counter % 2 == 0:

            print(f"{second_player} is out of the game! The winner is {first_player}.")

        break

    elif letter == "W":

        if counter % 2 != 0:

            print(f"{first_player} hits a wall and needs to rest.")

        elif counter % 2 == 0:

            print(f"{second_player} hits a wall and needs to rest.")