
#https://practice.geeksforgeeks.org/problems/equilibrium-point/0

def Equillibrium(li,n):
    total_sum=sum(li)
    left_sum=0
    for i,num in enumerate(li):
        total_sum-=num
        if left_sum==total_sum:
            return i+1
        left_sum+=num
    return -1

for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    res=Equillibrium(li,n)
    print(res)
            
