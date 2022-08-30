"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730436720"

"""The name 'Go (ご/五)' in Japanese means the number 5."""
go: str = str(input("Enter a 5-character word: "))
go_num: int = int(len(go))

if go_num == 5:
    None
else:
    print("Error: Word must contain 5 characters.")
    exit()

"""The name 'ichi (いち/一)' in Japanese means 1."""
ichi: str = str(input("Enter a single-character: "))
ichi_num: int = int(len(ichi))

if ichi_num == 1:
    None
else:
    print("Error: Character must be single character.")
    exit()

print("Searching for " + str(ichi) + " in " + str(go))

indexes: int = 0

letter: int = 0

if ichi == go[0]:
    print(str(ichi) + " found at index " + str(indexes))
    indexes = indexes + 1
    letter = letter + 1
else:
    indexes = indexes + 1
if ichi == go[1]:
    print(str(ichi) + " found at index " + str(indexes))
    indexes = indexes + 1
    letter = letter + 1
else:
    indexes = indexes + 1
if ichi == go[2]:
    print(str(ichi) + " found at index " + str(indexes))
    indexes = indexes + 1
    letter = letter + 1
else:
    indexes = indexes + 1
if ichi == go[3]:
    print(str(ichi) + " found at index " + str(indexes))
    indexes = indexes + 1
    letter = letter + 1
else:
    indexes = indexes + 1
if ichi == go[4]:
    print(str(ichi) + " found at index " + str(indexes))
    letter = letter + 1
else:
    None
if letter == 0:
    print("No instances of " + str(ichi) + " found in " + str(go))
elif letter == 1:
    print(str(letter) + " instance of " + str(ichi) + " found in " + str(go))
else:
    print(str(letter) + " instances of " + str(ichi) + " found in " + str(go))