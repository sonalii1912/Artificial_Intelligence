#N queen Problem
n = int(input("Enter no of Queens:"))
a = [[0 for x in range(n)] for y in range(n)]
b = {}

# To check in column
def isColumnSafe(r,c):
    while(r>=0):
        if (a[r][c]==1):
            return 0
        r=r-1
    return 1
# To check in left diagonal
def isLeftDiagonalSafe(r,c):
    while(r>=0 and c>=0):
        if(a[r][c]==1):
            return 0
        r=r-1
        c=c-1
    return 1
# To check in right diagonal
def isRightDiagonalSafe(r,c):
    while(r>=0 and c<n):
        if(a[r][c]==1):
            return 0
        r=r-1
        c=c+1
    return 1
# function to check given row and col position is safe or not.
def isSafe(row,col):
    if(isColumnSafe(row,col)== 0):
        return 0
    if(isLeftDiagonalSafe(row,col)==0):
        return 0
    if(isRightDiagonalSafe(row,col)==0):
        return 0
    return 1
# to check row wise safe position for each queen(n).
def checkBoard(r,c):
    if(r>=n):
        return
    p=0
    while(c<n):
        p = isSafe(r,c)
        if(p==1):
            a[r][c] = 1
            b.update({r:c})
            break
        c=c+1
    if(p==1):
        checkBoard(r+1,0)   # Calling recursion for next row
    else:
        a[r-1][b.get(r-1)]=0
        checkBoard(r-1,int(b.get(r-1))+1)   # Here actual backtracking happens for previous row

checkBoard(0,0)
for i in a:
    print(i)
    