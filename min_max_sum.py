#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort(reverse = True)
    n = len(arr)
    s = 0
    t = 0
    for i in range(n-1):
        s = s + arr[i]
    for i in range(1,n):
        t = t+ arr[i]
    print(t,s) 
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
