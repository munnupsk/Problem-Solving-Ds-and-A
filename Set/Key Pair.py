#https://practice.geeksforgeeks.org/problems/key-pair/0


for _ in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    s=set()
    flag=1
    for i in range(n):
        temp=k-li[i]
        if temp in s:
            print("Yes")
            flag=0
            break
        s.add(li[i])
    if flag:
        print("No")
