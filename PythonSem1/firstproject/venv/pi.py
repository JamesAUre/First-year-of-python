import math
def basel(precision):
    x=1.0
    n=2
    while math.sqrt(6*x)-math.pi >= precision or math.sqrt(6*x)-math.pi <= -precision:
        x = x + (1/(n**2))
        n = n + 1

    x = math.sqrt(6*x)
    n=n-1
    return x, n

def taylor(precision):
    x=1.0
    n=3
    switch = -1
    while (4*x)-math.pi >= precision or (4*x)-math.pi <= -precision:
        x = x + switch*(1/n)
        switch = switch * -1
        n = n + 2
    x=(4*x)
    n=(n-1)//2
    return x,n

def wallis(precision):
    x=4/3
    n=4

    while(2*x)-math.pi >= precision or (2*x)-math.pi <= -precision:
        x = x * ((n**2)/((n-1)*(n+1)))
        n = n + 2
    x=(2*x)
    n=(n//2)-1
    return x,n
def spigot(precision):
    x=1
    counter = 1
    y = 1
    total = 1
    while (2*x)-math.pi >= precision or (2*x)-math.pi <= -precision:
        for i in range(0,counter):
            y = y + 2
            total = total * ((y-1)/2)/y
            #print(total)
        x = x + total
        total = 1
        y=1
        counter += 1
    x=x*2

    return x, counter

def min_index(lst):
    k=0
    for i in range(1,len(lst)):
        if lst[i][1]<lst[k][1]:
            k=i
    return k
#efficiency comparer
def race(precision, algorithms):
    i = 0
    list=[]
    if "BASEL" in algorithms:
        algorithms.remove("BASEL")
        list.append([1,basel(precision)[1]])
    if "TAYLOR" in algorithms:
        algorithms.remove("TAYLOR")
        list.append([2,taylor(precision)[1]])
    if "WALLIS" in algorithms:
        algorithms.remove("WALLIS")
        list.append([3,wallis(precision)[1]])
    if "SPIGOT" in algorithms:
        algorithms.remove("SPIGOT")
        list.append([4,spigot(precision)[1]])

    for i in range (len(list)):
        j = min_index(list[i:]) + i

        list[j],list[i] = list[i],list[j]

    return list

def print_results(resultlist):
    for i in range (0,len(resultlist)):
        print("Algorithm", resultlist[i][0], "finished in", resultlist[i][1], "steps")

    return
#main/user input &  output
userinput = float(input("Enter precision for pi: "))
formulaList = [basel(userinput), basel(userinput), wallis(userinput)]

print("basel problem: ", basel(userinput))
print("taylor expansion: ", taylor(userinput))
print("wallis algorithm: ", wallis(userinput))
print("spigot algorithm: ", spigot(userinput))

formulapick = (input("Enter algorithms for comparison: "))
formulaListpick = formulapick.upper().split()

racelist = race(userinput,formulaListpick)
print("integer pairs: ", racelist)

print_results(racelist)