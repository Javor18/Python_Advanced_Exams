def shopping_cart(*args):

    output, result = "", {"Soup": [], "Pizza": [], "Dessert": []}

    for info in args:

        if "Stop" in info:
            break

        type_of_meal, product = info

        if product not in result[type_of_meal]:
            if type_of_meal == "Soup" and len(result[type_of_meal]) != 3:

                result[type_of_meal].append(product)

            elif type_of_meal == "Pizza" and len(result[type_of_meal]) != 4:

                result[type_of_meal].append(product)

            elif type_of_meal == "Dessert" and len(result[type_of_meal]) != 2:

                result[type_of_meal].append(product)

    for s_meal, s_product in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):

        output += f"{s_meal}:\n"

        for item in sorted(s_product):

            output += f" - {item}\n"

    if len(output) == 22:

        output = "No products in the cart!"

    return output


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
