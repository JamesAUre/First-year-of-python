import random

def coinflip():
    heads = 0
    tails = 0
    unknown = 0
    userinput = int(input("How times would you like to flip the coin? "))
    for i in range(0,userinput):
        x = random.randrange(0, 3)
        if  x == 0:
            heads = heads + 1

        elif x == 1: tails = tails + 1

        elif x == 2: unknown = unknown + 1

    print(heads, "heads,", tails, "tails and", unknown, "unknowns")
    return

coinflip()