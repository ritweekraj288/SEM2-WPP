# # Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens according to the following constraints.
# # a. Each row should have exactly only one queen.
# # b. Each column should have exactly only one queen.
# # c. No queens are attacking each other.

# import numpy as np

# def queen(board,row,n):
#     if(row==n):
#         print(board)
#         return
#     for i in range(n):
#         if(issafe(board,row,i,n)):
#             board[row][i]=1
#             queen(board,row+1,n)
#             board[row][i]=0

# def issafe(board,row,col,n):
#     #horizonally checking
#     for i in range(n):
#         if(board[row][i]==1):
#             return False
#     #vertically checking
#     for i in range(n):
#         if(board[i][col]==1):
#             return False
#     #diagonally checking
#     r=row-1
#     c=col-1
#     while(r>=0 and c>=0):
#         if(board[r][c])==1:
#             return False
#         r-=1
#         c-=1
#     r=row-1
#     c=col+1
#     while(r>=0 and c<n):
#         if(board[r][c]==1):
#             return False
#         r-=1
#         c+=1
#     return True        

    
# board=np.zeros((8,8),dtype=int)
# print(board)
# queen(board,0,8)

# Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens
# according to the following constraints.
# a. Each row should have exactly only one queen.
# b. Each column should have exactly only one queen.
# c. No queens are attacking each other.

import numpy as np

def is_valid(board, row, col, n):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_queen(board, col, n):
    if col == n:
        return True

    for row in range(n):
        if is_valid(board, row, col, n):
            board[col] = row
            if solve_queen(board, col + 1, n):
                return True
            board[col] = -1
    return False

def print_board(board, n):
    board_array = np.full((n, n), '.', dtype=str)
    for col in range(n):
        board_array[board[col], col] = 'Q'
    for row in board_array:
        print(' '.join(row))

def solve_n_queens(n):
    board = np.full(n, -1)
    if solve_queen(board, 0, n):
        print_board(board, n)
    else:
        print('No solution found')

n = int(input("Enter the number of queens you want to place "))
solve_n_queens(n)