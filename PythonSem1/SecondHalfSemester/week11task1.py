def min_child(v, heap):
    right = v * 2 + 2
    left = v * 2 + 1
    if heap[left] == None and heap[right] == None:
        return False
    elif heap[left] == None:
        return right
    elif heap[right] == None:
        return left
    else:
        minimum_value = min(heap[left], heap[right])
        return heap.index(minimum_value)

def insert(heap, item):
    for i in range (len(heap)):
        if heap[i] == None:
            heap[i] = 12
            break
    heap.append(None)
    heap.append(None)
    while heap[i] > heap[i//2]:
        heap[i],heap[i//2] = heap[i//2],heap[i]
        i=i//2
    return

def balance(heap, v = 0):
    #print(v)
    #print(heap[v])
    if heap[v] == None:
        return heap
    heap = balance(heap, v * 2 + 1)
    heap = balance(heap, v * 2 + 2)

    if v*2+1 < (len(heap) - heap.count(None)):
        min = min_child(v, heap)
        print(v)
        print(heap)
        if heap[min] != None:
            if heap[min] < heap[v]:
                heap[min],heap[v] = heap[v],heap[min]
    return heap

def extract_min(heap):
    result = heap[0]
    minimum = heap[0]
    for i in range (len(heap)):
        if heap[i] == None:
            heap[0] = heap[i-1]
            heap.pop(i-1)
            break
    return result, balance(heap)

def heapsort(heap):
    sortedlist = []
    while(len(heap) - heap.count(None) > 0):
        foo = extract_min(heap)[0]
        sortedlist.append(foo)
    sortedlist.append(sortedlist[0])
    sortedlist.pop(0)
    return sortedlist
heap = [16,14,10,8,7,9,4,2,3,1,None,None,None,None,None,None,None,None,None,None,None]
print(heapsort(heap))