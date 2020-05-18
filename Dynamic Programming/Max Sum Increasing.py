


for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    s=[0 for i in range(n)]
    max=0
    for i in range(n):
        s[i]=li[i]
        
        
    for i in range(1,n):
        for j in range(i):
            if li[i]>li[j] and s[i]<s[j]+li[i]:
                s[i]=s[j]+li[i]
                
    for i in range(n):
        if s[i]>max:
            max=s[i]
            
    print(max)
            
