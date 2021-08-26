class BST_NODE():
    def __init__(self,v,p):
        self.value = v
        self.count = 0
        self.parent = p
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.value)

class BST():
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self,v):
        temp2 = None
        temp1 = self.root
        
        while temp1 != None:
            temp2 = temp1
            if v < temp1.value:
                temp1 = temp1.left
            elif v > temp1.value:
                temp1 = temp1.right
            else:
                temp1.count += 1
                return
            
        x = BST_NODE(v, temp2)
        
        if temp2 == None:
            self.root = x
        elif v < temp2.value:
            temp2.left = x
        else:
            temp2.right = x
            
        return x

    def find(self,n,v):        
        while n != None and n.value != v:
            if n.value > v:
                n = n.left
            else:
                n = n.right
                
        return n
            
    def find_min(self,n):        
        x = n
        
        while x.left != None:
            x = x.left
            
        return x
            
    def find_max(self,n):
        x = n
        
        while x.right != None:
            x = x.right
            
        return x
    
    def next_larger(self,n):
        if n.right != None:
            return self.find_min(n.right)
        
        x = n.parent
        
        while x != None and n == x.right:
            n = x
            x = n.parent
        
        return x
    
    def next_smaller(self,n):
        if n.left != None:
            return self.find_max(n.left)
        
        x = n.parent
        
        while x != None and n == x.left:
            n = x
            x = n.parent
        
        return x
    
    def transplant(self,u,v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
            
    def delete(self,n):
        if n.left == None:
            self.transplant(n,n.right)
        elif n.right == None:
            self.transplant(n,n.left)
        else:
            x = self.find_min(n.right)
            
            if n != x.parent:
                self.transplant(x,x.right)
                x.right = n.right
                x.right.parent = x
                
            self.transplant(n,x)
            x.left = n.left
            x.left.parent = x
                
            
    def __str__(self):
        if self.root is None:
            return '<empty tree>'
        def recurse(node):
            if node is None:
                return [], 0, 0
            label = str(node.value)
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
