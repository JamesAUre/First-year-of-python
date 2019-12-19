list = [3,5,3,2,6,5,3,8]

def sorting(list):

    """
    :param a list of numerically comparable elements
    :return a list of sorted elements from the lowest values on the left to the highest values on the right
    :precondition: input must be a list of numbers
    :postcondition: output will be a list of numbers of the same list size inputted.
    :complexity: best case O(n), worst case O(n^2) where n is the number of elements in the list
    :stability: stable because elements of a list will only swap if the value to the right is less or
    if the value to the left is greater. Hence two equal elements will remain in the same order for both input
    and output.
    """

    swapped = True
    left = 0
    right = len(list)-1

    while right - left > 1 and swapped:
        swapped = False

        for i in range(left, right):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                swapped = True
        right = right - 1

        for i in range(right, left, -1):
            if list[i] < list[i-1]:
                list[i],list[i-1] = list[i-1],list[i]
                swapped = True
        left = left + 1

    return list


def splitnadd(num):
    digit = 0
    total = 0
    while(num>0):
        digit = num%10
        num = num//10
        total = total + digit
    return total



print(sorting(list))