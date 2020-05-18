

ans = []

def get_ans(n):
    
    grid = [[None for i in range(n)] for i in range(n)]
    tmp_ans_list = []
    
    # Checks if there is a collision with any queen    
    def check(row, col):
        
        # Check row wise
        for i in range(row):
            # Check for left diagonal.
            # If position within the array check further
            if col-(row-i) >= 0:
                if grid[i][col-(row-i)] != None: return False
            
            # Check for right diagonal.
            # If position within the array check further
            if col+(row-i) <= n-1:
                if grid[i][col+(row-i)] != None: return False
            
            # Check for element straight up
            if grid[i][col] != None:
                return False
                
        return True
    
    # Recurse starting from top row to bottom
    def recurse(row):
        global ans
        
        if row == n:
            return True
        
        found = False
        
        # traverse left to right
        for curr_col in range(n):
            
            # Check for collision
            if check(row, curr_col):

                grid[row][curr_col] = row+1
                
                # Append [curr_col, row+1] so we can later sort on basis of curr_col
                ans.append([curr_col, row+1])
                
                # Recurse for next row. At this step the recurse func will be called
                # till we reach the last row(if possible) else we would move to next
                # column
                if recurse(row+1):
                    found = True
                    ans_copy = ans.copy()
                    ans_copy.sort(key = lambda x: x[0])
                    tmp_ans_list.append([x[1] for x in ans_copy])
                
                # If failed then remove the value from grid as well as ans
                grid[row][curr_col] = None
                ans.pop(-1)
        
        return found
        
    recurse(0)
    
    # To store the true answers
    new_ans_list = []
    for ans in tmp_ans_list:
        if len(ans) == n:
            new_ans_list.append(ans)
            
    if not new_ans_list:
        print(-1, end = '')
    else:
        new_ans_list.sort(key = lambda x: [e for e in x])
        for ans in new_ans_list:
            print('[', end = '')
            print(*ans, end = ' ')
            print(']', end = ' ')
    
    print()
    

cases = int(input())
for _ in range(cases):
    n = int(input())
    get_ans(n)
