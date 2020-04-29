
'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def minValueNode(node):
    current=node
    while(current.left is not None): 
        current = current.left  
    return current 
def deleteNode(root, key):
    # code here.
    if root is None:
        return root
    if key <root.data:
        root.left=deleteNode(root.left,key)
    elif key>root.data:
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right , temp.data) 
    return root
