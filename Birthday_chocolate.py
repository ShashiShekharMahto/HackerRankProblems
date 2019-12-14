#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    sum = 0
    for i in range(len(s)):
        if(m+i <= len(s)):
            for j in range(i,m+i):
                sum = sum + s[j]           
        if(sum ==d):
            count += 1
            sum = 0
        else:
            sum = 0
    return(count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
