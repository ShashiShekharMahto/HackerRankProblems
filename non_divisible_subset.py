#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    s = list(dict.fromkeys(s))
    s = list(i%k for i in s)
    a = [s.count(i) for i in range(k)]
    print(a)
    count = 0
    l = 1
    r = len(a)-1
    while(l<=r):
        if(l == r):
            count +=1
        else:
            count = count + max(a[l],a[r])
        l += 1
        r -= 1
    if(a[0] != 0):
        return(count + 1)
    else:
        return(count)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
