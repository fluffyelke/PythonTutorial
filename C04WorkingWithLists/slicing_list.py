players = ['caprice', 'alaina', 'vanya', 'elinna', 'melena']
# start from begin to index - 1
print(players[0:3])

# slice from index to index - 1
print(players[2:4])

# slice from begin to index - 1

print(players[:3])

# from index to end
print(players[2:])

# print last 3 elements
print(players[-3:])

numbers = [num for num in range(1, 1000)]
print(numbers)

# print every 5 elements of the list
print(numbers[0:100:5])

# looping through a slice
print("Here are my favorite numbers")
for number in numbers[:100:3]:
    print(number, end=' ')

