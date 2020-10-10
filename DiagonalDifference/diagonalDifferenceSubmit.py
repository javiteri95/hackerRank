#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    firstDiag = 0
    secondDiag = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                firstDiag+= arr[i][j]
            if (len(arr) - i) == j + 1:
                secondDiag += arr[i][j]
    
    return abs(firstDiag - secondDiag)
    # Write your code here
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
