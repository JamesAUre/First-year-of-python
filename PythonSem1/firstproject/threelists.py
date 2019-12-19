def max(a_list):
    highest = list[0]
    for x in list:
        if x > highest:
            highest = x

    return highest

def min(a_list):
    lowest = list[0]
    for x in list:
        if x < lowest:
            lowest = x
    return lowest

list = [1,2,3,4]

range = max(list) - min(list)

if range == 0:
    print ("L has a narrow range.")

elif range > 0 and range <= 100:
    print ("L has a normal range.")

else: print ("L has a wide range.")

print(range)