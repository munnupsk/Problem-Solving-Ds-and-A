
#https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array/0


def bs(li,l,r,key):
    if l>r:
        return -1
    mid=(l+r)//2
    if li[mid]==key:
        return mid
    
    if li[l]<=li[mid]:
        if key>=li[l] and key<=li[mid]:
            return bs(li,l,mid-1,key)
        return bs(li,mid+1,r,key)
    
    if key>=li[mid] and key<=li[r]:
        return bs(li,mid+1,r,key)
    return bs(li,l,mid-1,key)
    
for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    key=int(input())
    res=bs(li,0,n-1,key)
    print(res)
