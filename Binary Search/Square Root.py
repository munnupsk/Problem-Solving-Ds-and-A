#https://practice.geeksforgeeks.org/problems/square-root/1


def floorSqrt(x): 
    #Your code here
    low=0
    high=x
    while low<=high:
        mid=(low+high)//2
        if mid*mid==x:
            return mid
            
        # Since we need floor, we update  
        # answer when mid*mid is smaller 
        # than x, and move closer to sqrt(x) 
        if mid*mid<x:
            low=mid+1
            ans =mid
        else:
            high=mid-1
    return ans
            
