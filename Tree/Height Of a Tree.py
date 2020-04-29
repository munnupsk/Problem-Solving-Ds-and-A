


def height(root):
    
    if root is None:
        return 0
    else:
        ldepth=height(root.left)
        rdepth=height(root.right)
        if ldepth>rdepth:
            return ldepth+1
        return rdepth+1

