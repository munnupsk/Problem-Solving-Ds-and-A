

def LeftView(root):
    
    # code here
    q=[]
    q.append(root)
    q.append(None)
    while len(q):
        temp=q[0]
        if temp:
            print(temp.data,end=" ")
            
            while q[0]:
                temp = q[0] 
                  
                # If left child is present  
                # append into queue  
                if (temp.left) : 
                    q.append(temp.left)  
  
                # If right child is present  
                # append into queue  
                if (temp.right) : 
                    q.append(temp.right)  
  
                # Pop the current node  
                q.pop(0)  
            q.append(None)
        q.pop(0)
