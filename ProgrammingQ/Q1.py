# reads input from user to create a list of integers
def reading():
    userlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(10):
        userlist[i] = int(input("Please enter number: "))
    return userlist


# main function for creating all valid pairs
# ASSUMPTION: no redundant pairs e.g. [1,2] and [2,1], instead only [1,2]
def finding_pairs(list):
    pairs = []
    for i in range(10):
        for j in range(i+1, 10):
            if checksum(list[i], list[j]) and checkproduct(list[i], list[j]):
                pairs.append([list[i], list[j]])
    return pairs


# checks to see if products are valid
def checkproduct(num1, num2):
    if (num1 * num2) % 2 == 1:
        return True
    return False


# checks to see if sums are valid
def checksum(num1, num2):
    if (num1 + num2) % 2 == 0:
        return True
    return False

# runs functions and prints result
print(finding_pairs(reading()))
