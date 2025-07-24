locations = ['peru', 'ecuador', 'colombia', 'italy', 'france']
print(f"Original order {locations}")

print(f"Sorted Temporary using sorted(): {sorted(locations)}")
print(f"After Sorted: {locations}")

print(f"Using sorted in reverse order: {sorted(locations, reverse=True)}")
print(f"Original List again: {locations}")

locations.reverse()

print(f"Using reverse: {locations}")
locations.sort()
print(f"List now: {locations}")
locations.sort(reverse=True)
print(f"List now in reverse: {locations}")
print()