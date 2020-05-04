



def isSafe( i, j, visited,n,m,a): 
    return (i >= 0 and i < n and j >= 0 and j < m and not visited[i][j] and a[i][j])
    
    
def dfs(i,j,visited,n,m,a):
    rowNbr = [-1,-1,-1,0,0,1,1,1]
    colNbr = [-1,0,1,-1,1,-1, 0, 1]
    visited[i][j]=True
    for k in range(8): 
        if isSafe(i + rowNbr[k], j + colNbr[k], visited,n,m,a): 
            dfs(i + rowNbr[k], j + colNbr[k], visited,n,m,a) 

def findIslands(a,n,m):
    #code here
    visited = [[False for j in range(m)]for i in range(n)]
    no_islands=0
    for i in range(n):
        for j in range(m):
            if visited[i][j]==False and a[i][j] ==1:
                dfs(i,j,visited,n,m,a)
                no_islands+=1
    return no_islands
    
