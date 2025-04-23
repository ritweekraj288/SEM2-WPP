#A magic square is an N×N grid of numbers in which the entries in each row, column and main diagonal sum to the same number (equal to N(N^2+1)/2). Create a magic square for N=4, 5, 6, 7, 8

import numpy as np

def magicsquare(square,n):
    square[n/2][n-1]=1
    

n=int(input("enter the value of n:\t"))
sum=n*(((n**2)+1)/2)
square=np.zeros((n,n),dtye=int)
magicsquare(square,n)