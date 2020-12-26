# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:01:19 2020

@author: shriyansh jain
"""

def filter_long_words(lst,n):
    temp=[]
    for i in lst:
        if len(i)>n:
            temp.append(i)
    return temp        


lst=["shriyansh","jain","cricket","basketball","football","Hockey"]
n=5

var=filter_long_words(lst, n)

print(var)