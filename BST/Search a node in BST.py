#https://practice.geeksforgeeks.org/problems/search-a-node-in-bst/1


class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class BST:
    def search(self, node, data):
        #code here
        if node is None:
            return False
        if node.data==data:
            return True
        if node.data>data:
            return self.search(node.left,data)
        return self.search(node.right,data)

