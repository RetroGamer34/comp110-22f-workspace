"""We will be continuing building utility functions."""

__author__ = "730436720"

x: list[int] = [1, 2, 3, 4]
print(x)
q: int = (x[0] // 2) + 1
print(q)
f: int = len(x)
print(f)

"""def only_evens(x: list[int]) -> list[int]:
    z: list[int] = []
    i: int = 0
    j: int = (x[i] // 2) + 1
    while i < len(x):
        if x[i] == j:
            z.append(x[i])
        else:
            None
    return z

y: list[int] = only_evens([1, 2, 4, 5])
print(y)"""



# y: list[int] = []
# w: int = int(input("What numbers will you be typing today? "))
# y.append(w)
# print(y)
# a: int = 1
# b: int = 1
# c: int = 1
# d: list[int] = []
# d.append(a)
# d.append(b)
# d.append(c)
# print(d)