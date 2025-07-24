guests = ['vanya', 'elinna', 'stella', 'caprice', 'alaina']
for guest in guests:
    print(f"Greetings, {guest.title()}, welcome to the dinner")
print()
print(f'{guests[1].title()} wont be available for tonight')
del guests[1]
for guest in guests:
    print(f"Greetings, {guest.title()}, welcome to the dinner")
print()
print("We found a bigger table")
guests.insert(0, 'lexi')
guests.insert(int(len(guests) / 2), 'maria')
guests.insert(len(guests), 'penny')
guests.append('adria')
print(guests)
for guest in guests:
    print(f"Greetings, {guest.title()}, welcome to the dinner")
print()

print("We can only invite 2 people for dinner")
print(f'Aurevaur {guests.pop().title()}')
print(f'Aurevaur {guests.pop().title()}')
print(f'Aurevaur {guests.pop().title()}')
print(f'Aurevaur {guests.pop().title()}')
print(f'Aurevaur {guests.pop().title()}')
print(f'Aurevaur {guests.pop().title()}')
print(guests)
del guests[1]
del guests[0]
print(guests)
