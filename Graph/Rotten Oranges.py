


from collections import deque
def fill(mat,r,c):
    que=deque()
    #enqueing all the 2's
    for i in range(r):
        for j in range(c):
            if mat[i][j]==2:
                que.append([i,j])
    time=0
    while que:
        curr_len=len(que)
        while curr_len:
            curr_len-=1
            x,y=que.popleft()
            #checking neighbour of the rotten orange
            if x>0 and mat[x-1][y]==1:
                mat[x-1][y]=2
                que.append([x-1,y])
            if y>0 and mat[x][y-1]==1:
                mat[x][y-1]=2
                que.append([x,y-1])
            if x<r-1 and mat[x+1][y]==1:
                mat[x+1][y]=2
                que.append([x+1,y])
            if y<c-1 and mat[x][y+1]==1:
                mat[x][y+1]=2
                que.append([x,y+1])
        time+=1
    #checking if there are any 1's left
    for row in mat:
        if 1 in row:
            return -1
    #else time
    return time-1




for _ in range(int(input())):
    r,c=map(int,input().split())
    arr=list(map(int,input().split()))
    mat=[]
    for i in range(0,r*c,c):
        mat.append(arr[i:i+c])
    #print(mat)
    print(fill(mat,r,c))
