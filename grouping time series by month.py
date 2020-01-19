# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:23:46 2020

@author: Dell
"""

df
x=prices.groupby(by=[prices.index.month,prices.index.year]).sum()
print(x)