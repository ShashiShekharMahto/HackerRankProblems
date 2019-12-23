#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack functi  on below.
def queensAttack(n, k, r_q, c_q, obstacles):

    #number of cells in the given direction
    right = n-c_q
    left = c_q - 1
    up = r_q - 1
    down = n - r_q
    upper_left = left if left<up else up
    upper_right = right if right<up else up
    down_left = left if left<down else down
    down_right = right if right<down else down

    #check up condition comment why we have used all this variable
    u = 0 
    r = 0
    l = 0
    u = 0
    d = 0
    ul = 0
    ur = 0
    dl = 0
    dr = 0

    #count the number of attacks
    for i in range(len(obstacles)):
        a = obstacles[i][0]
        b = obstacles[i][1]
        c = r_q - a 
        d = c_q - b

        #up
        if(c>0 and d == 0):
            if(u == 0):
                u = c-1
                up = c -1
                #print("u",up)
            elif(u>c-1): #if we already calculated the value for up but if a obstacle is present below the obstacle from the before we have taken for calculation and also if obstacle is present in the same cell which already calculated(for ex: n=5,queen =(5,3) first obstacle co-ordinates is (1,3) so here queen can attack till (2,3) so,number of attack in up direction =3. again an obstacle at (3,3) then queen can attack till (4,3),now number of attack in up direction =1. thats why 'elif' condition.) 
                u = c-1
                up = c-1

        #down
        elif(c<0 and d == 0):
            if(d == 0):
                d = abs(c+1)
                down = abs(c+1)
                #print("d",down)
            elif(d>abs(c+1)):
                d = abs(c+1)
                down = abs(c+1)
        
        #left
        elif(c == 0 and d>0):
            if(l == 0):
                l = d-1
                left = d - 1
                #print("l",left)
            elif(l>d-1):
                l = d-1
                left = d-1
        
        #right
        elif(c == 0 and d<0):
            if(r == 0):
                r = abs(d+1)
                right = abs(d+1)
                #print("r",right)
            elif(r>abs(d+1)):
                r = abs(d+1)
                right = abs(d+1)
        
        #upper_left
        elif(c>0 and d>0 and c==d):
            if(ul == 0):
                ul = c-1
                upper_left = c-1
                #print("ul",upper_left)
            elif(ul>c-1):
                ul = c-1
                upper_left = c-1
        
        #down_right
        elif(c<0 and d<0 and c==d):
            if(dr == 0):
                dr = abs(c+1)
                down_right = abs(c+1)
                #print("dr",down_right)
            elif(dr>abs(c+1)):
                dr = abs(c+1)
                down_right = abs(c+1)
                #print("dr",down_right)
        
        #upper_right
        elif(c>0 and d<0 and (c+d) == 0):
            if(ur == 0):
                ur = c-1
                upper_right = c-1
                #print("ur",upper_right)
            elif(ur>c-1):
                ur = c-1
                upper_right = c-1
        
        #down_left
        elif(c<0 and d>0 and (c+d)==0):
            if(dl == 0):
                dl = d-1
                down_left = d-1
                #print("dl",down_left)
            elif(dl>d-1):
                dl = d-1
                down_left = d-1
    return(up + down + left + right + upper_left + upper_right + down_left + down_right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
