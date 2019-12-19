def ParseTidesFile( filename ):
    File = open(filename,"r")

    Records = []
    for line in File:

        Record = line.split(",")
        Record[1] = float(Record[1])

        Record[2] = Record[2].replace("meters", "");
        Record[2] = Record[2].replace("\n", "");
        Record[2] = float(Record[2])

        Records.append(Record)

    File.close()
    return Records
def tidesperday(Records):
    max = 0
    min = 1000000
    mintime = 0
    maxtime = 0
    maxmintide = []
    for i in range (0,len(Records)):
        if Records[i][0] != Records[i-1][0] and i > 0:
            #print(Records[i-1][0], ": ", min, " meters at lowest and ", max, "meters at highest")
            maxmintide.append([Records[i-1][0],mintime,min,maxtime,max])
            max = 0
            min = 100000
        #for j in range(0,len(Records[i])):
        if Records[i][2] < min:
            mintime = Records[i][1]
            min = Records[i][2]
        if Records[i][2] > max:
            maxtime = Records[i][1]
            max = Records[i][2]
    #print(Records[i][0], ": ", min, " meters at lowest and ", max, "meters at highest")
    maxmintide.append([Records[i - 1][0], mintime, min, maxtime, max])
    for i in range(0,len(maxmintide)):
        print(maxmintide[i])
    return

file = ("Tides.txt")
#print(ParseTidesFile(file))
tidesperday(ParseTidesFile(file))