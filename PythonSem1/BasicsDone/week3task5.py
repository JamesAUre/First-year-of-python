from random import randint
mylist = []
tally = 0
for i in range (0,1000):
    diceroll = randint(1,6)
    mylist.append(diceroll)

for i in range (0, len(mylist)):
    tally += mylist[i]
    average = tally/1000
print (average)
