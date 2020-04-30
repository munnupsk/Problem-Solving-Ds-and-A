

def lca(root, n1, n2):
    # Code here
    
    #inorder traversal
    if not root:
        return None
    
    if root.data==n1 or root.data==n2:
        return root
        
    l=lca(root.left,n1,n2)
    r=lca(root.right,n1,n2)

    if l and r:
        return root
    elif l:
        return l
    return r
