def coins(coinlist):
    profit = [0] * len(coinlist)
    for i in range(0, len(coinlist)):
        profit[i] = max(coinlist[i] + profit[i-2], profit[i-1])
    return profit

def coins2(items):
    n = len(items)
    profit = [0] * n
    profit[0] = items[0]
    profit[1] = max(items[0], items[1])
    for i in range(2, n):
        profit[i] = max(items[i] + profit[i-2], profit[i-1])
    return profit[-1]

coinlist = [7,2,10,12,5]
print(coins(coinlist))
