# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
#
# print("You ordered a " + pizza['crust'] + "-crust pizza " +
#       "with the following toppings:")
#
# for topping in pizza['toppings']:
#     print("\t" + topping)


def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
