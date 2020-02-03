#https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum/0

for _ in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    hash={}
    count=0
    for i in range(n):
        if li[i] in hash:
            hash[li[i]]+=1
        else:
            hash[li[i]]=1
    for i in range(n):
        if k-li[i] in hash:
            count+=hash[k-li[i]]
        
        if k-li[i]==li[i]:
            count-=1
    print(count//2)
            
    
