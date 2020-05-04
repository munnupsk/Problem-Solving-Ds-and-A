
#https://practice.geeksforgeeks.org/problems/find-whether-path-exist/0


import numpy as np
for test in range(int(input())):
    n=int(input())
    arr= np.array( list(map(int,input().split())) ).reshape(n,n)
    queue=[]
    src=np.where(arr==1)
    queue.append([src[0][0],src[1][0]])
    found=False
    while(queue):
        #popping cordinates as (p,q) and updating queue after removing first value 
        p,q=queue[0]    
        queue=queue[1:]
        if p-1>=0 and arr[p-1][q]==2:
            found=True
            break            
        if q-1>=0 and arr[p][q-1]==2:
            found=True
            break            
        if p+1<n and arr[p+1][q]==2:
            found=True
            break            
        if q+1<n and arr[p][q+1]==2:
            found=True
            break
        #----------------------#
        if p-1>=0 and arr[p-1][q]==3:
            arr[p-1][q]=0
            queue.append([p-1,q])
        if q-1>=0 and arr[p][q-1]==3:
            arr[p][q-1]=0
            queue.append([p,q-1])
        if p+1<n and arr[p+1][q]==3:
            arr[p+1][q]=0
            queue.append([p+1,q])
        if q+1<n and arr[p][q+1]==3:
            arr[p][q+1]=0
            queue.append([p,q+1])
            
            
    if found:
        print(1)
    else:
        print(0)
