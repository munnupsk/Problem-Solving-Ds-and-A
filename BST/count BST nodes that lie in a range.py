#https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1

def inorder(root,lis):
    if root is None:
        return 
    inorder(root.left,lis)
    lis.append(root.data)
    inorder(root.right,lis)
    
    
def getCountOfNode(root,l,h):
    ##Your code here
    lis=[]
    inorder(root,lis)
    count=0
    for i in lis:
        if i>=l and i<=h:
            count+=1
    return count

