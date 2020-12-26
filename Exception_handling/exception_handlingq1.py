# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:44:57 2020

@author: shriyansh jain
"""

try:
    a = 5/0
    print(a)
    
except ZeroDivisionError as e:
    print("You cannot divide a number by 0")
    print(e)