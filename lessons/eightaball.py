"""Learning how to import, use random integer and elif statement"""

from random import randint

question: str = input("What is your yes/no question? ")
response: int = randint(0, 3)

if response == 0:
    print("Yes, definitely")
elif response == 1:
    print("Ask again later")
elif response == 2:
    print("Yes, of course!")
else:
    print("My sources say no")