
#https://practice.geeksforgeeks.org/problems/find-transition-point/1


def transitionPoint(arr, n):
    #Code here
    left=0
    high=n-1
    while left<=high:
        mid=(left+high)//2
        if arr[mid]==0:
            left=mid+1
        elif arr[mid]==1:
            if arr[mid-1]==0:
                return mid
            else:
                high=mid-1
    return -1
    
