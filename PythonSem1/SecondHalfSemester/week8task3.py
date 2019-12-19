def simplerecursivebinarysearch(alist, target, lo, hi):
    if alist[lo] == target:
        return lo
    if lo == hi:
        return False
    return simplerecursivebinarysearch(alist,target, lo+1, hi)

list = ['a','b','c','d','james','australia','test','ok','winna','yeet']
numba = 'Amir'
lo = 0
hi = len(list) - 1
print(simplerecursivebinarysearch(list, numba, lo, hi))