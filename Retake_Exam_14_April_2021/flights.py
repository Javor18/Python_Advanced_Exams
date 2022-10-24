# def flights(*args):
#
#     result = {}
#
#     for x in range(0, len(args), 2):
#
#         if args[x] == "Finish":
#             break
#
#         destination, passengers = args[x], args[x + 1]
#
#         result[destination] = result.get(destination, 0) + passengers
#
#     return result
#
# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
#
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
#
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))

def flights(*args):

    flight = {}

    for x in range(0, len(args), 2):

        if args[x] == "Finish":
            break

        destination, people = args[x], args[x + 1]

        if not destination in flight:

            flight[destination] = people

        else:
            flight[destination] += people

    return flight

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))