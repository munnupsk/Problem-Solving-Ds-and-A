
#https://practice.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1

# ex : 2 2 4 5 6 3 2 
# find min distance b/w 2 and 3 or 3 and 2

import sys
def minDist(arr, n, x, y):
    # Code here
    if x not in arr or y not in arr:
        return -1
    min_dis=sys.maxsize
    for i in range(n):
        if x==arr[i] or y==arr[i]:
            prev=i
            break
    while i<n:
        if arr[i]==x or arr[i]==y:
            if arr[prev]!=arr[i] and (i-prev)<min_dis:
                min_dis=i-prev
                prev=i
            else:
                prev=i
        i+=1
    return min_dis
    
    
