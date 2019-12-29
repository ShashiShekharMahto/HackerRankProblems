#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    time ={1:"one",2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",8:"eight",\
    9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", \
    15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", \
    20:"twenty"}
    if(m == 00):
        return(time[h]+" o' clock")
    if(m>0):
        if(m==1):
            return("one minute past "+ time[h])
        if(m<=30):
            if(m == 15):
                return("quarter past "+time[h])
            if(m == 30):
                return("half past "+time[h])
            if(m>20):
                b = m-20
                return(time[20]+" "+time[b]+" minutes past "+time[h])
            if(m<=20):
                return(time[m]+ " minutes past "+time[h])
        if(m>30):
            m = 60-m
            if(m==1):
                return(time[m]+ " minute to "+time[h+1])
            if(m == 15):
                return("quarter to "+time[h+1])
            if(m>20):
                b = m-20
                return(time[20]+" "+time[b]+" minutes to "+time[h+1])
            if(m<=20):
                return(time[m]+ " minutes to "+time[h+1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
