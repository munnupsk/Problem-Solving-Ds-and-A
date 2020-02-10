
#https://practice.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array/0

def bs(li,low,high):
    if low>high:
        return -1
    if low==high:
        return li[low]
    
    mid=(low+high)//2
    
    if mid%2==0:
        if li[mid]==li[mid+1]:
            return bs(li,low+2,high)
        else:
            return bs(li,low,mid)
    else:
        if li[mid]==li[mid-1]:
            return bs(li,mid+1,high)
        else:
            return bs(li,low,mid-1)
    
for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    
    res=bs(li,0,n-1)
    print(res)
