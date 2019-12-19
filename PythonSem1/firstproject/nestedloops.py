x = 1
y = 1

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
for x in range(x,m+1):
    for y in range(y,n):
        print(x*y, end = " ")
        y = y + 1
    print(x * y)
    x = x + 1
    y=1
x=1