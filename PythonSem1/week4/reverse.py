list = [1,2,3,4]

stack = []

while len(list)>0:
    if list[-1]%2 == 0:
        stack.append(list.pop())
        continue
    list.pop()


print(stack)
