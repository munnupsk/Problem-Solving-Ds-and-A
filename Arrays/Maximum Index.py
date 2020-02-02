#https://practice.geeksforgeeks.org/problems/maximum-index/0


for _ in range(int(input())):
    n=int(input())
    max_Diff=0;
    li=list(map(int,input().split()))
    L_min=[0]*n
    R_max=[0]*n
    
    L_min[0]=li[0]
    for i in range(1,n):
        L_min[i]=min(li[i],L_min[i-1])
    R_max[n-1]=li[-1]
    for i in range(n-2,-1,-1):
        R_max[i]=max(li[i],R_max[i+1])
    
    i,j=0,0
    maxDiff=0
    while j<n and i<n:
        if L_min[i]<=R_max[j]:
            maxDiff = max(maxDiff, j - i)
            j+=1
        else:
            i+=1
    print(maxDiff)
        
