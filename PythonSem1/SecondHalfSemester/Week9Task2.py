def checksurroundings(M, point):
    directions = []
    for xdirection, ydirection in [[0,-1],[0,1],[-1,0],[-1,-1],[-1,1],[1,0],[1,1],[1,-1]]:
        movedirection = [0,0]
        if point[0] == 0 and xdirection == -1:
            continue
        if point[1] == 0 and ydirection == -1:
            continue
        if point[0] == len(M) and xdirection == 1:
            continue
        if point[1] == len(M) and ydirection == 1:
            continue

        movedirection[0] = point[0] + xdirection
        movedirection[1] = point[1] + ydirection

        if movedirection[0] < len(M) and movedirection[1] < len(M) and M[movedirection[0]][movedirection[1]] == 0:
            directions.append(movedirection)

    if directions == []:
        return False

    #print(directions)
    return directions

def all_paths(M, u, v, path):
    if u == v:
        print(path)
        return

    paths = checksurroundings(M, u)

    if paths != False :
        for i in range (len(paths)):
            M[u[0]][u[1]] = 1
            path.append(paths[i])
            u = paths[i]
            all_paths(M, u, v, path)

    return path.pop()

u = [0,0]
v = [3,3]

M =[[0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]]

path = []
all_paths(M, u, v, path)