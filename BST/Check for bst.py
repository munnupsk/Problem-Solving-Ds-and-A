


def isbst_rec(root): 
    global prev  
    if root is None: 
        return True
    if isbst_rec(root.left) is False: 
        return False
    if prev is not None and prev.data >= root.data: 
        return False
    prev = root 
    return isbst_rec(root.right)
    
def isBST(node):
    #code here
    
    global prev 
    prev = None
    res= isbst_rec(root) 
    if res :
        return 1
    return 0
