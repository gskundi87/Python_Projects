# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 09:40:19 2021

@author: p4ul
"""

import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('c:\\Users\\p4ul\\Documents\\R_Projects\\HighwaySign.txt',sep='\t',header=None,names=["Age","Distance"])

x = df["Age"]
x = sm.add_constant(x)

y = df["Distance"]

model = sm.OLS(y, x).fit()
predictions = model.predict(x) # make the predictions by the model

# Print out the statistics
print(model.summary())
