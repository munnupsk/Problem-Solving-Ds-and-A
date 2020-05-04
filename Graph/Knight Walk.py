


from collections import deque
def safe(i,j,row,col):
    if i>=1 and j>=1 and i<=row and j<=col:
        return True
    return False
    
def bfs(row,col,s1,s2,d1,d2):
    visited=set()
    que=deque()
    que.append((s1,s2,0))
    visited.add((s1,s2))
    while que:
        i,j,depth=que.popleft()
        if i==d1 and j==d2:
            return depth
        for x,y in [(2,1),(2,-1),(-2,1),(-2,-1), (1,2),(-1,2),(1,-2),(-1,-2)]:
            curr_x,curr_y=i+x,j+y
            if safe(curr_x,curr_y,row,col) and (curr_x,curr_y) not in visited:
                visited.add((curr_x,curr_y))
                que.append((curr_x,curr_y,depth+1))
    return -1


for _ in range(int(input())):
    row,col=map(int,input().split())
    s1,s2,d1,d2=list(map(int,input().split()))
    print(bfs(row,col,s1,s2,d1,d2))
