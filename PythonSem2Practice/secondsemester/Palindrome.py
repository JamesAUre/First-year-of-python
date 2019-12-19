list1 = ['yes', 'random']
list2 = ['random','no']

for i in range (len(list1)):
    for j in range (len(list2)):
        if list1[i] == list2[j]:
            print('true')
            exit()

print('false')