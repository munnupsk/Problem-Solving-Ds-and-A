


def isMirror(root1 , root2): 
    # If both trees are empty, then they are mirror images 
    if root1 is None and root2 is None: 
        return True 
    

    if (root1 is not None and root2 is not None): 
            if  root1.data == root2.data: 
                return (isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left))
    return False
def isSymmetric(root):
    return isMirror(root,root)

