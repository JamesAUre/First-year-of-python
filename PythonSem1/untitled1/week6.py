def greedy_items(items,capacity):
    greedylist = []
    space = 0
    while len(items) > 0:
        bestIndex = best_item(items)
        if space_left(items[bestIndex][0],space,capacity):
            space+=items[bestIndex][0]
            greedylist.append(items[bestIndex])
        items.pop(bestIndex)
    return greedylist

def compare_items(A,B):
    if A[0] < B[0]:
        return True
    return False

def space_left(bestItem, space, capacity):
    if bestItem + space <= capacity:
        return True
    return False

def best_item(records):
    bestvalue = 0
    for i in range (0,len(records)):
        if compare_items(records[i],records[bestvalue]):
            bestvalue = i
    return bestvalue

def Parseitems( filename ):

    File = open(filename,"r")

    records = []
    for line in File:

        line = line.replace("\n"," ")
        line = line.split(" ")

        kilos = line[0]
        kilos = int(kilos.replace("kg", ""))

        price = line[1]
        price = int(price.replace("$",""))

        records.append([kilos,price])
    File.close()
    return records
def nice_printing(thealgorithm):
    totalweight = 0
    totalcost = 0
    for i in range (len(thealgorithm)):
        print("steal item", i+1, "with ", thealgorithm[i][0], "kg and $", thealgorithm[i][1])
        totalweight += thealgorithm[i][0]
        totalcost += thealgorithm[i][1]
    print("total weight is", totalweight, "kg and total cost is $", totalcost)

    return

print(Parseitems("items.txt"))

nice_printing(greedy_items(Parseitems("items.txt"),10))
