



for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    dep=list(map(int,input().split()))
    res=1
    platform_needed=1
    i=1
    j=0
    while i<n and j<n:
        
        if arr[i]<dep[j]:
            platform_needed+=1
            i+=1
            if platform_needed>res:
                res=platform_needed
        else:
            platform_needed-=1
            j+=1
    print(res)
