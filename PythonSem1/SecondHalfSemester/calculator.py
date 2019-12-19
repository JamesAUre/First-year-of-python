def tokenization(expr):
    startingpos = 0
    tokens = {"^", "/", "*", "-", "+","(",")"}
    splitexpr = []

    for i in range(0 , len(expr)):
        if expr[i] in tokens:
            splitexpr.append(expr[startingpos:i])
            splitexpr.append(expr[i])
            startingpos = i+1

    splitexpr.append(expr[startingpos:i+1])

    while "" in splitexpr:
        splitexpr.remove("")

    return splitexpr
def has_presedence(op1,op2):
    tokens = ["^", "/", "*", "-", "+", "(", ")"]

    for i in range(0, len(tokens)):
        if op1 == tokens[i]:
            return True
        if op2 == tokens[i]:
            return False

def simple_evaluation(tokens):
    base = 0
    try:
        while len(tokens) > 1:
            for i in range (0, len(tokens)):
                if has_presedence(tokens[i],tokens[base]):
                    base = i

            result = str(operation(float(tokens[base-1]),float(tokens[base+1]),tokens[base]))
            tokens.pop(base - 1)
            tokens.pop(base - 1)
            tokens.pop(base - 1)
            tokens.insert(base-1, result)
            base = 0
        return float(tokens[0])
    except:
        print("SYNTAX ERROR")
        exit()

def operation (a,b,operate):
    if operate == '^': return a**b
    elif operate == "/": return a/b
    elif operate == "*": return a*b
    elif operate == "-": return a-b
    elif operate == "+": return a+b

def complex_evaluation(tokens):
    while "(" in tokens:
        startindex = tokens.index("(")
        count = 0
        endindex = startindex

        for i in range(startindex + 1, len(tokens)):
            if "(" == tokens[i]:
                count += 1
            if ")" == tokens[i]:
                if count == 0:
                    endindex = i
                    break
                count -= 1

        tokens.insert(startindex, complex_evaluation(tokens[startindex+1: endindex]))
        while startindex != endindex:
            tokens.pop(startindex+1)
            endindex -= 1
        tokens.pop(startindex+1)
        print(tokens)

    return str(simple_evaluation(tokens))

    #evalu = complex_evaluation(tokens[startindex:i-1])
    #print(tokens[0:startindex] + [evalu] + tokens[i+1:])
    #tokens = tokens[0:startindex] + [evalu] + tokens[i+1:]

print("CALCULATOR MADE BY JAMES URE 5/14/2019")

while True:
    equation = input("enter an equation: ")
    splitstring = tokenization(equation)

    print('ANSWER: ', complex_evaluation(splitstring))