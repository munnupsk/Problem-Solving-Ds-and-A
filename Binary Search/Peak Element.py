
#https://practice.geeksforgeeks.org/problems/peak-element/1

def peakElement(arr, n):
    # Code here
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        
        if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
            return mid
        if arr[mid-1]>arr[mid]:
            r=mid-1
        else:
            l=mid+1
    return -1
        
        
