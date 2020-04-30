



def inorder(root): 
    global v 
      
    if (root == None): 
        return
 
    inorder(root.left) 
  
  
    v.append(root.data) 
    
    inorder(root.right) 

def bTreeToClist(root):
    global v 

    if (root == None): 
        return None
  

    v = [] 

    inorder(root) 

    head_ref = Node(v[0]) 
    curr = head_ref 
  
    i = 1
    while ( i < len(v)) : 
      

        temp = curr 
  
        curr.right = Node(v[i]) 
  

        curr = curr.right 
  
      
        curr.left = temp 
        i = i + 1
  
    
    curr.right = head_ref 
  

    head_ref.left = curr 
  

    return head_ref 
