def Noidea(ar, A, B):
    A.sort()
    B.sort()
    #print(ar)
    nA = len(A)
    count = 0
    l = 0
    h = nA-1
    #print("na ",nA,"l h ",l," ",h)
    for i in range(len(ar)):
        while(l<=h):
            #print("aA ",ar[i]," l h ",l," ",h)
            mid = (l+h)//2
            if(ar[i] == A[mid]):
                count += 1
                #print(" ca",count," ",ar[i])
                l=0
                h=nA-1
                break
            elif(ar[i] < A[mid]):
                h = mid-1
            else:
                l = mid+1
        l=0
        h = nA-1
    nB = len(B)
    l=0
    h = nB-1
    #print("nB ",nB,"l h ",l," ",h)
    for i in range(len(ar)):
        #print("aB ",ar[i]," l h ",l," ",h)
        while(l<=h):
            mid = (l+h)//2
            if(ar[i] == B[mid]):
                count -= 1
                #print("cb ",count," ",ar[i])
                l=0
                h=nB-1
                break
            elif(ar[i] < B[mid]):
                h = mid-1
            else:
                l = mid+1
        l=0
        h = nB-1
    return(count)
if __name__ == "__main__":
    nm = input().split(" ")
    n = int(nm[0])
    m = int(nm[1])
    ar = list(map(int, input().split(" ")))
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))
    result = Noidea(ar, A, B)
    print(result)
