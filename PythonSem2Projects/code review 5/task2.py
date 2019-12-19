class Item:
    def __init__(self, value=0, weight=0):
        assert type(weight) == int
        self.value = value
        self.weight = weight

    def __str__(self):
        return "(v={}: w={})".format(self.value, self.weight)

    def __repr__(self):
        return str(self)


def knapsack(item_list, capacity):
    assert len(item_list) > 0, "no items"
    assert capacity > 0, "no space to store"
    assert type(capacity) == int

    (rows, cols) = len(item_list)+1, capacity+1
    table = [[0 for i in range(cols)] for j in range(rows)]

    for i, item in enumerate(item_list, start=1):
        # print(table[i-1][21-item.weight])

        for j in range(1, capacity+1):

            if item.weight > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], item.value + table[i-1][j - item.weight])
        # print(table)

    maxWeight = capacity
    selectedKnapsack = []

    for upperBound in range(len(item_list), 0, -1):
        if table[upperBound][maxWeight] != table[upperBound-1][maxWeight]:
            selectedKnapsack.append(item_list[upperBound-1])
            maxWeight -= item_list[upperBound - 1].weight

    return [table[-1][-1], selectedKnapsack]


item1 = Item(4000, 20)
item2 = Item(3500, 10)
item3 = Item(1800, 9)
item4 = Item(400, 4)
item5 = Item(1000, 2)
item6 = Item(200, 1)
list_of_items = [item1, item2, item3, item4, item5, item6]
print(knapsack(list_of_items, 20))
