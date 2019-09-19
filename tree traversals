class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
class binarytree:
    def __init__(self,root):
        self.root=Node(root)
        #self.root stores the address of the root node 
    
    def print_tree(self,traversal_type):
        if traversal_type=="preorder":
            return self.preorder_print(tree.root,"")
        elif traversal_type=="inorder":
            return self.inorder_print(tree.root,"")
        elif traversal_type=="postorder":
            return self.postorder_print(tree.root,"")
    
    
    #preorder
    def preorder_print(self,start,traversal):
        """" Root->left->right"""
        if start:
            traversal+=(str(start.key)+"-")
            traversal=self.preorder_print(start.left,traversal)
            traversal=self.preorder_print(start.right,traversal)
        return traversal
    #inorder
    def inorder_print(self,start,traversal):
        """left->Root->right"""
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal+=(str(start.key)+'-')
            traversal=self.inorder_print(start.right,traversal)
        return traversal
    def postorder_print(self,start,traversal):
        """left->right->root"""
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal+=(str(start.key)+'-')
            traversal=self.inorder_print(start.right,traversal)
            traversal+=(str(start.key)+'-')
        return traversal
        
        
        
tree=binarytree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4) 

print("preorder",tree.print_tree("preorder"))
print("inorder",tree.print_tree("inorder"))
print("postorder",tree.print_tree("postorder"))
