def reverse(list_test):
    if len(list_test) == 1:
        return list_test
    else:
        print(list_test[1:])
        return reverse(list_test[1:]) + list_test[0:1]
list_test = [1,2,3,4,5,6]
print(reverse(list_test))
