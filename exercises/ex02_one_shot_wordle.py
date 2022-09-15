"""EX02 - One Shot Wordle - A bigger step to Wordle."""

__author__ = "730436720"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")
white: str = "\U00002B1C"
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"

if guess != secret:
    if len(guess) != len(secret):
        i: int = 0
        while i != len(secret):
            again: str = input(f"That was not {len(secret)} letters! Try again: ")
            i += len(again)
        if again != secret:
            j: int = 0
            k: int = 0
            ball: bool = False
            answer: str = ""
            while len(secret) > j and not ball:
                while k < len(secret):
                    m: int = 0
                    if again[k] == secret[m]:
                        answer += green
                        m += 1
                    else:
                        m += 1
                        if again[k] == secret[m]:
                            answer += yellow
                            m += 1
                        else:
                            m += 1
                            if again[k] == secret[m]:
                                answer += yellow
                                m += 1
                            else:
                                m += 1
                                if again[k] == secret[m]:
                                    answer += yellow
                                    m += 1
                                else:
                                    m += 1
                                    if again[k] == secret[m]:
                                        answer += yellow
                                        m += 1
                                    else:
                                        answer += white
                                        m += 1
                    k += 1
                ball = True
            print(f"{answer}")
            print("Not quite. Play again soon!") 
    else:
        None
else:
    l: int = 0
    answer: str = ""
    while len(guess) > l:
        if secret[l] == guess[l]:
            answer += green
        else:
            answer += white
        l += 1
    print(f"{answer}")
    print("Woo! You got it!")

""" 
    l: int = 0
    answer: str = ""
    while len(guess) > l:
        if secret[l] == guess[l]:
            answer += green
        else:
            answer += white
        l += 1 
    print(f"{answer}")
"""