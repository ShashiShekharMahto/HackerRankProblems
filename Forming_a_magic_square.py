#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    a = [[[8,1,6],[3,5,7],[4,9,2]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,7,6],[9,5,1],[4,3,8]],
        [[6,1,8],[7,5,3],[2,9,4]]]
    p = 46
    q = 0
    k = 0
    while(k<8):
        for i in range(len(s)):
            for j in range(len(s)):
                q = q + (abs(s[i][j]-a[k][i][j]))
        if(q<p):
            p = q
        print(q)
        q = 0
        k +=1
    return(p)        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
