def inputlist():
    userinput = input('enter a list of numbers: ')
    upper_bound = userinput.split()
    upper_bound_1 = [int(item) for item in upper_bound]
    print(upper_bound_1)
    return upper_bound_1

def lexicoinitiate(lexicolist, upper_bound):
    while len(lexicolist) < len(upper_bound):
        lexicolist.append(0)
    return lexicolist

def lexicorecursion (lexicolist, upper_bound, i):
    while i >= 0:
        while lexicolist[i] < upper_bound[i]:
            lexicolist[i] += 1
            print (lexicolist)
        j = i
        while j < len(lexicolist):
            lexicolist[j] = 0
            j+= 1
        i -= 1
    return
def lexicograph(upper_bound):
    lexicolist = []
    lexicolist = lexicoinitiate(lexicolist, upper_bound)
    i = len(lexicolist) - 1
    lexicorecursion(lexicolist, upper_bound, i)
    print(lexicolist)
    return
lexicograph(inputlist())
