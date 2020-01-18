#https://practice.geeksforgeeks.org/problems/prime-number/0

import math
for _ in range(int(input())):
    n= int(input())
    f=1
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            print("No")
            f=0
            break
    if f:
        print("Yes")
