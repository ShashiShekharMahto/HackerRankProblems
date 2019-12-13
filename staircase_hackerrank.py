#1st approach
import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        for j in range(n-(i+1)):
            print(" ",end='')
        for k in range(i+1):
            print("#",end='')
        print()
if __name__ == '__main__':
    n = int(input())

    staircase(n)
    
#2nd approach

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        print(" " * (n-i-1) + "#" * (i+1))
if __name__ == '__main__':
    n = int(input())

    staircase(n)
