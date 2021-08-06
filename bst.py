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

    def set_left(self,node):
        self.left = node

    def set_right(self,node):
        self.right = node

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
            
        # if self.root == None:
        #     self.root = bst_node(v,None)
        # else:
        #     flag = None
        #     temp1 = self.root
        #     temp2 = None
        #     while temp1 != None:
        #         if v < temp1.get_value():
        #             flag = False
        #             temp2 = temp1
        #             temp1 = temp1.get_left()
        #         elif v > temp1.get_value():
        #             flag = True
        #             temp2 = temp1
        #             temp1 = temp1.get_right()
        #         else:
        #             temp1.increase_count()
        #             return
            
        #     if flag:
        #         temp2.set_right(bst_node(v,temp2))
        #     else:
        #         temp2.set_left(bst_node(v,temp2))

    def print_tree(self,node=bst_node):
        if node != None:
            self.print_tree(node.get_left())
            print(node.get_value())
            self.print_tree(node.get_right())

import random

items = [random.randrange(100) for i in range(25)]

tree = bst()

for item in items:
    tree.insert(item)

tree.print_tree(tree.get_root())
