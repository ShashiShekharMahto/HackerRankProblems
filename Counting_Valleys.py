import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    up = 0
    down = 0
    valleyseq = 0
    set = 0
    for i in range(n):
        if(up == 1 and down == 0):
            set  =1
            #print("set ",i,set)
        if(s[i] == 'U'):
            up +=1
        else:
            down +=1
        if(up == down):
            if(set == 1):
                up = 0
                down = 0
                set = 0
                #print("up ,down when set ",up,down)
            else:
                valleyseq += 1
                up = 0
                down = 0
                #print("up ,down when not set ",up,down)
    return(valleyseq) 

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
