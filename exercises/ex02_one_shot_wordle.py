"""EX02 - One Shot Wordle - A bigger step to Wordle."""

__author__ = "730436720"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")
white: str = "\U00002B1C"
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"

if len(guess) != len(secret):
    length: int = 0
    while length < len(secret):
        length -= length
        again: str = input(f"That was not {len(secret)} letters! Try again: ")
        length += len(again)
    if again != secret:
        hashtag: int = 0
        answer: str = ""
        while len(guess) > hashtag:
            if secret[hashtag] == guess[hashtag]:
                answer += green
            else:
                answer += white
            hashtag += 1
        print(f"{answer}")
        print("Not quite. Play again soon!") 
elif guess == secret:
    integer: int = 0
    answers: str = ""
    while len(guess) > integer:
        if secret[integer] == guess[integer]:
            answers += green
        else:
            answers += white
        integer += 1
    print(f"{answers}")
    print("Woo! You got it!")
else:
    num: int = 0
    ans: str = ""
    while len(guess) > num:
        if secret[num] == guess[num]:
            ans += green
        else:
            ans += white
        num += 1
    print(f"{ans}")
    print("Not quite. Play again soon!") 