bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

for bike in bicycles:
    print(bike, end=' ')
print()

for bike in bicycles:
    print(bike.title(), end=' ')
print()

print(bicycles[0])
print(bicycles[2].title())
print(bicycles[3].upper())

# accessing last element in the list
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('asprilla')
print(motorcycles)

# empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# insert element at any position
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(1, 'ducati')
print(motorcycles)

# remove element from the list, the element is lost, if you want to use
# removed element use pop() method
del motorcycles[1]
print(motorcycles)

# using pop(), default returns the last element in the list, if you want
# specific element position to pop(), use pop(index)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_elem = motorcycles.pop()
print(motorcycles)
print(popped_elem)

names = ['vanya', 'caprice', 'elinna', 'alaina']
print(len(names))
print(names)
name_caprice = names.pop(1)
print(names)
print(len(names))
print(name_caprice.title())

# remove() if you want to remove element by value use remove() method
names = ['vanya', 'caprice', 'elinna', 'alaina']
print(names)
names.remove('elinna')
print(names)

# sorting a list permanently with sort() method, alphabetical is default order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

# reverse
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily with the sorted() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

new_car_list = sorted(cars)
print(new_car_list)

names = ['vanya', 'caprice', 'elinna', 'alaina']
print(names)

names.reverse()
print(names)