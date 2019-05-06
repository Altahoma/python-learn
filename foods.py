my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print("-" + food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print("-" + food)

print("\nMy favorite food is: " + my_foods[-1])
print("But my fried favorite foods is:" + str(friend_foods[2:]))