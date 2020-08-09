def traversal(m, n):
    i = 0 #upper row
    j = n-1 #right column
    k = n-1 #down row
    l = 0 #left column
    
    while(i <= k): #till upper row less than the down row
        for p in range(i, j+1):  #upper row
            print(m[i][p], end=" ")
        i += 1
        
        for q in range(i, k+1): #right column
            print(m[q][k], end=" ")
        j -= 1
        
        for r in range(j, l-1, -1): #lower row
            print(m[k][r], end=" ")
        k -= 1
        
        for s in range(k, i-1, -1): # left column
            print(m[s][l], end=" ")
        l +=1
    print()

t=int(input())
for _ in range(t):
    n=int(input())
    m=[]
    for i in range(n):
        a=list(map(int,input().split()))
        m.append(a)
    traversal(m,n)
