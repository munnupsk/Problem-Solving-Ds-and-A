
#https://practice.geeksforgeeks.org/problems/largest-fibonacci-subsequence/0

for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    m=max(li)
    hash=[]
    a=0
    b=1
    hash.append(0)
    hash.append(1)
    while b<m:
        c=a+b
        a=b
        b=c
        hash.append(b)
    for i in range(n):
        if li[i] in hash:
            print(li[i],end=" ")
    print()
