#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

for i in range(int(input())):
    n,s=map(int,input().split())
    li=list(map(int,input().split()))
    l,r=0,0
    sum=0
    flag=1
    while r<n:
        sum+=li[r]
        while sum>s:
            sum-=li[l]
            l+=1
        if sum==s:
            print("{} {}".format(l+1,r+1))
            flag=0
            break
        
        
            
        r+=1
    if flag:
        print(-1)
            
