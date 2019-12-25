#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    sum = 0
    a =[]
    b =[]
    for i in range(len(container)):
        for j in range(len(container)):
            sum = sum + container[i][j]
        a.append(sum)
        sum = 0
    sum = 0
    for i in range(len(container)):
        for j in range(len(container)):
            sum = sum + container[j][i]
        b.append(sum)
        sum = 0
    sum = 0
    return('Impossible') if((max(a)>max(b)) or (max(a)<max(b))) else 'Possible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
