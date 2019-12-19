def bracketstack(userinput):
    stack = []
    for i in range (0,len(userinput)):
        if "(" in userinput[i]:
            stack.append("(")

        if ")" in userinput[i]:
            if len(stack) == 0:
                return False
            stack.pop()
    return True
userinput = input("ENTER A STRING YO: ")
print(bracketstack(userinput))