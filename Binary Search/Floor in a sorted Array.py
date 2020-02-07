
#https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array/0

def bs(li,left,high,k):
    if left>high:
        return -1
    if k>li[high]:
        return high
    mid =(left+high)//2
    if li[mid]==k:
        return mid
    if mid >0 and li[mid-1]<k and k<li[mid]:
        return mid-1
    
    if k<li[mid]:
        return bs(li,left,mid-1,k)
    return bs(li,mid+1,high,k)

for _ in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    res=bs(li,0,n-1,k)
    print(res)
    
