def minIndex(L):
    minIndex = 0
    min_value = L[0][0]
    for i in range (1,len(L)):
        if min_value > L[i][0]:
            min_value= L[i][0]
            minIndex = i
    return minIndex

def maxIndex(L):
    maxIndex = 0
    max_value = L[0][1]
    for i in range (1,len(L)):
        if max_value > L[i][1]:
            max_value= L[i][1]
            maxIndex = i
    return maxIndex

def selectionSortDistance(Records):
    for i in range(0, len(Records)):
        minPos = minIndex(Records[i:]) + i
        #Records[minPos][i] = Records[i][minPos]
        Records[minPos], Records[i] = Records[i], Records[minPos]
    return Records

def selectionSortPrice(Records):
    for i in range(0, len(Records)):
        maxPrice = maxIndex(Records[i:]) + i
        #Records[minPos][i] = Records[i][minPos]
        Records[maxPrice], Records[i] = Records[i], Records[maxPrice]
    return Records

def nice_printing(Records):
    for i in range (0,len(Records)):
        print(Records[i][0], " kms, $", Records[i][1])

def initialize():
    userinput = input("Enter name of file: ")
    file = open(userinput)
    Records = []
    for line in file:
        Record = line.split(",")
        Record[0] = int(Record[0])

        #Record[1] = Record[1].replace("\n","")
        Record[1] = float(Record[1])
        Records.append(Record)

        #print(Record[0], " kms, $", Record[1])
    #nice_printing(Records)
    return Records

Records = initialize()

while True:
    userinput = input("Enter choice Print, Sort1 (distance), Sort2 (price) or Quit: ")
    userinput.split(",")

    if "Print" in userinput:
        nice_printing(Records)

    if "Sort1" in userinput:
        selectionSortDistance(Records)

    if "Sort2" in userinput:
        selectionSortPrice(Records)

    if "Quit" in userinput:
        quit()

