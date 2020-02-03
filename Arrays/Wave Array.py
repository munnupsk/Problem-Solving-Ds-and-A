#https://practice.geeksforgeeks.org/problems/wave-array/0

for _ in range(int(input())):
    n=int(input())
    li=list(input().split())
    for i in range(0,n-1,2):
        li[i],li[i+1]=li[i+1],li[i]
    for i in range(n):
        print(li[i],end=" ")
    print()
