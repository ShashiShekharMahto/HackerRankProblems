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
    a = 0
    b = 0
    l = len(arr)
    for i in range(len(arr)):
        a = a + arr[i][i]
        b = b + arr[i][l-1-i]
    if(a>b):
        return(a-b)
    if(b>a):
        return(b-a)
    if(a==b):
        return(a-b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
