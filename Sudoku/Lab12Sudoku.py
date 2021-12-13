import sys

def CheckRow(board):
    for i in board:
        checkNumber = []
        for j in i:
            checkNumber.append(j)
            print(checkNumber)
            if checkNumber.count(j)>1:
                return False
    return True


def CheckColumn(board):
    for i in range(0, 9):
        checkNumber = []
        for j in range(0, 9):
            checkNumber.append(board[j][i])
            print(checkNumber)
            if checkNumber.count(board[j][i]) > 1:
                return False
    return True

def Check3x3(board):
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            checkNumber = []
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    checkNumber.append(board[r][c])
                    if checkNumber.count(board[r][c])>1:
                        return False
    return True




sys.stdin = open('correct.txt')
#sys.stdin = open('incorrect.txt')
board=[]
for i in range(0,9):
    board.append(input())

control=CheckRow(board)
control2=CheckColumn(board)
control3=Check3x3(board)
print(control)
print(control2)
print(control3)
if (control==True and control2==True and control3==True):
    print("Valid Sudoku")
else:
    print("Invalid Sudoku")

