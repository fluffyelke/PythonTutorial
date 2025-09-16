import random

magicians = ['alice', 'caprice', 'vanya']
# simple for loop iterating over list.
for magician in magicians:
    print(magician)
print()

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print()

# using range()
for value in range(1, 10):
    print(value, end=" ")
print()

# using range() to create List of numbers
numbers = list(range(10, 21))
print(numbers, end=' ')
print()

# using range() and using skip a patterns of numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# using min()
digits = [5, 15, 25, 1, 3, 35, 55, 23]
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehensions
squares = [pow(value, 3) for value in range(1, 11)]
print(squares)

# counting to 20
for number in range(1, 21):
    print(number, end = ' ')
print()

numbers = [number for number in range(1, 1000000)]
print(numbers, end = ' ')
print()
random.shuffle(numbers)
print(numbers)
print(sum(numbers))

print(list(range(1, 20, 2)))

multiplies_of_3 = [pow(value, 3) for value in range(3, 30)]
print(multiplies_of_3)
