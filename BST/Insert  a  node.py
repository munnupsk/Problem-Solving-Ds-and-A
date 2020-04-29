
'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

def insert(root,k):
    # code here
    newNode=Node(k)
    x=root
    y=None
    while x:
        y=x
        if x.data>k:
            x=x.left
        elif x.data<k:
            x=x.right
        else:
            break
    if  y is None:
        root=newNode
    elif y.left==k:
        return root
    elif y.right==k:
        return root
    elif k<y.data:
        y.left=newNode
    elif k>y.data:
        y.right=newNode
    
    return root
    
        
        
    
