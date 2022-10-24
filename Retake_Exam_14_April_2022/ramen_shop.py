from collections import deque

bowls_of_ramen = deque(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))

while bowls_of_ramen and customers:

    ramen_value = bowls_of_ramen.pop()
    customer_value = customers.popleft()

    if ramen_value > customer_value:

        ramen_value -= customer_value
        bowls_of_ramen.append(ramen_value)

    elif customer_value > ramen_value:

        customer_value -= ramen_value
        customers.appendleft(customer_value)

if not customers:

    print("Great job! You served all the customers.")

    if bowls_of_ramen:

        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")

else:

    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")