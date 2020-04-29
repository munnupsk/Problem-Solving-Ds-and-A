
#https://practice.geeksforgeeks.org/problems/closest-neighbor-in-bst/1

def inorder(root,lis):
    if root is None:
        return 
    inorder(root.left,lis)
    lis.append(root.data)
    inorder(root.right,lis)
    
def findMaxforKey(root,k):
    if not root:
        return None
    lis=[]
    inorder(root,lis)
    res=-1
    for i in range(len(lis)-1,-1,-1):
        if lis[i]<k:
            res=lis[i]
            break
    print(res)
