
#https://practice.geeksforgeeks.org/problems/kth-largest-element-in-a-stream/0/?track=md-heap&batchId=144

import heapq
for i in range(int(input())):

    a,b=list(map(int,input().split()))
    
    l=list(map(int,input().split()))
    
    k=[]
    
    for j in range(a):
    
        heapq.heappush(k,l[j])
    
    for j in range(a-1):
    
        print(-1,end=" ")
    print(k[0],end=" ")
    for j in range(a,b):
        s=k[0]
        if l[j]>s:
            heapq.heappop(k)
            heapq.heappush(k,l[j])
        print(k[0],end=" ")
    print()
