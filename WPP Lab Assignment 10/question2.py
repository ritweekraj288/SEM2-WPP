#Write a program to place the queens randomly in the chess board so that all the conditions are satisfied. Find the solutions to the problem.# Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens according to the following constraints.
# a. Each row should have exactly only one queen.
# b. Each column should have exactly only one queen.
# c. No queens are attacking each other.

import numpy as np

def queen(board,row,n):
    if(row==n):
        print(board)
        return
    for i in range(n):
        if(issafe(board,row,i,n)):
            board[row][i]=1
            queen(board,row+1,n)
            board[row][i]=0

def issafe(board,row,col,n):
    #horizonally checking
    for i in range(n):
        if(board[row][i]==1):
            return False
    #vertically checking
    for i in range(n):
        if(board[i][col]==1):
            return False
    #diagonally checking
    r=row-1
    c=col-1
    while(r>=0 and c>=0):
        if(board[r][c])==1:
            return False
        r-=1
        c-=1
    r=row-1
    c=col+1
    while(r>=0 and c<n):
        if(board[r][c]==1):
            return False
        r-=1
        c+=1
    return True        

    
board=np.zeros((8,8),dtype=int)
print(board)
queen(board,0,8)