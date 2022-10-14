"""Demonstration of dictionaries capabilities."""


# Declaring the type of a dictionary (dict).
schools: dict[str, int]

# Initialize to an empty dict
schools = dict()

# Set a key-value pairing in the dict | "_" means a comma in Python
schools["UNC"] = 19_400
schools["Duke"] = 6717
schools["NCSU"] = 26_150

# Print a dict literal representation
print(schools)

# Access a value by its key -- "Lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dict
# by its key.
schools.pop("Duke")

# Test form the existence of a key
is_duke_present: bool = "Duke" in schools

points: dict[str, int] = {"Kris": 0, "Kaki": 10}
points["Kaki"] += 100
print(points)