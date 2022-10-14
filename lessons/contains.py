"""Example implementing a list utility function"""

# Function name: contains
# We will have 2 parameters: needle (str), haystack (list[str])
# Return type bool
def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack):
        if haystack [i] == needle:
        #     2.A  True return True! We found it!
            return True
        i += 1
    return False