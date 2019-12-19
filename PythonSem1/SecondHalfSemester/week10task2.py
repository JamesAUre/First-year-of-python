def count(T, v):
    counter = 1
    if T[v][0] is None and T[v][1] is None:
        return counter

    if T[v][0] is not None:
        counter += count(T, T[v][0])

    if T[v][1] is not None:
        counter += count(T, T[v][1])

    return counter


def balance(T, v):
    return count(T, T[v][0])-count(T, T[v][1])


binarytree = [(2, 1), (3, None), (5, 4), (None, None), (None, None), (None, None)]
print(balance(binarytree, 0))
