maxnumber = int(input("Enter max number: "))

digits = len(str(maxnumber))
for i in range(0,maxnumber+1):
    length = len(str(i))
    zeros = digits-length
    xstr = str(i)
    for j in range(0,zeros):
        xstr = '0' + xstr
    print (xstr)