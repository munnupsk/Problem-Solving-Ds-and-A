
#https://practice.geeksforgeeks.org/problems/next-larger-element/0

for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    arr=[0]*n
    s=list()
    for i in range(n-1,-1,-1):
        while len(s)>0 and s[-1]<=li[i]:
            s.pop()
        
        
        # if stack gots empty means there  
        # is no element on right which is  
        # greater than the current element. 
        # if not empty then the next greater  
        # element is on top of stack 
        if len(s)==0:
            arr[i]=-1
        else:
            arr[i]=s[-1]
        s.append(li[i])
        
    for i in range(n):
        print(arr[i],end=" ")
    print()
    
