


def printSpiral(root):
    # Code here
    if not root:
        return
    s1=[]
    s2=[]
    s1.append(root)
    while len(s1) or len(s2):
        while len(s1):
            temp=s1[-1]
            s1.pop()
            print(temp.data,end=" ")
            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)
        while len(s2):
            temp=s2[-1]
            s2.pop()
            print(temp.data,end=" ")
            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)
    
        
