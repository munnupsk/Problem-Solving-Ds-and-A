#https://practice.geeksforgeeks.org/problems/pair-with-given-sum-in-a-sorted-array/0

def pairsum(li,k,n):
    a=set()
    s=[]
    for i in range(n):
        temp=k-li[i]
        if temp>=0 and  temp in a:
            s.append((temp,li[i]))
        a.add(li[i])
        
    return sorted(s)


for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    k=int(input())
    res=pairsum(li,k,n)
    if len(res)==0:
        print('-1')
    else:
        for i in range(len(res)):
            print(res[i][0],res[i][1],k)
