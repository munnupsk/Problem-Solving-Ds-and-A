


def bToDLL(root):
    # do Code here
    global l1
    l1=[]
    def tr(temp):
        global l1
        if temp!=None:
            tr(temp.left)
            l1.append(temp.data)
            tr(temp.right)
        else:
            return
    tr(root)
    r=Node(l1[0])
    temp=r
    temp1=r
    for i in range(1,len(l1)):
        temp.right=Node(l1[i])
        temp.right.left=temp1
        temp1=temp.right
        temp=temp.right

    return r
