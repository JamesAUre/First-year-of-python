INF = 2147483647
def justifier(wordlist, width):
    """
    This function finds the most balanced use of space between each line of the list of characters.
    worst time complexity: O(N*M)
    best time complexity: O(N*M)
    :param wordlist: the list of words being used for the lines
    :param width: the maximum amount of characters per line
    :return: a list where each element represents a line
    """
    wl = [len(word) for word in wordlist]

    n = len(wordlist)

    table = [[0 for i in range(len(wordlist))] for j in range(len(wordlist))]
    lc = [[0 for i in range(len(wordlist))] for j in range(len(wordlist))]
    c = [0 for i in range(len(wordlist))]
    length = 0
    lines = []
    mincost = []

    for i in range(len(table)):

        # loops across each column
        for j in range(i, len(table[i])):
            if width - (len(wordlist[j])+length) >= 0:
                table[i][j] = (width - (len(wordlist[j])+length))**3
                length += len(wordlist[j])+1
            else:
                table[i][j] = 999999999

        length = 0

    wordlen = len(wordlist)

    #for i in range(len(table), -1, -1):
     #   j = i
     #   if table[i][j] == INF:
     #       j-=1

     #   elif j == len(table) and table[i][j] >= 0:
     #       lc[i][j] = 0

     #   else:
     #       lc[i][j] = table[i][j]*table[i][j]

    #c[0] = 0
    #for j in range(1, n+1):

    return table

def printSolution(p, n):
    k = 0
    if p[n] == 1:
        k = 1
    else:
        k = printSolution(p, p[n] - 1) + 1
    print('Line number ', k, ': From word no. ',
                                 p[n], 'to ', n)
    return k

list_of_words = ['you', 'can', 'use', 'dynamic', 'programming', 'to', 'justify', 'text', 'and', 'I', 'learned','that',
                 'in', 'FIT1008']

list2 = ['Tushar', 'Roy', 'likes','to','code']

words = ["my name is james and",
        "i live in",
         "bangkok, this should adjust",
         "according to the width"]
width = 10

print (justifier(list2, 10))