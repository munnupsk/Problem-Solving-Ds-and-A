



cases = int(input())

for _ in range(cases):
    m = int(input())
    s = list(map(int, input().split()))
    n = int(input())
    memo = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        memo[i][0] = 1

    for i in range(1,m+1):
        for j in range(1,n+1):
            memo[i][j] += memo[i-1][j]
            if(s[i-1]<=j):
                memo[i][j] += memo[i][j-(s[i-1])]
    print(memo[m][n])
