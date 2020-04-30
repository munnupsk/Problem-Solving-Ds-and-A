


def height(node):
    if node is None:
        return 0
    return 1+max(height(node.left),height(node.right))
    
def diameter(root):
    # Code here
    if root is None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    
    ldiameter=diameter(root.left)
    rdiameter=diameter(root.right)
    
    return max(lh+rh+1,max(ldiameter,rdiameter))
    
