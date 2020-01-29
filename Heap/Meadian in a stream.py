#code
#https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0/?track=md-heap&batchId=144
# consider the example 5,7,1,6,3,8,9
import heapq
import math
t=int(input())
mh=[]
maxh=[]
root=0
while t:
   # flag=1
    e=int(input())
    if len(maxh)>len(mh):
        if e<root:
            #we are using -ve sign logically to build max heap using heap which is used for min heap
            heapq.heappush(mh,-1*heapq.heappop(maxh))
            
            heapq.heappush(maxh,-1*e)
            root=math.floor((-1*maxh[0]+mh[0])/2)
            print(root)
            
        else:
            heapq.heappush(mh,e)
            root=math.floor((-1*maxh[0]+mh[0])/2)
            print(root)
        
            
            
        
        
    elif len(mh)==len(maxh):
        if e<root:
            heapq.heappush(maxh,-1*e)
            root=-1*maxh[0]
            print(root)
        
        else:
            heapq.heappush(mh,e)
            root=mh[0]
            print(root)
        
    
    else:
        if e>root:
            heapq.heappush(maxh,-1*heapq.heappop(mh))
            
            heapq.heappush(mh,e)
            root=math.floor((-1*maxh[0]+mh[0])/2)
            print(root)
            
        else:
            heapq.heappush(maxh,-1*e)
            root=math.floor((-1*maxh[0]+mh[0])/2)
            print(root)
        
    
        
    t-=1    
        
