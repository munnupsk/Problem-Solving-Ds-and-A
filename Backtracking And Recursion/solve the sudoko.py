

def print_sudoku(arr,li):
    
    for i in range(9): 
        for j in range(9):
            
            
            
                
            li.append(arr[i][j])
            
            
        

def find_empty_location(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False
  

def used_in_row(arr,row,num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  
 
def used_in_col(arr,col,num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  

def used_in_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                return True
    return False
    
    
def check_location_is_safe(arr,row,col,num): 
      
     
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num) 
  

def solve_sudoku(arr): 
      
       
    l=[0,0] 
      
        
    if(not find_empty_location(arr,l)): 
        return True
      
    
    row=l[0] 
    col=l[1] 
      
    # consider digits 1 to 9 
    for num in range(1,10): 
          
        # if looks promising 
        if(check_location_is_safe(arr,row,col,num)): 
              
            # make tentative assignment 
            arr[row][col]=num 
  
            # return, if success, ya! 
            if(solve_sudoku(arr)): 
                return True
  
            # failure, unmake & try again 
            arr[row][col] = 0
              
            
    return False 
for i in range(int(input())):
    li=list(map(int,input().split()))
    l=[]
    arr=[[0]*9 for i in range(9)]
    c=0
    for i in range(9):
        for j in range(9):
            arr[i][j]=li[c]
            c+=1
    
    solve_sudoku(arr)
        
    print_sudoku(arr,l)
    for i in range(81):
        print(l[i],end=" ")
    print()
    
        
