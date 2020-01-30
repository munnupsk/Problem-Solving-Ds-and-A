#https://practice.geeksforgeeks.org/problems/kth-smallest-element/0/?track=md-arrays&batchId=144

import heapq
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    heapq.heapify(arr)
    print(heapq.nsmallest(k,arr)[-1])
