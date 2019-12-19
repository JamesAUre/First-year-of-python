def reading():
    userlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(10):
        userlist[i] = int(input("Please enter number: "))
    return userlist


def finding_pairs(list):
    pairs = []
    for i in range(10):
        for j in range(i+1, 10):
            if checksum(list[i], list[j]) and checkproduct(list[i], list[j]):
                pairs.append([list[i], list[j]])
    return pairs


def checkproduct(num1, num2):
    if (num1 * num2) % 2 == 1:
        return True
    return False


def checksum(num1, num2):
    if (num1 + num2) % 2 == 0:
        return True
    return False
print(finding_pairs(reading()))