#https://practice.geeksforgeeks.org/problems/missing-number-in-array/0/?track=md-arrays&batchId=144


# A^A=0

for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    x1=li[0]
    x2=1
    for i in range(1,n-1):
        x1^=li[i]
    for i in range(2,n+1):
        x2^=i
    ans=x2^x1
    print(ans)
        
