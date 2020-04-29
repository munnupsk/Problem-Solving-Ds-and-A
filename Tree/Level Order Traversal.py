


def levelOrder( root ):
    # Code here
    if not root:
        return 
    q=[]
    q.append(root)
    while len(q):
        temp=q.pop(0)
        print(temp.data,end=" ")
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
        
