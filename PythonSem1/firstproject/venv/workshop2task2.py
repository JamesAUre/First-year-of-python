total = 0

start = int(input("Enter start: "))
finish = int(input("Enter finish: "))
#divisible = int(input("Valid i values are those divisible by: "))
for i in range (start,finish+1):
    for j in range(1,i+1):
        #if i % divisible == 0:
        total += (2 * (i ** 2) + (4 * j))



print (total)
