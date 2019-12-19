import random
def playerchoice(turn):
    count = 0
    if turn == 2:
        turn = -1
    while(count < 9):
        userchoicex = int(input("Enter x coordinate of choice: ")) - 1
        userchoicey = int(input("Enter y coordinate of choice: ")) - 1

        if(turn == 1):
            board[userchoicex][userchoicey] = 'X'
        elif(turn == -1):
            board[userchoicex][userchoicey] = 'O'
        turn = turn * -1
        if winnercheck() == False:
            print (board[0])
            print (board[1])
            print (board[2])

        else: return

def winnercheck():
    totalrow = 0
    totalcolumn = 0
    for i in range(0, 3):
        totalrow = 0
        totalcolumn = 0
        diagonals = 0
        for j in range(0, 3):

            #row check
            if board[i][j] == 'X':
                totalrow += 1
            if board[i][j] == 'O':
                totalrow -= 1

            #column check
            if board[j][i] == 'X':
                totalcolumn += 1
            if board[j][i] == 'O':
                totalcolumn -= 1

            #diagonal check


        if totalrow == 3 or totalcolumn == 3:
            print("you win!")
            return True
        if totalrow == -3 or totalcolumn == -3:
            print("you lose!")
            return True

    return False

board = []
#empty board set
for i in range(0,):
    board.append([])
    for j in range(0,3):
        board[i].append(' ')


print (board[0])
print (board[1])
print (board[2])

turn = int(input("Which player would like to start? (1 or 2): "))
playerchoice(turn)