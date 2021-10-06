import bst_alt

def get_count(node):
    if node == None:
        return 0
    left = get_count(node.left)
    right = get_count(node.right)
    return node.count + left + right
    
def get_height(node):
    if node == None:
        return -1
    else:
        return node.height
    
def update_stats(node):
    node.STSize = (0 if node.left is None else node.left.STSize) + (0 if node.right is None else node.right.STSize) + 1 
    node.height = max(get_height(node.left), get_height(node.right)) + 1

class AVL(bst_alt.BST):
    """
AVL binary search tree implementation.
Supports insert, delete, find, find_min, next_larger each in O(lg n) time.
"""
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_stats(x)
        update_stats(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_stats(x)
        update_stats(y)

    def rebalance(self, node):
        while node is not None and node.key is not None:
            update_stats(node)
            if get_height(node.left) >= 2 + get_height(node.right):
                if get_height(node.left.left) >= get_height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif get_height(node.right) >= 2 + get_height(node.left):
                if get_height(node.right.right) >= get_height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    ## other methods inherited from bst_alt.py

    def insert(self, k):
        """Inserts a node with key k into the subtree rooted at this node.
        This AVL version guarantees the balance property: h = O(lg n).
        
        Args:
            k: The key of the node to be inserted.
        """
        node = super(AVL, self).insert(k)
        self.rebalance(node)

    def delete(self, k):
        """Deletes and returns a node with key k if it exists from the BST.
        This AVL version guarantees the balance property: h = O(lg n).
        
        Args:
            k: The key of the node that we want to delete.
            
        Returns:
            The deleted node with key k.
        """
        node = super(AVL, self).delete(k)
        ## node.parent is actually the old parent of the node,
        ## which is the first potentially out-of-balance node.
        self.rebalance(node.parent)

import random

items = [random.randrange(100) for i in range(25)]

tree = AVL()

for item in items:
    tree.insert(item)

print(tree)
