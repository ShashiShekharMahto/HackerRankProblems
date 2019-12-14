#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    n = len(s)
    if(s[8]=='a' or s[8]=='A'):
        a = int(s[0:2])
        if(a == 12):
            a = a+12
            p = str(a)
            if(a == 24):
                p = '00'
            b = s[2:n-2]
            c = p+b 
            return(c)   
        return(s[:n-2])
    else:
        a = int(s[0:2])
        if(a !=12):
            a = a+12
        p = str(a)
        b = s[2:n-2]
        c = p+b 
        return(c)     

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
