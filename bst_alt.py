# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:04:42 2021

@author: p4u13
"""

"""
AS OF 9/21/21 - BST_ALT DOES NOT KEEP TRACK OF STSize or height
THIS IS DONE IN AVL_ALT
FURTHER ENHANCEMENT SHOULD BE TO HAVE BOTH BE STANDALONE WITH
FULL NODE FUNCTIONALITY INCLUDING HEIGHTS AND STSize(to get rank)
"""
    
class BST_NODE():
    def __init__(self,k,p):
        self.parent = p
        self.left = None
        self.right = None
        self.key = k
        self.STSize = 1
        self.count = 1
        self.height = 0
        
    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent 
            return self
        else:
            s = self.successor()
            self.key, s.key = s.key, self.key
            self.count, s.count = s.count, self.count
            return s.delete() 
        
    def find(self,k):
        if k == None:
            return
        
        if k == self.key:
            return self
        elif k < self.key:
            if self.left == None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right == None:
                return None
            else:
                return self.right.find(k)
            
    def find_man(self):
        current = self
        while current.right != None:
            current = current.right
        return current
            
    def find_min(self):
        current = self
        while current.left != None:
            current = current.left
        return current
    
    def get_height(node):
        if node == None:
            return -1
        else:
            return node.height
        
    def insert(self,k):
        if k == None:
            return
        
        if k == self.key:
            self.count += 1
            x = self
        elif k < self.key:
            if self.left == None:
                self.left = BST_NODE(k,self)
                x = self.left
            else:
                x = self.left.insert(k)
        else:
            if self.right == None:
                self.right = BST_NODE(k,self)
                x = self.right
            else:
                x = self.right.insert(k)
                
        return x
            
    def predecessor(self):
        if self.left != None:
            return self.left.find_max()
        current = self
        while current.parent != None and current.parent.left == self:
            current = current.parent
        return current.parent
    
    def rank(self, k):
        """Return the number of keys <= k in the subtree rooted at this node."""
        if k == None:
            return
        
        left_size = 0 if self.left is None else self.left.STSize 
        
        if k == self.key:
            return left_size + 1
        elif k < self.key:
            if self.left is None:
                return 0
            else:
                return self.left.rank(k)
        else:
            if self.right is None:
                return left_size + 1
            else:
                return self.right.rank(k) + left_size + 1 
            
    def successor(self):
        if self.right != None:
            return self.right.find_min()
        current = self
        while current.parent != None and current.parent.right == self:
            current = current.parent
        return current.parent
        
class BST(object):
    def __init__(self):
        self.root = None
        
    def delete(self, k):
        """Delete the node for key k if it is in the tree."""
        node = self.find(k)
        if node == None:
            return None
        return node.delete()
    
    def find(self, k):
        """Return the node for key k if is in the tree, or None otherwise."""
        if self.root is None:
            return None
        else:
            return self.root.find(k)
        
    def insert(self, k):
        """Insert key k into this BST, modifying it in-place."""
        if self.root is None:
            self.root = BST_NODE(k,None)
            return self.root
        else:
            return self.root.insert(k)
        
    def rank(self, k):
        """The number of keys <= k in the tree."""
        if self.root is None:
            return 0
        else:
            return self.root.rank(k)  
            
    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])
            
# import random

# items = [random.randrange(100) for i in range(25)]

# tree = BST()

# for item in items:
#     tree.insert(item)

# print(tree)
                
        