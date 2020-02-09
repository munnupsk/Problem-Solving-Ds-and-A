
#https://practice.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1

from collections import defaultdict 
def countDistinct(arr, n, k):
    # Code here
    hash=defaultdict(lambda:0)
    count=0
    for i in range(k):
        if hash[arr[i]]==0:
            count+=1
        hash[arr[i]]+=1
    print(count,end=" ")
    for i in range(k,n):
        if hash[arr[i-k]]==1:
            count-=1
        hash[arr[i-k]]-=1
        
        if hash[arr[i]]==0:
            count+=1
        hash[arr[i]]+=1
        print(count,end=" ")
    print()
