secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
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
            boll: bool = False
            answer: str = ""
            while len(secret) > j and not ball:
                m: int = 0
                while k < len(secret):
                    print(f"{m}")
                    if again[m] == secret[k]:
                        answer += green
                        m += 1
                    elif again[m] != secret[k]:
                        while again[m] == secret[k] and not boll:
                            again += yellow
                            m += 1
                        
                    else:
                        answer += white
                        m += 1
                    k += 1
                    print(f"{m}+{answer}")
                ball = True
            print(f"{answer}")
            print("Not quite. Play again soon!")

"""
if again[k] == secret[m]:
                        answer += green
                    else:
                        if again[k] == secret[m]:
                            answer += yellow
                        else:
                            m += 1
                            if again[k] == secret[m]:
                                answer += yellow
                            else:
                                if again[k] == secret[m]:
                                    answer += yellow
                                else:
                                    if again[k] == secret[m]:
                                        answer += yellow
                                    else:
                                        answer += white
"""