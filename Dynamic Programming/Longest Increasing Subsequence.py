


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [0]*(n)
    dp[0] = 1
    for i in range(1,n):
        f=0
        for j in range(i):
            if arr[i]>arr[j]:
                f=1
                dp[i] = max(dp[i],dp[j])
        if f:
            dp[i]+=1
        else:
            dp[i]=1
    print(max(dp))
