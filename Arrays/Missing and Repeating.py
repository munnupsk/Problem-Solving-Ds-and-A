#https://practice.geeksforgeeks.org/problems/find-missing-and-repeating/0

for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    s=(n*(n+1))//2
    s_sq=(n*(n+1)*(2*n+1))//6
    
    for i in range(n):
        s-=li[i]
        s_sq-=li[i]*li[i]
    missing=(s+(s_sq//s))//2
    repeating=missing-s
    print("{} {}".format(repeating,missing))
