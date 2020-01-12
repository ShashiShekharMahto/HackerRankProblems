#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    for i in range(len(s)):
        b = s[i].isalnum()
        a=''
        if(b):
            a = s[i][0].isalpha()
        if(a):
            s[i] = s[i][0].upper() + s[i][1:]
    #print(s)
    return(" ".join(s))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
