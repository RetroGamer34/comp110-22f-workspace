"""Examples of the tuple and range sequences."""

# An example of a tuple w/o type aliasing
goat: tuple[str, int] = ("MJ", 23)

# Tuples are sequences, so they're 0-indexes
print(goat[0])
print(goat[1])

# Printing a tuple produces its literal syntax 
print(goat)

# Print both items on same line
print(f"{goat[0]} is number {goat[1]}")

# Sequences have length
print(len(goat))

# Sequences are iterable with for... in loops
# Meaning you can loop over them with for... in
for item in goat:
    print(item)

# Tuple, unlike lists, are immutable
# Which means we cannot reassigns items, nor append, nor pop, etc.
# goat[0] = "LBJ"

# We can "invent" our own type w/ a type alias
Player = tuple[str, int]

# Once we've aliased a type, we ca, 5n create variable of that type
unc_poy: Player = ("Bacot", 5)

# In a strange world, where jersey number changes...
unc_poy = (unc_poy[0], unc_poy[1] + 1)


# A range is another common sequence type
zero_to_nine: range = range(0 ,10, 1)

# The range on top will be the same as the bottom two
# zero_to_nine: range = range (0, 10) or zero_to_nine: range = range (10)

# We can access items of the range
print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)


# We can have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)


names: list[str] = ["Kris", "Alyssa", "Michael", "Lebron"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")


for i in range(0, len(names), 2):
    print(f"{i}. {names[i]}")
