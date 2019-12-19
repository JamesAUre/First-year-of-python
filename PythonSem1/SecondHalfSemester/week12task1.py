def is_clique(S, k, G):
    for i in S:
        print(G[i][S])
        if G[i][S] != 1:
            return False
    return True

graph = [[0, 1, 0, 0, 0, 0, 0],[1, 0, 1, 1, 0, 0, 0],[0, 1, 0, 1, 1, 1, 0],[0,1,1,0,1,1,0],[0,0,1,1,0,1,1],
        [0,0,1,1,1,1,1],[0,0,0,0,1,1,0]]

is_clique([2,3,4,5],4,graph)