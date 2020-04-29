

flag=True
def res(root):
    global flag
    if root is None:
        return  0
    a,b=res(root.left),res(root.right)
    if abs(a-b)>1:
        flag=False
    return max(a,b)+1
    
def isBalanced(root):
    global flag
    flag=True
    res(root)
    return flag

