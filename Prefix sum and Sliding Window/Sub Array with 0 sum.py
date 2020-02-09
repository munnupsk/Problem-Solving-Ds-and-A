
#https://practice.geeksforgeeks.org/problems/subarray-with-0-sum/0

def find(li,n):
    s=set()
    sum=0
    for i,num in enumerate(li):
        sum+=num
        if sum==0 or sum in s:
            return True
        s.add(sum)
    return False


for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    res=find(li,n)
    if res:
        print("Yes")
    else:
        print("No")
