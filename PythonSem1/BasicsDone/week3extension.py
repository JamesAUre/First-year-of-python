import random
userlength = int(input("Enter amount of cards: "))
list = []
for i in range (0,userlength):
    if random.randint(0,1) == 1:
        list.append('X')
    else: list.append('O')
print (list)
while ('X' in list):
        userinput = int(input("Enter card to flip: "))
        if list[userinput-1] == 'X':
            list[userinput - 1] = 'O'
        else:
            list[userinput - 1] = 'X'
        if userinput - 2 >= 0:
            if list[userinput-2] == 'X':
                list[userinput-2] = 'O'
            else:
                list[userinput-2] = 'X'
        print (list)
print ("LOL GG")