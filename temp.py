# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# def cube_root(cube, epsilon):
#     if abs(cube) < 1 and abs(cube) > 0:
#         high = 1
#         low = 0
#     else:
#         high = abs(cube)
#         low = 0
        
#     root = (high + low)/2.0
        
#     while abs(abs(cube) - root**3) >= epsilon:
#         if root**3 < abs(cube):
#             low = root
#         else:
#             high = root
#         root = (high + low)/2.0
    
#     if cube < 0:    
#         return -root
    
#     return root

# def cube_root_2(cube, epsilon):
#     low = min(-1.0,cube)
#     high = max(1.0,cube)
#     root = (high + low)/2.0
        
#     while abs(abs(cube) - root**3) >= epsilon:
#         if root**3 < abs(cube):
#             low = root
#         else:
#             high = root
#         root = (high + low)/2.0
        
#     if cube < 0:
#         return -root
    
#     return root
        
# print(cube_root_2(-0.23,0.0001))

# x = 0.0

# for i in range(10):
#     x = x + 0.1
#     if x == 1.0:
#         print(x, '= 1.0')
#     else:
#         print(x, 'is not 1.0')

# import sympy as sym

# x = sym.symbols('x')

# def newton_raphson(expr,guess,epsilon):
#     der = sym.diff(expr)
    
#     while abs(expr.subs(x,guess)) >= epsilon:
#         guess = guess - (expr.subs(x,guess)/der.subs(x,guess))
#     print(guess)
#     print(expr.subs(x,guess))
    
# expr = x**5+2*x**4-3*x**3
# newton_raphson(expr, -2.4, 0.00001)

# def isIn(str1, str2):
#     if str1 in str2:
#         return True
#     else:
#         return False
    
# print(isIn("apple", "apples"))
# print(isIn("jepper", "laftum"))


# def findRoot(x, power, epsilon):
#     """Assumes x and epsilon int or float, power an int,
#     epsilon > 0 & power >= 1
#     Returns float y such that y**power is within epsilon of x.
#     If such a float does not exist, it returns None"""
#     if x < 0 and power%2 == 0: #Negative number has no even-powered roots
#         return None
#     low = min(-1.0, x)
#     high = max(1.0, x)
#     ans = (high + low)/2.0
#     while abs(ans**power - x) >= epsilon:
#         if ans**power < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low)/2.0
#     return ans

# def testFindRoot():
#     epsilon = 0.0001
#     for x in [0.25, -0.25, 2, -2, 8, -8]:
#         for power in range(1, 4):
#             print('Testing x =', str(x), 'and power = ', power)
#             result = findRoot(x, power, epsilon)
#             print(result)
#             if result == None:
#                 print(' No root')
#             else:
#                 print(' ', result**power, '~=', x)
                
# testFindRoot()




    
                          
    
    
                
    
