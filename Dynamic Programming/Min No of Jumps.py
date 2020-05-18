


def minNum(li,n):
    if n==0 or len(li)==0 or li[0]==0:
        return -1
     
        
    jumps=[0 for i in range(n)]
    jumps[0]=0
    for i in range(1,n):
        jumps[i]=float('inf')
        for j in range(i):
            if i<=j+li[j] and jumps[j] != float('inf'):
                jumps[i] = min(jumps[i], jumps[j] + 1) 
                break
    return jumps[n-1] 
    
        

for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    res=minNum(li,n)
    if res==float('inf'):
        print(-1)
    else:
        print(res)
