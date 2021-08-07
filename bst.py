class bst_node():
    def __init__(self,v,p):
        self.value = v
        self.count = 0
        self.parent = p
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_count(self):
        return self.count

    def increase_count(self):
        self.count += 1

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
    
    def set_parent(self,p):
        self.parent = p

    def set_left(self,node):
        self.left = node

    def set_right(self,node):
        self.right = node
        
    def __str__(self):
        return str(self.value)

class bst():
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self,v):
        temp2 = None
        temp1 = self.root
        
        while temp1 != None:
            temp2 = temp1
            if v < temp1.get_value():
                temp1 = temp1.get_left()
            elif v > temp1.get_value():
                temp1 = temp1.get_right()
            else:
                temp1.increase_count()
                return
            
        x = bst_node(v, temp2)
        
        if temp2 == None:
            self.root = x
        elif v < temp2.get_value():
            temp2.set_left(x)
        else:
            temp2.set_right(x)

    def find(self,n,v):        
        while n != None and n.get_value() != v:
            if n.get_value() > v:
                n = n.get_left()
            else:
                n = n.get_right()
                
        return n
            
    def find_min(self,n):        
        x = n
        
        while x.get_left() != None:
            x = x.get_left()
            
        return x
            
    def find_max(self,n):
        x = n
        
        while x.get_right() != None:
            x = x.get_right()
            
        return x
    
    def next_larger(self,n):
        if n.get_right() != None:
            return self.find_min(n.get_right())
        
        x = n.get_parent()
        
        while x != None and n == x.get_right():
            n = x
            x = n.get_parent()
        
        return x
    
    def transplant(self,u,v):
        if u.get_parent() == None:
            self.root = v
        elif u == u.get_parent().get_left():
            u.get_parent().set_left(v)
        else:
            u.get_parent().set_right(v)
        if v != None:
            v.set_parent(u.get_parent())
            
    def delete(self,n):
        if n.get_left() == None:
            self.transplant(n,n.get_right())
        elif n.get_right() == None:
            self.transplant(n,n.get_left())
        else:
            x = self.find_min(n.get_right())
            
            if n != x.get_parent():
                self.transplant(x,x.get_right())
                x.set_right(n.get_right())
                x.get_right().set_parent(x)
                
            self.transplant(n,x)
            x.set_left(n.get_left())
            x.get_left().set_parent(x)
                
            
    def __str__(self):
        if self.root is None:
            return '<empty tree>'
        def recurse(node):
            if node is None:
                return [], 0, 0
            label = str(node.get_value())
            left_lines, left_pos, left_width = recurse(node.get_left())
            right_lines, right_pos, right_width = recurse(node.get_right())
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.get_parent() is not None and \
               node is node.get_parent().get_left() and len(label) < middle:
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

import random

items = [random.randrange(100) for i in range(25)]

tree = bst()

for item in items:
    tree.insert(item)

print(tree)
