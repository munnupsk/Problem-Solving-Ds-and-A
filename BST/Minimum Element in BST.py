


'''
class Node:
    data=0
    left=None
    right=None

'''
def inorder(root,lis):
    if root is None:
        return 
    inorder(root.left,lis)
    lis.append(root.data)
    inorder(root.right,lis)
    

def minValue(root):
    ##Your code here
    if root is None:
        return -1
    lis=[]
    inorder(root,lis)
    return lis[0]
