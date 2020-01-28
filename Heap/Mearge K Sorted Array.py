#https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1/?track=md-heap&batchId=144

import heapq
def mergeKArrays(a,n):
    '''
    :param a: given array
    :param n: size of row and column
    :return: merged sorted list
    '''
    q=[]
    m=len(a[0])
    if m==0:
        return []
    for i in range(n):
        heapq.heappush(q,(a[i][0],i,0))
    ans=[]
    while len(q)>0:
        top=heapq.heappop(q)
        ans.append(top[0])
        if top[2]==m-1:
            continue
        x,y=top[1],top[2]+1
        heapq.heappush(q,(a[x][y],x,y))
    return ans
        
        
