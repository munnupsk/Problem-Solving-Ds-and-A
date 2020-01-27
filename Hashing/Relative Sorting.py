#https://practice.geeksforgeeks.org/problems/relative-sorting/0/?track=md-hashing&batchId=144

for _ in range(int(input())):
    n1,n2=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    hash={}
    
    for i in l1:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    
    for j in l2:
        if j in hash and hash[j]>=1:
            print((str(j)+" ")*hash[j],end="")
        del hash[j]
        
    if len(hash)>0:
        ls=sorted(list(hash.keys()))
    for l in ls:
        print((str(l)+" ")*hash[l],end="")
    print()
