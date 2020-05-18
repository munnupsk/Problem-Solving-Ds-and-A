



for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().strip().split(" ")))
    costs = [[0 for i in range(n)] for j in range(n)]
    
    k = 0
    for i in range(n):
        for j in range(n):
            costs[i][j] = nums[k]
            k += 1
            
    res.append(BFS(costs, n))
