queens = [2,1,3,0]

def lastQueenOk(queens, lastqueen):
    print(queens)
    print(lastqueen)
    for i in range (lastqueen):
        if queens[i] == queens[lastqueen]:
            print('t')
            return False

        if abs(queens[i] - i+1) == abs(queens[lastqueen] - lastqueen+1):
            print(queens[i] - i+1)
            print(queens[lastqueen] - lastqueen+1)
            print('t2')
            return False
    return True

def solution(queens):
    for i in range (1, len(queens)):
        if lastQueenOk(queens, i) == False:
            return False
    return True
print(solution(queens))