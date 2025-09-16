my_foods = ['pizza', 'falafel', 'carrot cake']
# copying a list
friend_foods = my_foods[:]
# friend_foods = my_foods # will produce a pointer to the same object, and both
# list will have same elements when we append to one or the other list.

print("My Favorite foods are:")
print(my_foods)

print("\nFriend foods are:")
print(friend_foods)

my_foods.append('caprice')
friend_foods.append('vanillia')
print(my_foods)
print(friend_foods)
