SORTINGLIST = [1,4,2,3,6,3,9,4,3,2]

for i in range (0,len(SORTINGLIST)):
    for j in range(i, len(SORTINGLIST)):
        minvalue = 0
        if minvalue < list[j]:
            minvalue = list[j]
            list.index[minvalue]

    list[j],list[i]=list[i],list[j]
