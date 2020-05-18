flag=False
def findPath(arr, n):
    global flag
    ans_l = []
    flag=False
    
    # to keep track of visited coordinates to avoid loop
    visited = [[False]*n for i in range(n)]
    
    def recurse(i, j, path):
        global flag
        # Base condition
        if i == n-1 and j == n-1 and arr[i][j]==0:
            flag=False
            return
        
        if i == n-1 and j == n-1:
            flag=True
            ans_l.append(path)
            return
        
        # Base condition 
        if i < 0 or j < 0 or i >= n or j >= n or arr[i][j] == 0 or visited[i][j]:
            
            return
            
        else:
            
            # Mark this coordinate visited so to avoid coming back to this
            # coordinate for next recursion calls
            visited[i][j] = True
            
            
            
            # Go down
            recurse(i+1, j, path + 'D')
            
            # Go left
            recurse(i, j-1, path + 'L')
            
            # Go right
            recurse(i, j+1, path + 'R')
            
            # Go up
            recurse(i-1, j, path + 'U')
            
            # Mark this coordinate not visited so to explore more possible
            # directions
            visited[i][j] = False

    
    recurse(0, 0, '')
    if flag:
    
        return ' '.join(sorted(ans_l))
    else:
        return -1
      
