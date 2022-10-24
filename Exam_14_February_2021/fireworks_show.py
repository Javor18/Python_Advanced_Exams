# from collections import deque
#
# firework_effects = deque(int(x) for x in input().split(", "))
#
# explosive_powers = deque(int(x) for x in input().split(", "))
#
# palm_fireworks = 0
#
# willow_fireworks = 0
#
# crossette_fireworks = 0
#
# perfect_show = False
#
# while firework_effects and explosive_powers:
#
#     firework_effect = firework_effects.popleft()
#
#     explosive_power = explosive_powers.pop()
#
#     sum = firework_effect + explosive_power
#
#     if firework_effect <= 0:
#
#         explosive_powers.append(explosive_power)
#         continue
#
#     if explosive_power <= 0:
#
#         firework_effects.appendleft(firework_effect)
#         continue
#
#     if sum % 3 == 0 and sum % 5 != 0:
#
#         palm_fireworks += 1
#
#     elif sum % 5 == 0 and sum % 3 != 0:
#
#         willow_fireworks += 1
#
#     elif sum % 3 == 0 and sum % 5 == 0:
#
#         crossette_fireworks += 1
#
#     else:
#
#         firework_effect -= 1
#
#         firework_effects.append(firework_effect)
#
#         explosive_powers.append(explosive_power)
#
#     if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
#
#         perfect_show = True
#
#         print("Congrats! You made the perfect firework show!")
#
#         break
#
# if perfect_show == False:
#
#     print("Sorry. You can't make the perfect firework show.")
#
# if firework_effects:
#
#     print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
#
# if explosive_powers:
#     print(f" Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")
#
# print(f"Palm Fireworks: {palm_fireworks}")
#
# print(f"Willow Fireworks: {willow_fireworks}")
#
# print(f"Crossette Fireworks: {crossette_fireworks}")





from collections import deque

firework_effects = deque(int(x) for x in input().split(", "))
explosive_powers = deque(int(x) for x in input().split(", "))

palm_fireworks = 0
willow_fireworks = 0
crossete_fireworks = 0

perfect_show = False

while firework_effects and explosive_powers:

    firework_effect = firework_effects.popleft()
    explosive_power = explosive_powers.pop()

    value = firework_effect + explosive_power

    if firework_effect <= 0:
        explosive_powers.append(explosive_power)
        continue

    if explosive_power <= 0:
        firework_effects.appendleft(firework_effect)
        continue

    if value % 3 == 0 and value % 5 != 0:

        palm_fireworks += 1

    elif value % 5 == 0 and value % 3 != 0:

        willow_fireworks += 1

    elif value % 3 == 0 and value % 5 == 0:

        crossete_fireworks += 1

    else:
        firework_effect -= 1
        firework_effects.append(firework_effect)
        explosive_powers.append(explosive_power)

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossete_fireworks >= 3:

        perfect_show = True
        break

if perfect_show == True:

    print("Congrats! You made the perfect firework show!")

else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:

    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")

if explosive_powers:

    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossete_fireworks}")
