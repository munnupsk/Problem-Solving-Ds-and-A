



def get_ans(str_list, q):
    n = len(q)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(n):
        for j in range(i,n):
            if dp[i] and q[i:j+1] in str_list:
                dp[j+1] = True
    
    if dp[-1]: return 1
    else: return 0   

cases = int(input())
for _ in range(cases):
    n = int(input())
    str_list = input().split()
    q = input()
    print(get_ans(str_list, q))
