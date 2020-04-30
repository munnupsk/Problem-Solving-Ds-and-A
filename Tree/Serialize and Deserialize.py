



def serialize(root, A):
    #code here
    #preorder
    if not root:
        A.append(-1)
        return
    A.append(root.data)
    serialize(root.left,A)
    serialize(root.right,A)
    
index=0

def deSerialize(A):
    #code here
    global index
    
    if A[index]==-1 or index>=len(A):
        index+=1
        index%=len(A)
        return None
    
    root=Node(A[index])
    index+=1
    root.left=deSerialize(A)
    root.right=deSerialize(A)
    return root
    
