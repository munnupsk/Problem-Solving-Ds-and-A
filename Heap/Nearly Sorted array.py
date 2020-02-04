
#https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0

from heapq import heappop, heappush, heapify 

for _ in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    heap=li[:k+1]
    heapify(heap)
    temp_index=0
    for i in range(k+1,n):
        li[temp_index]=heappop(heap)
        heappush(heap,li[i])
        temp_index+=1
    while heap:
        li[temp_index]=heappop(heap)
        temp_index+=1
    
    
    for i in range(n):
        print(li[i],end=" ")
    print()
    
