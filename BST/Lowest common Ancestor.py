

def LCA(root,n1,n2):
    #code here.
    '''
    :param root: given root of the bst
    :param n1: value one.
    :param n2: value two.
    :return: Lowest common Ancestor address.
    '''
    while root:
        if root.data>n1 and root.data>n2:
            root=root.left
        elif root.data<n1 and root.data<n2:
            root=root.right
        else:
            return root
    
