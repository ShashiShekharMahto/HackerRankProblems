"""
n = 3
    *
   * * 
    *
n=5
    *
   * *
  *   *
   * *
    *
"""


t = int(input())
for i in range(t):
    n = int(input())
    print(" " *(n//2) + "*" ) #first line for one "*"
    for i in range(1,(n//2 + 1)):  #till middle line
        print(" " *(n//2 -i) + "*" + " " * (2*i - 1) + "*" )
    for i in range(1,(n//2)): # till "middle+1" to "last-1" line
        print(" " * (i) + "*" + " " * ((n-2)- 2*i )+ "*") 
    print(" " *(n//2) + "*")  #last line
