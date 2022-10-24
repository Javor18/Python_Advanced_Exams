from collections import deque

# seats = input().split(", ")
#
# first_sequence = deque(int(x) for x in input().split(", "))
#
# second_sequence = deque(int(x) for x in input().split(", "))
#
#
# taken_seats = []
#
# rotations = 0
#
# while rotations < 10:
#
#     taken_seat = False
#
#     rotations += 1
#
#     first_num = first_sequence.popleft()
#     second_num = second_sequence.pop()
#
#     letter = chr(first_num + second_num)
#
#     for seat in (f"{first_num}{letter}", f"{second_num}{letter}"):
#
#         if seat in seats:
#
#             taken_seat = True
#
#             seats.remove(seat)
#
#             taken_seats.append(seat)
#
#
#     if taken_seat == False:
#
#         first_sequence.append(first_num)
#         second_sequence.appendleft(second_num)
#
#     if len(taken_seats) == 3:
#
#         break
#
# print(f"Seat matches: {', '.join(str(x) for x in taken_seats)}")
#
# print(f"Rotations count: {rotations}")



available_seats = input().split(", ")
first_sequence = deque(int(x) for x in input().split(", "))
second_sequence = deque(int(x) for x in input().split(", "))

rotations = 0
found_seats = []

while first_sequence and second_sequence:

    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()

    taken_seats = False

    letter = chr(first_num + second_num)

    if rotations == 10 or len(found_seats) == 3:

        break

    for seat in (f'{first_num}{letter}', f'{second_num}{letter}'):

        if seat in available_seats:

            available_seats.remove(seat)
            taken_seats = True
            found_seats.append(seat)

    if taken_seats == False:

        first_sequence.append(first_num)
        second_sequence.appendleft(second_num)

    rotations += 1

print(f'Seat matches: {", ".join(str(x) for x in found_seats)}')
print(f"Rotations count: {rotations}")