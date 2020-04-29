def inorder(root,lis):
    if not root:
        return 
    inorder(root.left,lis)
    lis.append(root.data)
    inorder(root.right,lis)
def isPairPresent(root,summ): 
    # code here.
    if root is None:
        return 0
    lis=[]
    inorder(root,lis)
    l=0
    r=len(lis)-1
    res=0
    while l<r:
        if lis[l]+lis[r]>summ:
            r-=1
        elif lis[l]+lis[r]<summ:
            l+=1
        else:
            res=1
            break
    return res
