counter = 0
list = [None]*5
while(counter<5):
    userinput = int(input("pls enter number: "))
    list[counter] = userinput**2
    counter+=1
print(list)