# from collections import deque
#
# pizza_orders = deque(int(x) for x in input().split(", ") if 11 > int(x) > 0)
# employees = deque(int(x) for x in input().split(", "))
#
# made_pizzas = 0
#
# while pizza_orders and employees:
#
#     order = pizza_orders.popleft()
#     employee_capacity = employees.pop()
#
#     if order > employee_capacity:
#         order -= employee_capacity
#         pizza_orders.appendleft(order)
#         made_pizzas += employee_capacity
#
#     else:
#         made_pizzas += order
#
# if not pizza_orders:
#
#     print("All orders are successfully completed!")
#     print(f"Total pizzas made: {made_pizzas}")
#
#     if employees:
#         print(f"Employees: {', '.join(str(x) for x in employees)}")
#
# else:
#
#     print("Not all orders are completed.")
#     print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")


from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
employees = deque(int(x) for x in input().split(", "))

made_pizzas = 0

while pizza_orders and employees:

    pizza_order = pizza_orders.popleft()
    employee_capacity = employees.pop()

    if pizza_order > 10:
        employees.append(employee_capacity)

    elif pizza_order <= 0:

        employees.append(employee_capacity)

    elif pizza_order > employee_capacity:

        pizza_order -= employee_capacity
        pizza_orders.appendleft(pizza_order)
        made_pizzas += employee_capacity

    else:
        made_pizzas += pizza_order

if not pizza_orders:

    print("All orders are successfully completed!")
    print(f"Total pizzas made: {made_pizzas}")

    if employees:

        print(f"Employees: {', '.join(str(x) for x in employees)}")

else:
    print("Not all orders are completed.")
    print(f'Orders left: {", ".join(str(x) for x in pizza_orders)}')
