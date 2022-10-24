# def shopping_list(money, **kwargs):
#
#     if money < 100:
#
#         return "You do not have enough budget."
#
#     type_of_products_count, output = 0, ""
#
#     for product, (price, quantity) in kwargs.items():
#
#         if price * quantity <= money:
#
#             total_price = price * quantity
#
#             output += f"You bought {product} for {total_price:.2f} leva.\n"
#
#             money -= total_price
#
#             type_of_products_count += 1
#
#             if type_of_products_count == 5:
#
#                 break
#
#     return output
#
# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

def shopping_list(money, **kwargs):

    if money < 100:
        return "You do not have enough budget."

    basket = set()

    products = []

    output = ""

    for product, (price, quantity) in kwargs.items():

        total_price = price * quantity

        if money >= total_price:

            money -= total_price

            output+= f"You bought {product} for {total_price:.2f} leva.\n"

            basket.add(product)

        if len(basket) == 5:

            break

    return output

print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
