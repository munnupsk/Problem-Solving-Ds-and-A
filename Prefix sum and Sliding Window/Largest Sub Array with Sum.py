
#https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k/0


def ls(li,n,k):
    hash={}
    sum=0
    max_len=0
    for i in range(n):
        sum+=li[i]
        if sum==k:
            max_len=i+1
        
        if sum-k in hash:
            max_len=max(max_len,i-hash[sum-k])
        if sum not in hash:
            hash[sum]=i
    return max_len

for _ in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    res=ls(li,n,k)
    print(res)
