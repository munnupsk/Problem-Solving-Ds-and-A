#https://practice.geeksforgeeks.org/problems/count-distinct-pairs-with-difference-k/0

for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    k=int(input())
    
    count=0
    li.sort()
    hash={}
    for i in range(n):
        if li[i] in hash:
            hash[li[i]]+=1
        else:
            hash[li[i]]=1
    if k==0:
        for i in range(n):
            if hash[li[i]]>1:
                count+=1
                hash[li[i]]=0
    else:
        for i in range(n):
            temp=abs(k-li[i])
            if temp in hash:
                count+=1
                del hash[li[i]]
    print(count)
