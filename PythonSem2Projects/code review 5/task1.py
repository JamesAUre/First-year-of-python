def naivefib(n):
    if n <= 1:
        return n
    else:
        return naivefib(n-1) + naivefib(n-2)


def fibcount(n):
    if n <= 1:
        return 1
    else:
        return fibcount(n-1) + fibcount(n-2) + 1


def fibdynamic(n):
    if n <= 0:
        return 0
    mem = [0] * (n+1)
    mem[0] = 0
    mem[1] = 1
    for i in range(2, n+1):
        mem[i] = mem[i-1] + mem[i-2]
    return mem[n]


def dynamiccount(n):
    depth = 1
    if n <= 0:
        return depth
    mem = [0] * (n + 1)
    mem[0] = 0
    mem[1] = 1
    for i in range(2, n + 1):
        depth+=1
        mem[i] = mem[i - 1] + mem[i - 2]
    return depth


#print(naivefib(40))
print(fibdynamic(13))
print(dynamiccount(10))