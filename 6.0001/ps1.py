# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:42:56 2020

@author: p4u1
"""
####################
#    Problem 1
####################

# annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# total_cost = float(input("Enter the cost of your dream home: "))

# portion_down_payment = 0.25
# r = 0.04
# current_savings = 0.00
# months = 0

# while current_savings <= total_cost*portion_down_payment:
#     current_savings += current_savings*(r/12)
#     current_savings += (annual_salary/12)*portion_saved
#     months += 1
    
# print("Number of months: %d" % months)

####################
#    Problem 2
####################

# annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# total_cost = float(input("Enter the cost of your dream home: "))
# semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# portion_down_payment = 0.25
# r = 0.04
# current_savings = 0.00
# months = 0

# while current_savings <= total_cost*portion_down_payment:
#     current_savings += current_savings*(r/12)
#     current_savings += (annual_salary/12)*portion_saved
#     months += 1
#     if months % 6 == 0:
#         annual_salary += semi_annual_raise*annual_salary
    
# print("Number of months: %d" % months)

####################
#    Problem 3
####################

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
cost = 1000000
step = 0

fixed_annual_salary = float(input("Enter your annual salary: "))
low = 0
high = 10000

while(True):
    step += 1
    current_savings = 0.00
    temp_annual_salary = fixed_annual_salary
    portion_saved = (high + low) // 2
    
    for month in range(1,37):
        current_savings += current_savings*(r/12)
        current_savings += (temp_annual_salary/12)*(portion_saved / 10000)
        if month % 6 == 0:
            temp_annual_salary += semi_annual_raise*temp_annual_salary
            
    if abs(cost*portion_down_payment - current_savings) <= 100:
        break;
    elif cost*portion_down_payment < current_savings:
        high = portion_saved
    else:
        low = portion_saved
        
print("Best savings rate: %0.4f" % (portion_saved/10000))
print("Steps in bisection search: %d" % step)