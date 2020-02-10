#https://practice.geeksforgeeks.org/problems/the-nth-fibonnaci/0


def nthfib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a=0
        b=1
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return c%10
    
for _ in range(int(input())):
    n=int(input())
    res=nthfib(n)
    
    print(res)
        
