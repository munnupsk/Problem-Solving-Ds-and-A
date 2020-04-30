

INT_MIN = -2**32
def maxPathSumUtil(root, res): 

    if root is None: 
        return 0
      
    if root.left is None and root.right is None: 
        return root.data 
 
    ls = maxPathSumUtil(root.left, res) 
    rs = maxPathSumUtil(root.right, res) 
  
    
    if root.left is not None and root.right is not None: 
        res[0] = max(res[0], ls + rs + root.data) 
        return max(ls, rs) + root.data 
          
    
    if root.left is None: 
        return rs + root.data 
    else: 
        return ls + root.data 

def maxPathSum(root):
    res = [INT_MIN] 
    maxPathSumUtil(root, res) 
    return res[0] 
  
