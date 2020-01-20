#https://practice.geeksforgeeks.org/problems/find-prime-numbers-in-a-range/0

import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    
    for i in range(a,b+1):
        if i==0 or i==1:
            continue
        flag=0
        for j in range(2,int(math.sqrt(i))+1):
            if i %j==0:
                flag=1
                break
        if flag==0:
            print(i,end=" ")
    print()
