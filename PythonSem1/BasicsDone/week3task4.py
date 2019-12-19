mylist = []

for i in range(1,6):
    userinput = input("pls enter numbers: ")
    listinput = userinput.split()

    for a in range(0, len(listinput)):
        if listinput[a].count('.') != 0:
            listinput[a] = float(listinput[a])
        else:
            listinput[a] = int(listinput[a])

    mylist.append(listinput)

print(mylist)