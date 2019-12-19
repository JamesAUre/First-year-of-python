import random
def beats(choice1, choice2,choices):
    i=(choices.index(choice1))
    if (i - 1) % 3 == choice2:
        print(choice1, "beats", choices[choice2])
        return True

    elif (i + 1) % 3 == choice2:
        print(choice1, "loses to", choices[choice2])
        return False
    else:
        print(choice1, "draws", choices[choice2])
        return False

choices = ["Rock", "Paper", "Scissors"]
choice1 = input("Enter choice 1: ")
choice2 = random.randrange(0,3)
print(beats(choice1, choice2,choices))