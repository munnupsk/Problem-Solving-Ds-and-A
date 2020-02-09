#https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k/0

for _ in range(int(input())):
    n,k=map(int,input().split())
    
    li=list(map(int,input().split()))
    
    maxi=0
    
    
    for i in range(k):
        
        maxi+=li[i]
    sum=maxi   
    for i in range(k,n):
        val=li[i-k]
        sum=sum-val+li[i]
        maxi=max(maxi,sum)
    print(maxi)
    
    
    
